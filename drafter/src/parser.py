import argparse
from player import (
    FootballPlayer,
)
def parse_file(filename: str):
    print('asdf', filename)
    players = []
    with open(filename) as f:
        for line in f:
            print(line)
            players.append(FootballPlayer(line))
    print(players)
    return players

def parse():
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument('filename', help='Specify data file. .txt or .csv')
    args = cli_parser.parse_args()
    print(args)
    return parse_file(args.filename)
