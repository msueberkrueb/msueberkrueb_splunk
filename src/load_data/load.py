"""
Script containing functions to load data

Author: Mike Süberkrüb
"""
import json


def load_json(path: str) -> dict[str, object]:
    """Return the data from a json file

    Args:
        path (str): The path of the file

    Raises:
        TypeError: If the path is not a string
        FileNotFoundError: If the config is not existing, or the path is wrong
        IsADirectoryError: If the path leads to a directory
        PermissionError: If the permissions are insufficient or IsADirectoryError on a Windows system

    Returns:
        dict: JSON dictionary containing the file data
    """

    # Checks if path is a string. If not: raise a TypeError
    if not isinstance(path, str):
        raise TypeError

    # Try to open the specified file -> extract and return its data
    try:
        with open(path, "r") as file:
            json_data = json.load(file)

        return json_data

    # Except the file is not present
    except FileNotFoundError as exception:
        raise FileNotFoundError from exception

    # Except the file is a directory
    except IsADirectoryError as exception:
        raise IsADirectoryError from exception

    # Except there is a PermissionError -> This is equivalent to a IsADirectoryError on Windows
    except PermissionError as exception:
        raise PermissionError from exception


def load_nested(nested: dict | list, target: list) -> object:
    """Return the value located at the path target in the list

    Args:
        nested (dict | list): Dict or list containing the targeted path and value.
        target (list): Path to the targeted key in the list. Format: ["Path", "To", "Target", "Key"].

    Raises:
        KeyError: If the current target is not in the list.

    Returns:
        object: Value from the targeted path
    """
    for element in target:
        if element in nested:
            nested = nested[element]
        else:
            raise KeyError

    return nested
