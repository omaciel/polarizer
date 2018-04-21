import os
import sys

import click

from rows import export_to_txt, Table

from polarizer.constants import PLAN_FIELDS
from polarizer.plan import get_plan
from polarizer.requirement import get_requirement


class Config(object):
    """Store Polarion attributes for all methods."""

    def __init__(self):
        self.username = os.environ.get('POLARION_USERNAME', None)
        self.password = os.environ.get('POLARION_PASSWORD', None)
        self.server = os.environ.get('POLARION_URL', None)

        # Get a valid web session if credentials are available.
        if not self.username and not self.password:
            click.echo('Please provide valid Polarion credentials!')
            sys.exit(-1)


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
def cli():
    '''CLI object.'''
    pass


@cli.command()
@click.option(
    '--product',
    required=True,
    type=str,
    help=("Product name"),
)
@click.option(
    '--requirement',
    '-r',
    required=True,
    type=str,
    help=("Requirement ID"),
)
@click.option(
    '--server',
    '-s',
    type=str,
    help=('Polarion server URL (e.g. https://example.com/polarion/)'),
)
@pass_config
def requirement(config, product, requirement, server):
    '''Display information about a Requirement.'''
    if server:
        config.server = server
    record = get_requirement(config, product, requirement)
    click.echo(f'Requirement: {record.id}')
    click.echo(f'Author: {record.author.name}')
    if hasattr(record.linkedWorkItemsDerived, 'LinkedWorkItem'):
        test_cases = record.linkedWorkItemsDerived.LinkedWorkItem
    else:
        test_cases = []
    click.echo(f'Test Cases: {len(test_cases)}')
    if test_cases:
        for test_case in test_cases:
            click.echo(f'  - {test_case.workItemURI}')


@cli.command()
@click.option(
    '--product',
    required=True,
    type=str,
    help=("Product name"),
)
@click.option(
    '--plan',
    required=True,
    type=str,
    help=("Plan ID"),
)
@click.option(
    '--server',
    '-s',
    type=str,
    help=('Polarion server URL (e.g. https://example.com/polarion/)'),
)
@pass_config
def plan(config, product, plan, server):
    '''Display information about a Plan.'''
    if server:
        config.server = server
    my_plan = get_plan(config, product, plan)

    bug_table = Table(fields=PLAN_FIELDS)

    if hasattr(my_plan, 'records'):
        for entry in my_plan.records[0]:
            if hasattr(entry.item, 'id'):
                # import pdb; pdb.set_trace()
                name = entry.item.id
                author = entry.item.author.name
                req = get_requirement(config, product, name)

                if hasattr(req.linkedWorkItemsDerived, 'LinkedWorkItem'):
                    test_cases = len(req.linkedWorkItemsDerived.LinkedWorkItem)
                else:
                    test_cases = 0
                bug_table.append({
                    'id': name,
                    'test_cases': test_cases,
                    'author': author,
                })
        print(export_to_txt(bug_table))
    else:
        click.echo(f'No requirements exist for {plan}.')
