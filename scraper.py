import urllib.request

from bs4 import BeautifulSoup

URL = "http://www.mini.pw.edu.pl/~dobrowolskip/lab/asd2lab/l16/results.html"
USERNAME = 'student'
PASSWORD = 'lab2asd'

p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, URL, USERNAME, PASSWORD)

handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)

page = urllib.request.urlopen(URL).read()

soup = BeautifulSoup(page, 'html.parser')
table = soup.find_all('table')[0]
student_name = u'Anonymous'
with open('parsed', 'w') as f:
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        print(cells[0].text)
        if(cells[0].text.strip() == student_name):
            for cell in cells[1:]:
                f.write(cell.text)
            f.write('\n')
f.close()
