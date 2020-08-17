#!/usr/bin/env python3
import PIL.Image
import pandas
import numpy as np
image=PIL.Image.open("myfile.jpg")
print(image.size)
print(image.format)

visitors = [1235, 6424, 9345, 8464, 2345]
errors = [23, 45, 33, 45, 76]
df = pandas.DataFrame( {"visitors": visitors, "errors": errors}, index=["Mon", "Tues", "Wed", "Thu", "Fri"])
print(df)
def numpyArray():
    x = np.array([[1,2,3], [4,5,6]], np.int32)
    y = np.array([[3, 6, 2], [9, 12, 8]], np.int32)
    return x*y
print(numpyArray())
