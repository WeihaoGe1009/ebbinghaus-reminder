# Ebbinghaus Reminder
This is a small code that deposit items to memorize into database, and remind me to review them based on Ebbinghaus Forgetting Curve.

## Function
- add item and generate review calendar
- automatically pop up daily review content in TextEdit

## usage

### 1. initialize database
```bash
python init_db.py 
```
### 2. add items
- create content in a .txt file (e.g. `content.txt`)
- create a json file like the example, or modify your example 
- run python command
```bash
python add_item.py json_example.json
``` 

### 3. set up system 
i'm using crontab on Mac to set up daily reminder

run
```bash
crontab -e
```
then add
```bash
0 8 * * * PATH_TO_Python3 /full/path/to/daily_review.py
```
 
