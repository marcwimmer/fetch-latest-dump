import click
import sys
from pathlib import Path
from .config import pass_config
import inquirer
from .config import Config
from click_default_group import DefaultGroup


global_data = {
    'config': None
}

@click.group(invoke_without_command=True, cls=DefaultGroup, default='fetch', default_if_no_args=True)
@pass_config
def cli(config):
    global_data['config'] = config



from . import fetch_latest_file