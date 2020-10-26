"""Testing new APIs"""

import json
import sys

import requests

def print_info(language):
    """Translating information"""
    base_url = "https://translate.google.be/?hl=fr"
    resp = requests.get(old_name + new_name)
    try:
        name = json.loads(resp.text)[0]
        languages = name['languages']
        print(f"Languages: {', '.join([lang['name'] for lang in languages])}")
        border_codes = country['borders']
        border_names = []
        for code in language_codes:
            resp = requests.get(code_url + code)
            border_country = json.loads(resp.text)
            border_name = border_country["name"]
            border_names.append(border_name)
        print(f"languages: {', '.join(border_names)}")
    except KeyError:
        print("Unknown words")

if __name__ == "__main__":
    try:
        service = sys.argv[1]
        if service == "coord":
            try:
                address = sys.argv[2]
                print_coord(address)
            except IndexError:
                print("Please enter an address")
        elif service == "info":
            try:
                country_name = sys.argv[2]
                print_info(country_name)
            except IndexError:
                print("Please write something")
 
    except IndexError:
        print("Missing action)
