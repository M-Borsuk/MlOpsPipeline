import yaml


def load_yaml(yaml_file: str) -> dict:
    """Function to load the configuration from a YAML file into a python dictionary

    Parameters:
    yaml_file {str} -- The path for the YAML file.

    Returns:
    A dictionary containing the configuration information.
    """

    file_stream = open(yaml_file, "r")
    config = yaml.load(file_stream, Loader=yaml.FullLoader)
    return config
