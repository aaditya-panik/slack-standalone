# Slack User-list

A Slack script to fetch users from a Workspace.

## Usage
### Install Slack App
1. Create a [Slack App](https://api.slack.com/apps).
2. Within Add feature and functionality >> Permissions >> Scope, add the `users:read` and `users:read:email` permissions and save the changes.
3. Once the changes are saved, in the same page you can install the app to the workspace.
Note: You need permissions in the workspace to 'Manage and Install Apps'.
4. Once you have authorized the app, the app will receive an OAuth Access Token of the form `xoxp-sample-token`.
5. Copy the token into the `resources/credentials.py` file.

### Run script
1. Install the requirements using `pip install -r requirements.txt`
2. Run the script using `python slack-userlist.py -f <INSERT-FILENAME>`
