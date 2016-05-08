from requests import session

payload = {
    'action': 'login',
    'username': 'student',
    'password': 'lab2asd'
}

url = "http://www.mini.pw.edu.pl/~dobrowolskip/lab/asd2lab/l16/results.html"

with session() as s:
    s.post(url, data=payload)
    response = s.get(url)
    print(response.headers)
    print(response.text)
