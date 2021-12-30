import click
import sys
from pathlib import Path
from .config import pass_config
import inquirer
from .default_command import DefaultCommandGroup
import click_completion
from .config import Config

click_completion.init()

global_data = {
    'config': None
}

def get_sources(ctx, args, incomplete):
    config = Config()
    keys = config.sources.keys()
    if incomplete:
        keys = list(filter(lambda x: x.startswith(incomplete), keys))
    return keys

@click.group(invoke_without_command=True, cls=DefaultCommandGroup)
@click.option('-s', '--source', required=True, autocompletion=get_sources)
@pass_config
def cli(config, source):
    global_data['config'] = config
    config.source = source



from . import fetch_latest_file