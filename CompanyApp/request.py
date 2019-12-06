import requests
import json, xmljson
from lxml.html import fromstring, tostring
from  datetime import date, datetime, timedelta



time_today = date.today().strftime('%d.%m.%Y')

time_yesterday = datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y')

url_today = f"https://www.cbar.az/currencies/{time_today}.xml"
url_yesterday = f"https://www.cbar.az/currencies/{time_yesterday}.xml"





def parse_data(url):
    response = requests.get(url)

    bank_mezenne = []
    xml = fromstring(response.content)
    json_data = json.dumps(xmljson.badgerfish.data(xml))

    data = json.loads(json_data)
    # list_data1 = data["valcurs"]["valtype"][0]
    list_data2 = data["valcurs"]["valtype"][1]
    for item in list_data2["valute"]:
        if item["@code"] == 'USD' or item["@code"] == 'EUR' :

            obj = {
                "code": item["@code"],
                "value": item["value"],

            }

            bank_mezenne.append(obj)

    return bank_mezenne

arr = parse_data(url_today)

# code = list(map(lambda x: x['code'], arr))