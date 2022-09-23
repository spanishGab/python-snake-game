from pathlib import Path
from .constants import RESOURCES_DIR

GAME_SCORE_DIR = Path(RESOURCES_DIR, 'game_score')
GAME_SCORE_FILE = GAME_SCORE_DIR.joinpath('best_score.txt')


def create_best_score_file() -> int:
    best_score = 0

    if not GAME_SCORE_DIR.exists():
        GAME_SCORE_DIR.mkdir()

    if GAME_SCORE_FILE.exists():
        with GAME_SCORE_FILE.open(mode='r') as file:
            try:
                best_score = int(file.readline())
            except ValueError:
                pass
    else:
        GAME_SCORE_FILE.touch()

    return best_score


def update_best_score(score: int):
    with GAME_SCORE_FILE.open(mode='w') as file:
        file.write(str(score))
