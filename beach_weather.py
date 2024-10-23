from typing import Annotated
import typer
from rich import print

from config import STORMGLASS_API_TOKEN
from services.stormglass_api import DataSource, StormglassAPI

hours_info = typer.Option(
    help="How many hours weather data is requred.",
    show_default="Defauls to showing current hour data only.",
)

source_info = typer.Option(
    help="The weather institute would you like to use as the data source.",
    case_sensitive=False,
)


def main(
    hours: Annotated[int, hours_info] = 0,
    source: Annotated[DataSource, source_info] = "sg",
):
    stormglass_api = StormglassAPI(token=STORMGLASS_API_TOKEN, source=source)
    data = stormglass_api.get_point_weather_data(hours=hours)
    print(data)


if __name__ == "__main__":
    typer.run(main)
