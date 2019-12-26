# import csv
# import json

from jira import JIRA
from json import dumps
from invoke import task
from invoke.config import Config
from taiga_client.taiga import Taiga
from jira.exceptions import JIRAError

Config = Config  # Silence flake8
jira = taiga = None

TYPE_MAP = {
    'Story': 'user_story',
    'Other': 'issue',
    'Task': 'task',
    'Suggestion': 'issue',
    'Epic': 'epic',
    'Enhancement': 'issue',
    'Subtask': 'task',
    'Bug': 'issue',
    'Sub-task': 'issue',
}


def _build_ticket(issue, taiga_project):
    description = f'''
{issue.fields.description}

----------

```
{dumps(issue.raw, indent=4)}
```'''
    ticket = {
        'project': taiga_project.id,
        'subject': issue.fields.summary,
        'description': description,
        'tags': [f'JIRA:{issue.key}'],
        'is_closed': issue.fields.status.name in ['Closed', 'Resolved'],
        # 'is_blocked': issue.fields.status.name == 'Blocked',
        # 'blocked_note': 'Note for blocked!',
    }
    return ticket


def _build_user_story(issue, taiga_project):
    return _build_ticket(issue, taiga_project)


def _build_epic(issue, taiga_project):
    return _build_ticket(issue, taiga_project)


def _build_task(issue, taiga_project):
    return _build_ticket(issue, taiga_project)


def _build_issue(issue, taiga_project):
    return _build_ticket(issue, taiga_project)


def _create_issue(taiga_project, key, number):
    try:
        jira_issue = jira.issue(f'{key}-{number}')
    except JIRAError:
        return
    print("MIGRATING:", jira_issue)
    issue_type = jira_issue.fields.issuetype.name
    if TYPE_MAP[issue_type] == 'user_story':
        ticket = _build_user_story(jira_issue, taiga_project)
        taiga.create_userstory(ticket)
    elif TYPE_MAP[issue_type] == 'task':
        ticket = _build_task(jira_issue, taiga_project)
        taiga.create_task(ticket)
    elif TYPE_MAP[issue_type] == 'epic':
        ticket = _build_epic(jira_issue, taiga_project)
        taiga.create_epic(ticket)
    elif TYPE_MAP[issue_type] == 'issue':
        ticket = _build_issue(jira_issue, taiga_project)
        taiga.create_issue(ticket)
    else:
        raise NotImplementedError(TYPE_MAP[issue_type])


def _import_issues(jira_project, taiga_project):
    last_ticket = jira.search_issues(
        f'project="{jira_project.key}" ORDER BY created DESC', maxResults=1)
    if not last_ticket:
        return
    last_ticket = last_ticket[0]
    last_number = int(last_ticket.key.replace(f'{jira_project.key}-', ''))
    for number in range(1, last_number + 1):
        _create_issue(taiga_project, jira_project.key, number)


def _import_project(jira_project):
    slug = taiga.get_project_slug(jira_project.name)
    taiga_project = taiga.project_by_slug(slug)
    if taiga_project is None:
        print('CREATING: %s' % jira_project)
        taiga_project = taiga.create_project(
            jira_project.name, jira_project.name)
    _import_issues(jira_project, taiga_project)


@task
def j2t(c):
    global jira
    global taiga
    jira_auth = (c.config.j2t.jira_user, c.config.j2t.jira_pass)
    taiga_auth = (c.config.j2t.taiga_user, c.config.j2t.taiga_pass)
    jira = JIRA(c.config.j2t.jira_host, basic_auth=jira_auth)
    taiga = Taiga(c.config.j2t.taiga_host, normal_auth=taiga_auth)
    for jira_project in jira.projects():
        _import_project(jira_project)
