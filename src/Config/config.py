from pathlib import Path
import os

DATABASE_PATH = os.path.join(Path(__file__).parents[2], "db.json")
DATE_FORMAT = "%d/%m/%Y"
HOUR_FORMAT = "%d/%m/%Y %H:%M"
NB_PLAYERS = 8
NB_ROUNDS = 4
