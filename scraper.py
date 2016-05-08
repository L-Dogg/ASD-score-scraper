import argparse
import urllib.request

from bs4 import BeautifulSoup

URL = "http://www.mini.pw.edu.pl/~dobrowolskip/lab/asd2lab/l16/results.html"
USERNAME = 'student'
PASSWORD = 'lab2asd'

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'

def parseArguments():
    parser = argparse.ArgumentParser(description='ASD2 Lab Scores')
    parser.add_argument('name', metavar='name', nargs=1, help='Student name')
    parser.add_argument('surname', metavar='surname', nargs=1, help='Student surname')
    return parser.parse_args()

def getPage():
    p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, URL, USERNAME, PASSWORD)

    handler = urllib.request.HTTPBasicAuthHandler(p)
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

    return urllib.request.urlopen(URL).read()

def parsePage(page, args):
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find_all('table')[0]
    student_name = '%s %s' % (args.name[0], args.surname[0])
    print(student_name)
    student_marks = {}
    i = 1
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if cells[0].text.strip() == student_name:
            for cell in cells[1:]:
                if not cell.text.strip() == '':
                    student_marks[i] = float(cell.text.strip())
                    i = i + 1
    return student_marks

def main():
    args = parseArguments()
    page = getPage()
    student_marks = parsePage(page, args)
    print(student_marks)

if __name__ == '__main__':
    main()
