import argparse
import json
import requests


# ██╗   ██╗ ██████╗██╗  ██╗     █████╗ ██████╗ ██╗
# ██║   ██║██╔════╝██║  ██║    ██╔══██╗██╔══██╗██║
# ██║   ██║██║     ███████║    ███████║██████╔╝██║
# ╚██╗ ██╔╝██║     ╚════██║    ██╔══██║██╔═══╝ ██║
#  ╚████╔╝ ╚██████╗     ██║    ██║  ██║██║     ██║
#   ╚═══╝   ╚═════╝     ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝


"""

curl -k --compressed --location --request POST "https://ip:2080/api/Login" --header "Authorization: Basic aXNsYW1AVEUjMjAyNA==" --data ''
curl -k --compressed  "https://ip:2080/api/ims/Geo/GetGeoFeatureSets/TB" -H "Authorization: Bearer ********-****-****-****-f6e590******"
curl -k --compressed  "https://ip:2080/api/ims/Geo/GetGeoFeatureSets/DDFODF" -H "Authorization: Bearer ********-****-****-****-f6e590******"

username = "***"
password = "****"

"""

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip')
parser.add_argument('-t', '--token')
args = parser.parse_args()
ip = args.ip
token = args.token
print(ip)
print(token)


url_LOGIN = "https://ip:2080/api/Login"
url_ODF = "https://ip:2080/api/ims/Geo/GetGeoFeatureSets/DDFODF"
url_TB = "https://ip:2080/api/ims/Geo/GetGeoFeatureSets/TB"
header = {"Authorization": "Bearer "+token}


def getAPIdata(url):
    r = requests.get(url, data='', headers=header, verify=False)
    print(r.status_code)
    if r.status_code == 200:
        print("Success") 
    else:
        print("There was an error, check connection")

    print(url + "Connected")
    print(r.text)
    return r.content


JSON_TB = getAPIdata(url_TB)

with open("JSON_TB.json", "w") as outfile_TB:
    json.dump(JSON_TB, outfile_TB)
    outfile_TB.close()


JSON_ODF = getAPIdata(url_ODF)

with open("JSON_ODF.json", "w") as outfile_ODF:
    json.dump(JSON_ODF, outfile_ODF)
    outfile_ODF.close()


JSON_TB_G = json.loads(JSON_TB)
JSON_ODF_G = json.loads(JSON_ODF)


# ███████ ███    ██ ██████       ██████  ███████      █████  ██████  ██ 
# ██      ████   ██ ██   ██     ██    ██ ██          ██   ██ ██   ██ ██ 
# █████   ██ ██  ██ ██   ██     ██    ██ █████       ███████ ██████  ██ 
# ██      ██  ██ ██ ██   ██     ██    ██ ██          ██   ██ ██      ██ 
# ███████ ██   ████ ██████       ██████  ██          ██   ██ ██      ██ 
