from json.decoder import JSONDecodeError
from getPower import get_power
from getCurrentAndVoltage import get_current_and_voltage
import json
from datetime import datetime


def get_and_save_readings():
    print("Getting and saving readings...")

    power = get_power()
    current_and_voltage = get_current_and_voltage()
    readings = {**power, **current_and_voltage}

    try:
        data = json.load(open('history.json'))
    except (JSONDecodeError, FileNotFoundError):
        data = {}

    data.update({datetime.now().strftime("%d/%m/%Y %H:%M:%S"): readings})

    history_file = open('history.json', 'w+')
    history_file.write(json.dumps(data))


if __name__ == "__main__":
    get_and_save_readings()
