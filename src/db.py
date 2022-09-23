from pathlib import Path
from .constants import RESOURCES_DIR

GAME_SCORE_FILE = Path(RESOURCES_DIR, 'game_score', 'best_score.txt')


def create_best_score_file() -> int:
    best_score = 0
    if GAME_SCORE_FILE.exists():
        with open(GAME_SCORE_FILE, mode='r') as file:
            try:
                best_score = int(file.readline())
            except ValueError:
                pass
    else:
        GAME_SCORE_FILE.touch()

    return best_score


def update_best_score(score: int):
    with open(GAME_SCORE_FILE, mode='w') as file:
        file.write(str(score))
