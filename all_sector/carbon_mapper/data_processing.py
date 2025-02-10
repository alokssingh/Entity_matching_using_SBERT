import json
import pandas as pd


def load_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


def serialize_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
