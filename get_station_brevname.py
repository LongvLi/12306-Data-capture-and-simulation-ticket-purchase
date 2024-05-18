import json
import requests
from requests.exceptions import RequestException

def getResponse(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
        return None
    except RequestException:
        return None


if __name__ == "__main__":
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
    data = getResponse(url)
    if data is not None:
        dict_data = {}
        text = data.text
        str_split = text.split('@')
        for chars in str_split[1:]:
            station = chars.split('|')
            dict_data[station[1]] = station[2]
        with open("stations.json", 'w', encoding='utf-8') as fp:
            json.dump(dict_data, fp, ensure_ascii=False)