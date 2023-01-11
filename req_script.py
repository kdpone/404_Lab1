import requests as req

print(req.__version__)

#r = req.get('https://www.google.com/')
#print(r)

raw_site = 'https://raw.githubusercontent.com/kdpone/404_Lab1/master/req_script.py?token=GHSAT0AAAAAAB4X6SKMSM6XVGVNK7TTLOHIY57FVZA'

r = req.get(raw_site)

open('downloaded_raw_code.py', 'wb').write(r.content)

print(r.text)