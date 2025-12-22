from blessed import Terminal
import random

term = Terminal()

fruits = [
    'apple',
    'banana',
    'cherry',
    'grapes',
    'mango',
    'orange',
    'peach',
]


colors = (
    term.red,
    term.green,
    term.yellow,
    term.blue,
    term.magenta,
    term.khaki,
    term.white,
)

for fruit in fruits:
    print(random.choice(colors)(fruit))