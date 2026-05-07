import click
from cloudmesh.ai.common.io import console, path_expand
from cloudmesh.ai.common.logging_utils import get_contextual_logger
from cloudmesh.ai.common.telemetry import Telemetry

# Initialize Logger and Telemetry
logger = get_contextual_logger("{{name}}")
telemetry = Telemetry("{{name}}")

# Define the group for the command
{{name}}_group = click.group(name="{{name}}")

@{{name}}_group.command(name="hello")
def hello_cmd():
    """Hello command for {{name}}."""
    logger.info("Executing hello command")
    console.ok(f"Hello from {{name}}!")

@{{name}}_group.command(name="test-path")
@click.argument("path")
def test_path_cmd(path):
    """Example command showing path expansion."""
    expanded = path_expand(path)
    console.info(f"Expanded path: {expanded}")

def register(cli):
    """Registers the {{name}} command group to the main CLI."""
    cli.add_command({{name}}_group)