#!/usr/bin/python3
import PIL.Image
import pandas
image=PIL.Image.open("myfile.jpg")
print(image.size)
print(image.format)

visitors = [1235, 6424, 9345, 8464, 2345]
errors = [23, 45, 33, 45, 76]
df = pandas.DataFrame( {"visitors": visitors, "errors": errors}, index=["Mon", "Tues", "Wed", "Thu", "Fri"])
print(df)
