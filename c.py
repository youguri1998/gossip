import requests, sqlite3


DB_PATH = 'upbit_notice.db'
upbit_notice = "https://api-manager.upbit.com/api/v1/announcements?os=web&page=1&per_page=10&category=all"



a = requests.get(upbit_notice).json()



if a['success']== True:
    for notice in a['data']['notices']:
    
        if notice['category'] == '거래' and "신규" in notice['title']:
            print(notice['title'] +'\n'+ notice['listed_at'])
            print(f'https://upbit.com/service_center/notice?id={notice["id"]} \n\n')
