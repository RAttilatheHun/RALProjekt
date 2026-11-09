import json
import os

FILE = "ruhak.json"


def ral_betoltes():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def ral_mentes(adatok):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(adatok, file, indent=4, ensure_ascii=False)


def ral_lista(adatok):
    return [ruha for ruha in adatok if ruha["archivalt"]]