import sys
import requests

"""To Use this tool you first need to create or modify the wordlist as wordlist.txt then Enter python dir_fuzzing.py domain
EX : python dir_fuzzing.py facebook.com"""

words = open("wordlist.txt").read()
words_filter = words.splitlines()

for wordlists in words_filter:
    url = f"https://{sys.argv[1]}/{wordlists}.html"
    try:
        send = requests.get(url)
        if send.status_code !=404:
            print("[+] VALID DIRECTORY : ",url)
    except requests.RequestException:
        pass
