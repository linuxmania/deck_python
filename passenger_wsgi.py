import os
import sys
import json
import random

sys.path.insert(0, os.path.dirname(__file__))


def getValue(name):
    if name == 'Ace':
        return '1';
    elif name == 'King':
        return '13';
    elif name == 'Queen':
        return '12';
    elif name == 'Jack':
        return '11';
    else:
        return name;


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])

    def create_deck():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
        deck = []
        for suit in suits:
            for name in names:
                card = {
                    'name': name,
                    'suit': suit,
                    'value': getValue(name) 
                }
                deck.append(card)
                
        random.shuffle(deck)
        return deck
    
    deck = create_deck()
    
    deck_json = json.dumps(deck, indent=2)    
    
    return [deck_json.encode()]
