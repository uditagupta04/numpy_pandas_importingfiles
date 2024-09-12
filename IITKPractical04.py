import numpy
import urllib.request

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataset = numpy.genfromtxt(web_path, delimiter=",")
print("shape of data from url:", dataset.shape)
print("format of data dim=", dataset.ndim)
print(dataset)
print("\n\n\n")


#nan=not a number
#no metadata im numpy