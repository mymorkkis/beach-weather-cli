from datetime import datetime, timedelta
from enum import Enum
from typing import NamedTuple

import requests
from rich import print


# TODO Add the data source full name to the cli help txt
class DataSource(str, Enum):
    noaa = "noaa"  # National Oceanic and Atmospheric Administration
    sg = "sg"  # Storm Glass AI


class PointWeatherData(NamedTuple):
    time: str
    air_temperature: float
    wave_height: float
    wind_speed: float


class StormglassAPI:
    def __init__(
        self,
        token: str,
        source: DataSource = "sg",
    ) -> None:
        self.token = token
        self.source = source

    def get_point_weather_data(self, hours: int) -> list[PointWeatherData]:
        start_timestamp = datetime.now()
        end_timestamp = start_timestamp + timedelta(hours=hours)

        response = requests.get(
            "https://api.stormglass.io/v2/weather/point",
            params={
                "lat": 38.6475853305747,
                "lng": -9.24349946254499,
                "params": "airTemperature,windSpeed,waveHeight",
                "source": self.source,
                "start": str(start_timestamp),
                "end": str(end_timestamp),
            },
            headers={"Authorization": self.token},
        )

        resp = response.json()

        print(
            f"Used {resp["meta"]["requestCount"]} out of {resp["meta"]["dailyQuota"]} daily requests"
        )

        return [
            PointWeatherData(
                time=str(datetime.fromisoformat(data["time"]).time()),
                air_temperature=data["airTemperature"][self.source],
                wave_height=data["waveHeight"][self.source],
                wind_speed=data["windSpeed"][self.source],
            )
            for data in resp["hours"]
        ]
