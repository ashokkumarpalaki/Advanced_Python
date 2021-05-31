import json
import os
import smtplib
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import git
import requests


class GitSecretsAWS():
    def __init__(self):
        self.giturl = 'https://api.github.com'

    def get_repo(self):
        get_repo_url = self.giturl + '/orgs/paxits/repos'
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.request("GET", get_repo_url)
        data = json.loads(response.text)
        for i in data:
            # if 'full_name' in i.keys():
            #     print(i['full_name'], i['html_url'])
            if 'Dummy' in i['full_name']:
                # git.Git(r"/home/ashok/Desktop/Python_II").clone(i['html_url'])
                os.chdir('../../../Dummy')
                os.system('git secrets --install')
                os.system('git secrets --register-aws')
                os.system('git secrets --scan')
                os.system('git secrets --scan > ../../file.txt 2>&1')
                with open('../../file.txt') as file:
                    data = str(file.read()).split('Possible')[0]
                gmail_user = 'ashok27245@gmail.com'
                gmail_pwd = 'AS3hokkuM@r'
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                to = ['ashokkumarpalaki@gmail.com',]#'charlie443abul@gmail.com']
                body = '"' + i['name'] + '" repository Scan results \n ' + data

                message = MIMEMultipart()
                message['From'] = gmail_user
                message['To'] = "".join(to)
                message['Subject'] = 'Git Secrets.'
                message.attach(MIMEText(body, 'plain'))
                text = message.as_string()
                server.sendmail(gmail_user, to, text.encode('utf-8'))
                server.close()


if __name__ == '__main__':
    gitsc = GitSecretsAWS()
    gitsc.get_repo()
