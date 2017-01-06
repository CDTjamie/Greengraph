
from .map import Map
import geopy
import numpy as np

class Greengraph(object):
    def __init__(self, start, end):
        if type(start) != str or type(end) != str:
            raise TypeError("Start and end point must be strings")
        
        self.start = start
        self.end = end
        self.geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
        
    def geolocate(self, place):
        if type(place) != str:
            raise TypeError("Place name must be of type string")
        
        return self.geocoder.geocode(place, exactly_one=False)[0][1]
    
    def location_sequence(self, start, end, steps):
        if float(steps) != int(float(steps)):
            raise TypeError("No. steps must be an integer")
        if float(steps) <= 0:
            raise ValueError("No. steps must be a positive integer")
        if type(start) != list or type(end) != list:
            raise TypeError("start, end input to location sequence incorrect type")
        if len(start) != 2 or len(end) != 2:
            raise ValueError("start, end input to location sequence must be array of length 2")
        
        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1], end[1], steps)
        return np.vstack([lats, longs]).transpose()
    
    def green_between(self, steps):
        if float(steps) != int(float(steps)):
            raise TypeError("No. steps must be an integer")
        if float(steps) <= 0:
            raise ValueError("No. steps must be a positive integer")
        
        return [Map(*location).count_green() for location in self.location_sequence(self.geolocate(self.start), self.geolocate(self.end), steps)]