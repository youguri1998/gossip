import requests, sqlite3, telepot, os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("my_token")
channel_id = os.getenv("me")
bot = telepot.Bot(bot_token)

DB_PATH = 'upbit_notice.db'
upbit_notice = "https://api-manager.upbit.com/api/v1/announcements?os=web&page=1&per_page=10&category=all"



def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS seen_notices (
            notice_id INTEGER PRIMARY KEY,
            listed_at TEXT,
            title TEXT,
            category TEXT
        )
    """)
    conn.commit()
    return conn

def insert_if_new(conn, n) -> bool:
    """
    새 공지면 True (insert 성공)
    이미 본 공지면 False (PRIMARY KEY 충돌)
    """
    try:
        conn.execute(
            "INSERT INTO seen_notices (notice_id, listed_at, title, category) VALUES (?, ?, ?, ?)",
            (n["id"], n.get("listed_at"), n.get("title"), n.get("category"))
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False



def main():
    conn = init_db()

    data = requests.get(upbit_notice).json()
    if not data.get("success"):
        bot.sendMessage(channel_id, f"API 실패: {data}")
        return

    for notice in data['data']['notices']:

        title = notice.get("title", "")
        category = notice.get("category", "")

        # ✅ 신규 거래지원만
        if notice['category'] == "거래" and "신규" in notice['title']:
            if insert_if_new(conn, notice):
                bot.sendMessage(channel_id, f"<a href='https://upbit.com/service_center/notice?id={notice['id']}'>{notice['title']}</a>\n{notice['listed_at'].split('+')[0]}", parse_mode='HTML')
            else:
                # 이미 봤던 공지면 조용히 패스
                pass

if __name__ == "__main__":
    main()







