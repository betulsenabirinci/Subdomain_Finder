import urllib3
import requests
import time
urllib3.disable_warnings()

line=[]
data=[line.strip() for line in open('subdomain-enumeration-521.rtf','r')]
file2 = open("200_Response.txt", "w")
file3 = open("300_Response.txt", "w")
file4 = open("400_Response.txt", "w")
file5 = open("500_Response.txt", "w")
file6 = open("ConnectionTimeOut.txt", "w")
for r in data :
    try:
        url1 = 'http://' +r
        response = requests.get(url1, verify=False)
        print(str(url1)+" ---> "+str(response.status_code))
        if str(response.status_code)[0] == '2':
            file2.write(url1+" \n")
        elif str(response.status_code)[0] == '3':
            file3.write(url1+" \n")
        elif str(response.status_code)[0] == '4':
            file4.write(url1+" \n")
        else :
            file5.write(url1+" \n")

    except requests.ConnectionError:
        print(url1+" ---> "+"CONNECTION TIMEOUT ERROR")
        file6.write(url1+" \n")

    try:
        url2 = 'https://' +r

        response = requests.get(url2, verify=False)
        print(str(url2) + " ---> " + str(response.status_code))
        if str(response.status_code)[0] == '2':
            file2.write(url2 + " \n")
        elif str(response.status_code)[0] == '3':
            file3.write(url2 + " \n")
        elif str(response.status_code)[0] == '4':
            file4.write(url2 + " \n")
        else:
            file5.write(url2 + " \n")

    except requests.ConnectionError:
        print(url2 + " ---> " + "CONNECTION TIMEOUT ERROR")
        file6.write(url2 + " \n")
    print()
