from nose.tools import assert_raises, assert_equal
from greengraph.map import Map
import yaml
import os

def test_greenness():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            name = fixture.pop('name')
            lat = fixture.pop('lat')
            long = fixture.pop('long')
            greenness = fixture.pop('greenness')
            assert_equal(Map(lat, long).count_green(), greenness)

def test_green():
    with assert_raises(TypeError) as exception: Map(50.0, 0.0).green('gdb')
    with assert_raises(ValueError) as exception: Map(50.0, 0.0).green(-3)
        
def test_Map():
    with assert_raises(TypeError) as exception: Map(50.0, 3)
    with assert_raises(TypeError) as exception: Map([50.0, 0.0], 0.0)
    with assert_raises(ValueError) as exception: Map(360.0, 0.0)
    with assert_raises(ValueError) as exception: Map(50.0, 360.0)