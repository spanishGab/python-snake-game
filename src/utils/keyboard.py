from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_KP8, K_KP2, K_KP4, K_KP6, K_e, K_d, K_s,
    K_f
)


def should_go_up(event_key: int):
    return event_key == K_UP or event_key == K_KP8 or event_key == K_e


def should_go_down(event_key: int):
    return event_key == K_DOWN or event_key == K_KP2 or event_key == K_d


def should_go_left(event_key: int):
    return event_key == K_LEFT or event_key == K_KP4 or event_key == K_s


def should_go_right(event_key: int):
    return event_key == K_RIGHT or event_key == K_KP6 or event_key == K_f
