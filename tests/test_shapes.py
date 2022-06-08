import pytest
from ammolite import reset, draw_arrows


def test_draw_arrow_uniform():
    """
    Draw arrows using the same radius for all arrows.
    The radius is taken is example property here,
    to test if uniform values are properly arrayfied.
    """
    reset()
    draw_arrows([(0,0,0), (1,0,1)], [(1,0,0), (1,0,1)], radius=0.1)


def test_draw_arrow_individual():
    """
    Draw arrows using the same radius for all arrows.
    The radius is taken is example property here,
    to test if uniform values are properly arrayfied.
    """
    reset()
    draw_arrows([(0,0,0), (1,0,1)], [(1,0,0), (1,0,1)], radius=[0.1, 0.2])