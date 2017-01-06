
import numpy as np
from io import BytesIO
from matplotlib import image as img
import requests

class Map(object):
    def __init__(self, lat, long, satellite=True, zoom=10, size=(400,400), sensor=False):
        if float(lat) < -90.0 or float(lat) > 90.0:
            raise ValueError("latitude must be between -90 and +90")
        if float(long) <-180.0 or float(long) > 180.0:
            raise ValueError("longitude must be between -180 and +180")
        
        base="http://maps.googleapis.com/maps/api/staticmap?"
        
        params=dict(sensor= str(sensor).lower(), zoom= zoom, size= "x".join(map(str, size)), center= ",".join(map(str, (lat, long) )), style="feature:all|element:labels|visibility:off")
        
        if satellite:
            params["maptype"]="satellite"
         
        self.image = requests.get(base, params=params).content
        self.pixels = img.imread(BytesIO(self.image))
        
    def green(self, threshold):
        if type(threshold) != int and type(threshold) != float:
            raise TypeError("threshold input to green function must be an integer or float")
        if float(threshold) <= 0:
            raise ValueError("threshold must be a positive number")
        
        greener_than_red = self.pixels[:,:,1] > threshold*self.pixels[:,:,0]
        greener_than_blue = self.pixels[:,:,1] > threshold*self.pixels[:,:,2]
        green = np.logical_and(greener_than_red, greener_than_blue)
        return green
    
    def count_green(self, threshold = 1.1):
        return np.sum(self.green(threshold))
    
    def show_green(data, threshold = 1.1):
        green = self.green(threshold)
        out = green[:,:,np.newaxis]*array([0,1,0])[np.newaxis,np.newaxis,:]
        buffer = BytesIO()
        result = img.imsave(buffer, out, format='png')
        return buffer.getvalue()