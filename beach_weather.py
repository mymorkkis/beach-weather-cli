import typer
from rich import print

from config import STORMGLASS_API_TOKEN
from services.stormglass_api import StormglassAPI


def main():
    stormglass_api = StormglassAPI(token=STORMGLASS_API_TOKEN)
    data = stormglass_api.get_point_weather_data()
    print(data)


if __name__ == "__main__":
    typer.run(main)
