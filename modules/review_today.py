from datetime import date
from collections import defaultdict

def get_today_reviews_by_category(conn):
    cur = conn.cursor()
    today = date.today()
    cur.execute("""
        SELECT m.category, m.content
        FROM review_schedule r
        JOIN memory_items m ON r.item_id = m.id
        WHERE r.review_date = ?
        ORDER BY m.category
    """, (today,))
    
    reviews = defaultdict(list)
    for category, content in cur.fetchall():
        reviews[category].append(content)
    return reviews

