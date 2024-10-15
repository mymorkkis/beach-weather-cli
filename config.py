import os
from dotenv import load_dotenv

load_dotenv()

STORMGLASS_API_TOKEN = os.getenv("STORMGLASS_API_TOKEN")
if not STORMGLASS_API_TOKEN:
    raise EnvironmentError("Required env var STORMGLASS_API_TOKEN not provided")
