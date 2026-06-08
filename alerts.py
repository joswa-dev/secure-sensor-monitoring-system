from database import SessionLocal
from models import SensorData


def check_alert(sensor, value):

    if sensor == "temperature" and value > 90:
        print("⚠️ ALERT: High temperature detected!")

    elif sensor == "pressure" and value > 70:
        print("⚠️ ALERT: High pressure detected!")

    elif sensor == "vibration" and value > 45:
        print("⚠️ ALERT: Excess vibration detected!")