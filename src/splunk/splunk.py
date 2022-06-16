"""
Script containing functions to format data for splunk imports

Author: Mike Süberkrüb
"""
import datetime
import logging

import load_data.load as load


def extract_data(data: dict, config: dict) -> dict:
    """Extract the data specified in the config from data"""
    extracted_data: dict = {}

    if not isinstance(data, dict) or not isinstance(config, dict):
        logging.error("extract_data - data or config is invalid")
        raise TypeError

    if "import" not in config:
        logging.error("extract_data - Invalid config")
        raise TypeError

    for import_entry in config["import"]:
        # If the optional parameter data_destination is not set, set the data_location to data_destination
        if "data_destination" not in import_entry:
            import_entry["data_destination"] = import_entry["data_location"]

        try:
            extracted_data[import_entry["data_destination"]] = load.load_nested(data, import_entry["data_location"])
        except KeyError:
            extracted_data[import_entry["data_destination"]] = "not_found"
        except Exception as exception:
            logging.error(f"extract_data - data: {data} \n error: {exception}")
            extracted_data[import_entry["data_destination"]] = "error"

    return extracted_data


def add_timestamp(data: dict) -> dict:
    """Add a splunk recognisable timestamp"""
    data["@timestamp"] = datetime.datetime.now().strftime("%Y-%M-%DT%H:%M:%S")

    return data
