from getPower import get_power
from getCurrentAndVoltage import get_current_and_voltage
from datetime import datetime


def get_and_save_readings():
    print("Getting and saving readings...")

    power = get_power()
    current_and_voltage = get_current_and_voltage()
    readings = {**power, **current_and_voltage}

    try:
        open('history.csv')
        data = ""
    except (FileNotFoundError):
        data = "Time," + ",".join(readings.keys()) + "\n"

    data += datetime.now().strftime("%d/%m/%Y %H:%M:%S") + \
        ","+",".join(readings.values()) + "\n"

    history_file = open('history.csv', 'a')
    history_file.write(data)


if __name__ == "__main__":
    get_and_save_readings()
