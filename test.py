
import json
with open('messages.json' , 'r') as f:
    msg = json.load(f)
print(msg)