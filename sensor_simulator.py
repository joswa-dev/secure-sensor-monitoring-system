import random
import time

from database import SessionLocal
from models import SensorData
from alerts import check_alert


def generate_sensor_data():

    sensors = ["temperature", "pressure", "vibration"]

    while True:

        db = SessionLocal()

        sensor = random.choice(sensors)

        if sensor == "temperature":
            value = random.uniform(60, 100)

        elif sensor == "pressure":
            value = random.uniform(20, 80)

        else:
            value = random.uniform(10, 50)

        new_data = SensorData(
            sensor_name=sensor,
            sensor_value=value
        )

        db.add(new_data)
        db.commit()
        db.close()

        check_alert(sensor, value)

        print(f"{sensor} reading stored: {value:.2f}")

        time.sleep(3)