from getAndSaveAsCSV import get_and_save_readings
import schedule
import time


def main():
    schedule.every(10).seconds.do(get_and_save_readings)
    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
