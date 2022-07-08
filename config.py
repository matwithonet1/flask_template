import json
import os

# Load the config file, if it exists.
_file = os.getenv('PL_ENV_FILE', "/path/to/config.json")

try:
    with open(_file) as config_file:
        _config_json = json.load(config_file)
except IOError:
    _config_json = {}
except:
    raise


def _get(name, default=None):
    """
    Return the value of a config variable. Priority is given to an environment
    variable. If it doesn't exist, the loaded config JSON is checked. Finally,
    it is set to `default` parameter if neither contain a value.
    """
    return os.getenv(name, _config_json.get(name, default))

POSTGRES_HOST = _get('POSTGRES_HOST', "some-network-address")

