import json

import random

import kivy

from kivy.app import App

from kivy.uix.gridlayout import GridLayout

kivy.require('1.10.0')


class GameSelectLayout(GridLayout):

    def select_game(self, console):
        with open('{}.json'.format(console)) as data_file:
            game_list = json.load(data_file)
        return random.choice(game_list)


class GameSelectorApp(App):

    def build(self):
        return GameSelectLayout()


game_select_app = GameSelectorApp()


if __name__ == "__main__":
    game_select_app.run()
