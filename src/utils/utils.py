from ..constants.constants import TYPE_ERROR_MESSAGE, VALUE_ERROR_MESSAGE

def collision(p1, p2):
    return (p1[0] == p2[0]) and (p1[1] == p2[1])


def is_valid_rgb_color(color: tuple):
    if isinstance(color, tuple):
        for i, elem in enumerate(color):
            if isinstance(elem, int):
                if elem < 0 or elem > 255:
                    return False
            else:
                raise TypeError(TYPE_ERROR_MESSAGE.format(param=f'color[{i}]',
                                                          tp=int, inst=type(elem)))
    else:
        raise TypeError(TYPE_ERROR_MESSAGE.format(param='color', tp=tuple,
                                                      inst=type(color)))
    return True


def are_valid_dimensions(dimensions: tuple, length: int = 2):
    if isinstance(dimensions, (tuple, list)):
        if len(dimensions) == length:
            for elem in dimensions:
                if not isinstance(elem, int):
                    return False
        else:
            raise ValueError(VALUE_ERROR_MESSAGE.format(
                param='dimensions', restr=f"'dimensions' mut have {length} integer elements")
            )
    else:
        raise TypeError(TYPE_ERROR_MESSAGE.format(param='dimensions', tp=(tuple, list),
                                                  inst=type(dimensions)))
    
    return True
