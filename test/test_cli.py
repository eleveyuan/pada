from unittest.mock import ANY, patch

import funcy
import pytest
from click.testing import CliRunner

import bricks
from bricks.cli import cli as _cli


@pytest.fixture
def cli():
    runner = CliRunner()
    return funcy.partial(runner.invoke, _cli)


def test_cli_version(cli):
    result = cli('--version')
    assert result.exit_code == 0
    assert bricks.__version__ in result.output


@patch('ballet.templating.render_project_template')
def test_create(mock_render, cli):
    cmd = 'create'
    result = cli(cmd)

    assert 'Generating new bricks project' in result.output

