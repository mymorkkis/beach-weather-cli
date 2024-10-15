from datetime import datetime
from typing import NamedTuple

import requests
from rich import print


class PointWeatherData(NamedTuple):
    air_temperature: float
    wave_height: float
    wind_speed: float


class StormglassAPI:
    def __init__(
        self,
        token: str,
        source: str = "sg",
    ) -> None:
        self.token = token
        self.source = source

    def get_point_weather_data(self) -> PointWeatherData:
        now_timestamp = str(datetime.now())

        response = requests.get(
            "https://api.stormglass.io/v2/weather/point",
            params={
                "lat": 38.6475853305747,
                "lng": -9.24349946254499,
                "params": "airTemperature,windSpeed,waveHeight",
                "source": self.source,
                "start": now_timestamp,
                "end": now_timestamp,
            },
            headers={"Authorization": self.token},
        )

        resp = response.json()

        print(
            f"Used {resp["meta"]["requestCount"]} out of {resp["meta"]["dailyQuota"]} daily requests"
        )

        # TODO guard against no data and handle multiple hours
        data = resp["hours"][0]

        return PointWeatherData(
            air_temperature=data["airTemperature"][self.source],
            wave_height=data["waveHeight"][self.source],
            wind_speed=data["windSpeed"][self.source],
        )
