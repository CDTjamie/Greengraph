from nose.tools import assert_raises
from greengraph import Greengraph

def test_location_sequence():
    with assert_raises(TypeError) as exception: Greengraph('London', 'Oxford').location_sequence([50.0, 0.0], [52.0, -1.0], 10.2)
    with assert_raises(ValueError) as exception: Greengraph('London', 'Oxford').location_sequence([50.0, 0.0], [52.0, -1.0], -2)
    with assert_raises(TypeError) as exception: Greengraph('London', 'Oxford').location_sequence('London', [52.0, -1.0], 20)
    with assert_raises(TypeError) as exception: Greengraph('London', 'Oxford').location_sequence([50.0, 0.0], 7.2, 20)
    with assert_raises(ValueError) as exception: Greengraph('London', 'Oxford').location_sequence([50.0, 0.0, 3.7], [52.0, -1.0], 20)
    with assert_raises(ValueError) as exception: Greengraph('London', 'Oxford').location_sequence([50.0, 0.0], [52.0, -1.0, 3.7], 20)

def test_geolocate():
    with assert_raises(TypeError) as exception: Greengraph('London', 'Oxford').geolocate(3.14)

def test_locations():
    with assert_raises(TypeError) as exception: Greengraph('London', 6)
    with assert_raises(TypeError) as exception: Greengraph(6.3, 'Oxford')
    with assert_raises(TypeError) as exception: Greengraph([2, 'ghf'], 8)

def test_green_bewteen():
    with assert_raises(TypeError) as exception: Greengraph('London', 'Oxford').green_between(10.2)
    with assert_raises(ValueError) as exception: Greengraph('London', 'Oxford').green_between(-2)