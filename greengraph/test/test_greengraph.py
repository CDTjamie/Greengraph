from nose.tools import assert_raises
from greengraph import Greengraph

def test_locations():
    with assert_raises(TypeError) as exception: Greengraph('London', 6)
    with assert_raises(TypeError) as exception: Greengraph(6.3, 'Oxford')
    with assert_raises(TypeError) as exception: Greengraph([2, 'ghf'], 8)

def test_steps_int():
    with assert_raises(TypeError) as exception: Greengraph('London', 'Oxford').green_between(10.2)

def test_steps_pos():
    with assert_raises(ValueError) as exception: Greengraph('London', 'Oxford').green_between(-2)