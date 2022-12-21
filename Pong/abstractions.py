import time
import random
import pygame
import pymongo
from pygame.locals import *


def show_text(window, text, x, y, size=32, color=(255, 255, 255)):
    font_obj = pygame.font.SysFont('courier new', size)
    window.blit(font_obj.render(text, False, color), (x, y))


class Button:

    def __init__(self, text, x, y, width=150, height=75, color=(255, 0, 255)):
        self.text = text
        self.pos = [x, y]
        self.dim = [width, height]
        self.color = color
        self.rect = None

    def draw(self, window):
        self.rect = pygame.draw.rect(window, self.color, self.pos + self.dim)
        show_text(window, self.text, self.pos[0] + 5, self.pos[1] + 5)


class Ball:

    def __init__(self, x, y, rad=25, color=(0, 0, 255)):
        self.pos = [x, y]
        self.rad = rad
        self.color = color
        self.rect = None
        self.speed = 5
        self.vel = [
            random.choice([1, -1]) * random.random() * self.speed,
            random.choice([1, -1]) * random.random() * self.speed
        ]

    def draw(self, window):
        self.rect = pygame.draw.circle(window, self.color, self.pos, self.rad)

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def to_json(self):
        return {'vel': self.vel, 'pos': self.pos}


class Paddle:

    def __init__(self, x, y, width=10, height=150, color=(255, 0, 0)):
        self.pos = [x, y]
        self.dim = [width, height]
        self.color = color
        self.rect = None
        self.vel = 0
        self.speed = 5

    def draw(self, window):
        self.rect = pygame.draw.rect(window, self.color, self.pos + self.dim)

    def move(self):
        self.pos[1] += self.vel * self.speed

    def to_json(self):
        return {'pos': self.pos}


class Game:

    def __init__(self, client):
        self.mongo_client = pymongo.MongoClient(client)
        self.db = self.mongo_client['Pong']
        self.col = self.db['Games']
        self.time = time.time()
        self.players = []
        self.identity = None
        self.col.insert_one({'time': self.time, 'players': self.players, 'start': False})
        self.identity = self.col.find_one({'time': self.time})['_id']

    def add_player(self, player):
        self.players.append(player)
        self.update()

    def update(self):
        self.col.update_one({'_id': self.identity}, {'$set': {'players': self.players, 'start': len(self.players) == 2}})


class Player:

    def __init__(self, client):
        self.mongo_client = pymongo.MongoClient(client)
        self.db = self.mongo_client['Pong']
        self.col = self.db['Players']
        self.time = time.time()
        self.game = None
        self.col.insert_one({'time': self.time})
        self.identity = self.col.find_one({'time': self.time, 'game': None})['_id']

    def add_game(self, game):
        self.col.update_one({'_id': self.identity}, {'$set': {'server': game.identity}})
        game.add_player(self.identity)
