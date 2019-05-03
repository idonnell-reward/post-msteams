
<img src="https://i.kym-cdn.com/photos/images/newsfeed/001/079/173/ed2.png" width="226" height="494"/>

## post-msteams

This repo contains a re-usable GitHub Action that when installed will post to Microsoft Teams details about various GitHub events.

This Action makes use of https://github.com/rveachkc/pymsteams for the Python code for Teams.

## Pre-requisites
 - A Microsoft Teams account.
 - Teams webhook "Incoming Webhook" added to the channel of your choice. This will provide a URL that will be added to the GitHub workflow as a secret. https://docs.microsoft.com/en-us/outlook/actionable-messages/actionable-messages-via-connectors 

## Setup

### 1. Create the release workflow

Add a new workflow to your `.github/main.workflow` to trigger on `issue_comment`.

<img src="img/new-workflow.png" alt="new-workflow" width="300" />

### 2. Create the Action

Create an action that uses this repository `idonnell-reward/post-msteams@master`

In the Action, create a secret called `TEAMS_WEBHOOK_URL` with your specific url to the Teams Channel:

<img src="img/webhook-secret.png" alt="webhook-secret" width="300" />

Add an event type environment varable called `GH_EVENT_TYPE`. As of now, this variable can be set to:
- push
- pull_request
- issue_comment
- issue

<img src="img/env-var.png" alt="env-var" width="300" />

### 3. Commit the changes

Make sure you commit all pending changes. After you've done that your `main.workflow` should look similar to this:

```
workflow "Issue comment to MS Teams" {
  on = "issue_comment"
  resolves = ["idonnell-reward/post-msteams"]
}

action "idonnell-reward/post-msteams" {
  uses = "chzbrgr71/post-msteams@master"
  secrets = ["TEAMS_WEBHOOK_URL"]
}
```

On the visual editor it should look similar to this:

<img src="img/workflow.png" alt="workflow" width="300" />

### 4. Test the workflow!

Create an PR in your repository. You should now see a post to your Teams channel!

## Local testing

The postmessage.py is the main program. You must set the below env var to run locally: `python postmessage.py`

```
TEAMS_WEBHOOK_URL=https://outlook.office.com/....
```

## Pull Requests and Issues are Welcome

Feel free to share your ideas.

:octocat::heart:


