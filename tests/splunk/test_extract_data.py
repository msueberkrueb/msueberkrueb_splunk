"""
Tests the extract_data function of the splunk library

Author: Mike Süberkrüb
"""
import pytest
import os

from splunk.splunk import extract_data


@pytest.mark.parametrize("data, config", [
    ([], {}),
    ({}, []),
    ([], []),
])
def test_extract_data_type(data, config):
    """Tests if the extract_data function raises a TypeError with the parametrized types"""

    with pytest.raises(TypeError) as exception_info:
        extract_data(data, config)


@pytest.mark.parametrize("data, config", [
    ({}, {"import": []}),
])
def test_extract_data_config_valid(data, config):
    """Tests if a valid config format results in no error"""

    assert extract_data(data, config) == {}


@pytest.mark.parametrize("data, config", [
    ({}, {"no-import": []}),
])
def test_extract_data_config_invalid(data, config):
    """Tests if an invalid config format results in an error"""

    with pytest.raises(TypeError) as exception_info:
        extract_data(data, config)


@pytest.mark.parametrize("data, config, expected", [
    ({"test_data": "test"}, {"import": [{"data_location": "test_data", "data_destination": "test_data"}]},
     {'test_data': 'test'}),
    ({"test_other_data": "other_test"},
     {"import": [{"data_location": "test_other_data", "data_destination": "test_other_data"}]},
     {'test_other_data': 'other_test'}),
])
def test_extract_data_extraction(data, config, expected):
    """Tests if data can be extracted"""
    assert extract_data(data, config) == expected


@pytest.mark.parametrize("data, config, expected", [
    ({}, {"import": [{"data_location": "test_data", "data_destination": "test_data"}]}, {'test_data': 'not_found'}),
    ({}, {"import": [{"data_location": "test_other_data", "data_destination": "test_other_data"}]},
     {'test_other_data': 'not_found'}),
])
def test_extract_data_invalid_extraction(data, config, expected):
    """Tests if non existent data returns 'not_found'"""
    assert extract_data(data, config) == expected
