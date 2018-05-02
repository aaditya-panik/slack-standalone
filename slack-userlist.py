import xlsxwriter
import argparse

from slackclient import SlackClient
from resources.credentials import SLACK_API_TOKEN
from resources.config import FIELDS_LIST
from typing import List

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="File name for output spreadsheet", type=str)


def add_to_workbook(workbook: xlsxwriter.Workbook, members: List):
    row = 1
    column = 0
    bold = workbook.add_format({'bold': 1})
    worksheet = workbook.add_worksheet('Slack')
    for key_value in members[0].keys():
        worksheet.write(0, column, key_value, bold)
        column += 1
    column = 0
    for member in members:
        for k in member:
            worksheet.write_string(row, column, member.get(k) if member.get(k) != '' else 'N/A')
            column += 1
        row += 1
        column = 0


def main(filename: str):
    sc = SlackClient(SLACK_API_TOKEN)
    users = sc.api_call("users.list")
    members = users.get('members')
    parsed_members = []
    for member in members:
        if member.get('id') != 'USLACKBOT' and not member.get('is_bot'):
            fields = {f: v for f, v in member.items() if f in FIELDS_LIST and f != 'profile'}
            if 'profile' in FIELDS_LIST:
                fields = {**fields, **{f: v for f, v in member.get('profile').items() if f in FIELDS_LIST}}
        else:
            continue
        if fields:
            parsed_members.append(fields)
    add_to_workbook(workbook=xlsxwriter.Workbook(filename+".xlsx"), members=parsed_members)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.filename:
        main(args.filename)
    else:
        main('slack-userlist')
