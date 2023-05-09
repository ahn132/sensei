import requests
import json
from github import Github


def get_inspo():
    response = requests.get("https://zenquotes.io/api/random")

    # parses json into python dict
    json_data = json.loads(response.text)

    # gets content at quote key and author key from dictionary
    inspo = json_data[0]['q'] + " - " + json_data[0]['a']
    return inspo


def hook_git(discord_hook, token, repo_name):
    g = Github(token)
    repo = g.get_repo(repo_name)
    config = {
        "url": discord_hook,
        "content_type": "json"
    }
    events = ["branch_protection_rule", "check_run", "check_suite", "code_scanning_alert", "commit_comment", "create", "delete", "dependabot_alert", "deploy_key", "deployment", "deployment_status", "discussion", "discussion_comment", "fork", "gollum", "issue_comment", "issues", "label", "member", "meta", "milestone", "package", "page_build", "ping", "project_card", "project", "project_column", "public", "pull_request", "pull_request_review_comment", "pull_request_review", "pull_request_review_thread", "push", "registry_package", "release", "repository_advisory", "repository", "repository_import", "secret_scanning_alert", "secret_scanning_alert_location", "security_and_analysis", "star", "status", "team_add", "watch"]
    repo.create_hook("web", config, events, active=True)
