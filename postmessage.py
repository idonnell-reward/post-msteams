import pymsteams
import sys
import os
import json

file_path = '/github/workflow/event.json'
with open(file_path, 'r') as read_file:
    data = json.load(read_file)

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard(os.environ['TEAMS_WEBHOOK_URL'])
# Create Section 1
myTeamsMessage.title('New pull request submitted to '+ data['pull_request']['head']['repo']['full_name'])
myTeamsMessage.text('A new pull request has been submitted by ' + data['pull_request']['user']['login'])
# Add both Sections to the main card object
myTeamsMessage.addLinkButton('View', data['pull_request']['html_url'])
myTeamsMessage.send()
