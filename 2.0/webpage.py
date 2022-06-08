import urllib.request


def download():
    url = 'https://www.embibe.com/exams/probability-formula/'

    response = urllib.request.urlopen(url)
    webContent = response.read()

    f = open('prob.html', 'w')
    f.write(str(webContent))
    f.close()


if __name__ == '__main__':
    download()
