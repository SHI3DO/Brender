import os
import json
from api.printer import print_

print_('Finding "token.json"...')

if not os.path.exists("token.json"):
    print_('"token.json" not found!')
else:
    print_('"token.json" found!')
    print_('Loading "token.json"')
    token_json = json.loads(open("token.json", "r").read())
    print_('"token.json" loaded!')

    print_("Finding valid data...")
    if not token_json.get("data"):
        print_("No valid data found!")
    else:
        data = token_json.get("data")
        print_("Valid data found!")

        print_(f"Data Author: {token_json.get('author')}")

        print_("Data loaded!")
