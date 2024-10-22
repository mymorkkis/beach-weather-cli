from typing import Annotated
import typer
from rich import print

from config import STORMGLASS_API_TOKEN
from services.stormglass_api import StormglassAPI

hours_info = typer.Option(
    help="How many hours weather data is requred.",
    show_default="Defauls to showing current hour data only.",
)


def main(hours: Annotated[int, hours_info] = 0):
    stormglass_api = StormglassAPI(token=STORMGLASS_API_TOKEN)
    data = stormglass_api.get_point_weather_data(hours=hours)
    print(data)


if __name__ == "__main__":
    typer.run(main)
