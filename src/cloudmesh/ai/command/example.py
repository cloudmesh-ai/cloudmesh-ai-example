import click
from cloudmesh.ai.common.io import console, path_expand
from cloudmesh.ai.common.logging_utils import get_contextual_logger
from cloudmesh.ai.common.telemetry import Telemetry

# Initialize Logger and Telemetry
logger = get_contextual_logger("example")
telemetry = Telemetry("example")

# Define the group for the command
example_group = click.group(name="example")

@example_group.command(name="hello")
def hello_cmd():
    """Hello command for example."""
    logger.info("Executing hello command")
    console.ok(f"Hello from example!")

@example_group.command(name="test-path")
@click.argument("path")
def test_path_cmd(path):
    """Example command showing path expansion."""
    expanded = path_expand(path)
    console.info(f"Expanded path: {expanded}")

def register(cli):
    """Registers the example command group to the main CLI."""
    cli.add_command(example_group),