# import csv
# import json

from jira import JIRA
from invoke import task
from invoke.config import Config
from taiga_client.taiga import Taiga

Config = Config  # Silence flake8
jira = taiga = None


def _import_project(jira_project):
    slug = taiga.get_project_slug(jira_project.name)
    project = taiga.project_by_slug(slug)
    if project is None:
        project = taiga.create_project(jira_project.name, jira_project.name)
        # Create Project
        print("CREATED", project.name)
    else:
        print("PRESENT", project.slug)


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
