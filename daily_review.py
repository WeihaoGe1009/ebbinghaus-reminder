import sqlite3
from modules.review_today import get_today_reviews_by_category

def open_review_in_textedit(reviews_by_cat: dict):
    import subprocess
    import tempfile

    if not reviews_by_cat:
        return

    lines = []
    for cat, items in reviews_by_cat.items():
        lines.append(f"【{cat}】")
        lines.extend(items)
        lines.append("")  # Blank line between categories

    content = "\n".join(lines)

    # Write to temporary text file
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".txt") as f:
        f.write(content)
        temp_path = f.name

    # Open file in TextEdit
    subprocess.run(["open", "-a", "TextEdit", temp_path])

# --- Main execution ---
with sqlite3.connect("review_items.db") as conn:
    reviews = get_today_reviews_by_category(conn)

open_review_in_textedit(reviews)

