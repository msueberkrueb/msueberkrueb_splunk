"""
Tests the load_json function of the load_data library

Author: Mike Süberkrüb
"""
import pytest
import os

from load_data.load import load_json


@pytest.mark.parametrize("path", [
    (None),
    (0),
    (0.0),
    ([]),
    ({}),
])
def test_load_json_type(path):
    """Tests if the load_json function raises a TypeError with the parametrized types"""

    with pytest.raises(TypeError) as exception_info:
        load_json(path)


@pytest.mark.parametrize("path", [
    ("tests/load_data/testing_data/InvalidName.cfg"),
    ("tests/load_data/testing_data/settings.txt"),
    ("tests/load_data/testing_data/settings")
])
def test_load_json_path(path):
    """Tests if an invalid name or extension to a path file raises a FileNotFoundError"""

    with pytest.raises(FileNotFoundError) as exception_info:
        load_json(path)


@pytest.mark.parametrize("path", [
    ("tests/load_data/testing_data/directory_1"),
    ("tests/load_data/testing_data/directory_2"),
])
def test_load_json_directory(path):
    """Tests if a directory path raises a IsADirectoryError or a PermissionError"""

    # If the os is Windows, only the PermissionError is raised
    if os.name == "nt":
        with pytest.raises(PermissionError) as exception_info:
            load_json(path)

    # If the os isn't Windows, then the IsADirectoryError is raised
    else:
        with pytest.raises(IsADirectoryError) as exception_info:
            load_json(path)
