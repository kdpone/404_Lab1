import requests as req

print(req.__version__)

r = req.get('https://www.google.com/')
print(r)