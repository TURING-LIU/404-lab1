import requests

print(requests.__version__)

google =requests.get("https://www.google.com")

print (google)

var=requests.get("https://raw.githubusercontent.com/TURING-LIU/404-lab1/master/404lab1.py")
print(var.content)