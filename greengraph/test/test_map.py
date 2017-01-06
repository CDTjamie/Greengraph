from nose.tools import assert_raises
from greengraph.map import Map

def test_green():
    with assert_raises(TypeError) as exception: Map(50.0, 0.0).green('gdb')
    with assert_raises(ValueError) as exception: Map(50.0, 0.0).green(-3)
        
def test_Map():
    with assert_raises(TypeError) as exception: Map(50.0, 3)
    with assert_raises(TypeError) as exception: Map([50.0, 0.0], 0.0)
    with assert_raises(ValueError) as exception: Map(360.0, 0.0)
    with assert_raises(ValueError) as exception: Map(50.0, 360.0)