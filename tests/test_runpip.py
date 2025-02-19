import sys

import pytest  # type: ignore

from helpers import run_pipx_cli


def test_runpip(pipx_temp_env, monkeypatch, capsys):
    assert not run_pipx_cli(["install", "pycowsay"])
    assert not run_pipx_cli(["runpip", "pycowsay", "list"])


def test_runpip_global(pipx_temp_env, monkeypatch, capsys):
    if sys.platform.startswith("win"):
        pytest.skip("This behavior is undefined on Windows")
    assert not run_pipx_cli(["--global", "install", "pycowsay"])
    assert not run_pipx_cli(["--global", "runpip", "pycowsay", "list"])
