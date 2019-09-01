from abc import (
    ABC,
    abstractmethod,
)

# class Player(ABC):
    # '''
    # A PlayerSet is a collection of players that can be sum-ed to
    # '''
    # # def __init__(self):
        # # self.

    # @abstractmethod
    # def parse(self, row: str) -> None:
        # pass

class FootballPlayer:
    def __init__(self, row: str):
        pos, pick, val = self.parse(row)
        self.position = pos
        self.expected_pick = pick
        self.value = val

    def __str__(self):
        return '{} {} {}\n'.format(self.position, self.expected_pick, self.value)

    def parse(self, row: str) -> (str, int, float):
        print('parsing', row)
        return 'QB', 37, 17.5

class FootballPlayerSet:
    def __init__(self):
        self.players = []
        self.position_map = {
            'QB': 0,
            'WR': 0,
            'RB': 0,
            'TE': 0,
            'DST': 0,
        }

    def __str__(self):
        return ''.join(map(str, self.players))

    def fork(self, player):
        new = FootballPlayerSet()
        new.players = self.players.copy()
        new.players.append(player)
        return new

    def sum(self):
        total = 0.0
        for player in players:
            total += player.value
        return total

    def get_needed_positions():
        pass

fp = FootballPlayer('asdf')
fp.parse('asdfasdf')


drafts = [FootballPlayerSet()]
for i in range(5):
    prev = drafts[i]
    drafts.append(prev.fork(FootballPlayer('')))

print('HELLO', drafts[2])

