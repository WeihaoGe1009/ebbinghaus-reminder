import argparse
import json
import sqlite3
from datetime import date
from modules.review_logic import add_item_to_db
from modules.text_parser import parse_items_from_text_file

parser = argparse.ArgumentParser(description="Add items from json file")
parser.add_argument("json_file", help="the json file contains category and path to the content file")
args = parser.parse_args()

with open(args.json_file, encoding="utf-8") as f:
    data = json.load(f)

category = data.get("category")
content_file = data.get("file")

if not category or not content_file:
    print("JSON must contain 'category' and 'file'")
    exit(1)

items = parse_items_from_text_file(content_file)
if not items:
    print("empty content file")
    exit(1)

created_date = date.today()
with sqlite3.connect("review_items.db") as conn:
    for content in items:
        item_id = add_item_to_db(conn, content, category, created_date)
        print(f"item added ID={item_id}")

