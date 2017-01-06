from nose.tools import assert_raises
from greengraph import Greengraph

def test_steps_int():
    with assert_raises(TypeError) as exception: Greengraph('London', 'Oxford').green_between(10.2)

def test_steps_pos():
    with assert_raises(ValueError) as exception: Greengraph('London', 'Oxford').green_between(-2)