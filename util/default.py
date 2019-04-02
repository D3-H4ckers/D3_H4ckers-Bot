import json
import PyColored as c
from collections import namedtuple


def getJSON(file: str) -> json:
    try:
        return json.load(open(file), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    except FileNotFoundError:
        raise FileNotFoundError(c.brightred(f'{file} file was not found.'))
