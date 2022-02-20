from unittest.mock import ANY, patch

import funcy
import pytest
from click.testing import CliRunner

import pada
from pada.cli import cli as _cli


@pytest.fixture
def cli():
    runner = CliRunner()
    return funcy.partial(runner.invoke, _cli)


def test_cli_version(cli):
    result = cli('--version')
    assert result.exit_code == 0
    assert pada.__version__ in result.output


@patch('pada.templating.render_project_template')
def test_create(mock_render, cli):
    cmd = 'create'
    result = cli(cmd)

    mock_render.assert_called_once()

    assert 'Generating new PADA project' in result.output

