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
            import_entry["data_destination"] = import_entry["data_location"][-1]

        try:
            extracted_data[import_entry["data_destination"]] = load.load_nested(data, import_entry["data_location"])
        except KeyError:
            extracted_data[import_entry["data_destination"]] = "not_found"
        except Exception as exception:
            logging.error(f"extract_data - data: {data} \n error: {exception}")
            extracted_data[import_entry["data_destination"]] = "error"

        # If the optional parameter split is set, split the string n times
        if "split" in import_entry:
            string = extracted_data[import_entry["data_destination"]]

            for index, delimiter in enumerate(import_entry["split"]["delimiters"]):
                if delimiter in string:
                    split_string = string.split(delimiter, 1)
                    extracted_data[import_entry["split"]["data_destinations"][index]] = split_string[0]
                    string = split_string[1]

                    if len(import_entry["split"]["delimiters"]) - 1 == index:
                        extracted_data[import_entry["split"]["data_destinations"][index + 1]] = string
                else:
                    # Resort to default behaviour, if the delimiter is not in the string
                    extracted_data[import_entry["split"]["data_destinations"][index]] = string

    return extracted_data


def add_timestamp(data: dict) -> dict:
    """Add a splunk recognisable timestamp"""
    data["@timestamp"] = datetime.datetime.now().strftime("%Y-%M-%DT%H:%M:%S")

    return data
