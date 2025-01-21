import os
from pathlib import Path
import json
import random


class Json:

    def __init__(self):
        self.json_music = Path("music.json")
        self.music = Path("music")

    def set_json(self, to_json=None):
        if to_json is None:
            to_json = dict()
            for folder in Path("music").iterdir():
                to_json |= {folder.name: (1, dict.fromkeys([song.name for song in Path(
                    f"../music/{folder.name}").iterdir()], 1))}
            #to_json = dict.fromkeys([song.name for song in Path("music").iterdir()], 1)
        with self.json_music.open('w', encoding='UTF-8') as json_music:
            json.dump(to_json, json_music, indent=2)

    def get_json(self):
        with self.json_music.open(encoding='UTF-8') as json_music:
            return json.load(json_music)

    def get_json_song(self):
        json = self.get_json()
        size = sum(json.values())
        nums = [i for i in range(size)]
        songs = {}
        for key, value in json.items():
            random.shuffle(nums)
            temp = nums[:value]
            nums = nums[value:]
            songs |= dict.fromkeys(temp, key)
        return Path(f'../music/{songs[random.randint(0, size - 1)]}')
