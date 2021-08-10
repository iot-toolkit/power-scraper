import json
from getAndSaveAsCSV import get_and_save_as_csv
from getAndSaveAsJSON import get_and_save_as_json
import schedule
import time

config = json.load(open('config.json'))


def main():
    print("Program starting...")

    if config['fileFormat'] == "json":
        job = get_and_save_as_json
    else:
        job = get_and_save_as_csv

    job()
    schedule.every(config['interval']).seconds.do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
