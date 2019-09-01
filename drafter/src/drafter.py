import parser
from player import (
    FootballPlayer,
    FootballPlayerSet,
)

def get_draft_picks(pick_num: int, num_players: int, rounds: int):
    draft_picks = []
    for i in range(rounds // 2):
        draft_picks.append(2 * num_players * i + pick_num)
        draft_picks.append(2 * num_players * i - pick_num + 1)
    return draft_picks

def compute_drafts(picks, draft_players):
    '''Compute all optimal draft options'''
    drafts = [FootballPlayerSet()]
    for pick in picks:
        next_draft_round = []
        for draft in drafts:
            for position in draft.get_needed_positions():
                for cur in draft_players.query(position, pick):
                    next_draft_round.append(draft.fork(cur))
        drafts = next_draft_round
    return drafts

def sort_drafts(drafts):
    return sorted(drafts)

class DraftPlayers:
    def __init__(self, players):
        self.position_map = {}
        pass

    def query(self, position: str, pick: int):
        return [FootballPlayer()]


if __name__ == '__main__':
    players = parser.parse()
    draft_players = DraftPlayers(players)
    pick_order = get_draft_picks(5, 10, 16)

    drafts = sorted(compute_drafts(pick_order, draft_players))
    print(drafts)
