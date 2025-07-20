from datetime import date, timedelta
from typing import List

def load_review_intervals(path="./review_days.txt") -> List[int]:
    try:
        with open(path, encoding="utf-8") as f:
            return sorted({int(line.strip()) for line in f if line.strip().isdigit()})
    except:
        return [0, 1, 2, 4, 7, 15, 30]


def add_item_to_db(conn, content: str, category: str, created_date: date = None):
    if created_date is None:
        created_date = date.today()

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO memory_items (content, created_at, category) VALUES (?, ?, ?)",
        (content, created_date, category)
    )
    item_id = cur.lastrowid

    for d in load_review_intervals():
        review_date = created_date + timedelta(days=d)
        cur.execute(
            "INSERT INTO review_schedule (item_id, review_date) VALUES (?, ?)",
            (item_id, review_date)
        )

    conn.commit()
    return item_id

