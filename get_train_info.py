import json

import requests

def getTrainInfo(from_station, to_station, date):
    # 导入信息
    with open("stations.json", mode='r', encoding='utf-8') as f:
        compare_station_data = json.load(f)

    # 转化为简称
    jc_from_station = compare_station_data[from_station]
    jc_to_station = compare_station_data[to_station]

    # url 与头文件
    url = f"https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={jc_from_station}&leftTicketDTO.to_station={jc_to_station}&purpose_codes=ADULT"

    header = {
        'Cookie' : '_uab_collina=171595714853392819893243; JSESSIONID=9D8AF64B4958ECE8E1724531A2234E3C; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=585629962.64545.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_fromDate=2024-05-18; _jc_save_toDate=2024-05-17; _jc_save_wfdc_flag=dc',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    # 接受消息并整理
    response = requests.get(url, headers=header)

    for index in response.json()['data']['result']:
        solve_index = index.split('|')
        dict = {
            '车次' : solve_index[3],
            '出发': solve_index[8],
            '到达': solve_index[9],
            '耗时': solve_index[10],
            '特等座': solve_index[32],
            '一等座': solve_index[31],
            '二等座': solve_index[30],

        }

    return dict