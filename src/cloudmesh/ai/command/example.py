import click
from cloudmesh.ai.common.io import console, path_expand
from cloudmesh.ai.common.logging_utils import get_contextual_logger
from cloudmesh.ai.common.telemetry import Telemetry

# Initialize Logger and Telemetry
logger = get_contextual_logger("{{name}}")
telemetry = Telemetry("{{name}}")

# Define the group for the command
@click.group(name="{{name}}")
def {{name}}_group():
    """{{name}} command group."""
    pass

@{{name}}_group.command(name="run")
def run_cmd():
    """Run the main functionality of {{name}}."""
    logger.info("Executing {{name}} run command")
    console.ok(f"The {{name}} extension is running successfully!")

@{{name}}_group.command(name="test-path")
@click.argument("path")
def test_path_cmd(path):
    """Example command showing path expansion."""
    expanded = path_expand(path)
    console.info(f"Expanded path: {expanded}")

entry_point = {{name}}_group

def register(cli):
    """Registers the {{name}} command group to the main CLI."""
    cli.add_command({{name}}_group, name="{{name}}")
