
import json
import random
import time
from datetime import datetime, timezone

SENSORS = [
    {"sensor_id": "SENSOR_001", "location": {"lat": 28.43, "lon": -9.42}},
    {"sensor_id": "SENSOR_002", "location": {"lat": 28.44, "lon": -9.41}},
    {"sensor_id": "SENSOR_003", "location": {"lat": 28.45, "lon": -9.40}},
]


def generate_measurement(sensor):
    is_anomaly = random.random() < 0.05

    pm25 = round(random.uniform(5, 35), 2)
    if is_anomaly:
        pm25 = round(random.uniform(100, 200), 2)

    return {
        "sensor_id": sensor["sensor_id"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "location": sensor["location"],
        "pm2_5": pm25,
        "pm10": round(random.uniform(10, 60), 2),
        "no2": round(random.uniform(5, 50), 2),
        "o3": round(random.uniform(10, 80), 2),
        "temperature": round(random.uniform(18, 40), 2),
        "humidity": round(random.uniform(20, 80), 2),
        "status": "active",
    }


def main():
    print("Starting IoT Air Quality Data Generator...", flush=True)

    try:
        while True:
            for sensor in SENSORS:
                measurement = generate_measurement(sensor)
                print(json.dumps(measurement), flush=True)

            time.sleep(5)

    except KeyboardInterrupt:
        print("\nGenerator stopped.")


if __name__ == "__main__":
    main()
