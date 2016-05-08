import urllib.request

url = "http://www.mini.pw.edu.pl/~dobrowolskip/lab/asd2lab/l16/results.html"
username = 'student'
password = 'lab2asd'
p = urllib.request.HTTPPasswordMgrWithDefaultRealm()

p.add_password(None, url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)

page = urllib.request.urlopen(url).read()
