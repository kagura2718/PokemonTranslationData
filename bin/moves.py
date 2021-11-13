#!/usr/bin/env python3

import sys
import json
import datetime
import re

from bs4 import BeautifulSoup

VERSION = '0.0.0'

def canonicalizeNumberNode(n):
    num = n.getText().strip()
    if num == '':
        return None

    return int(num)

def canonicalizeName(s):
    return s.strip()

def canonicalizeNameNode(n):
    return canonicalizeName(n.getText())

def readSourceHtml(file):
    with open(file) as f:
        s = f.read()
        return BeautifulSoup(s, "html.parser")

def stderr(text):
    print(text, file=sys.stderr)

def buildDatabase(soup):
    def buildItem(row):
        ja = canonicalizeNameNode(row[0])
        en = canonicalizeNameNode(row[1])
        de = canonicalizeNameNode(row[2])
        fr = canonicalizeNameNode(row[3])
        kr = canonicalizeNameNode(row[4])
        zh_ch = canonicalizeNameNode(row[5])
        zh_tw = canonicalizeNameNode(row[6])
    
        obj = {
            "i18n": {
                "ja": ja,
                "en": en,
                "de": de,
                "fr": fr,
                "kr": kr,
                "zh_ch": zh_ch,
                "zh_tw": zh_tw,
            },
        };

        return obj;

    array = []

    for tr in soup.find("div", {"id": "mw-content-text"}).findAll("tr"):
        row = tr.findAll("td")
        if len(row) >= 8:
            item = buildItem(row);
            if item == None:
                stderr(tr)
                continue
            array.append(item)
        else:
            stderr(tr)

    return {
	"generatedAt": datetime.datetime.utcnow().isoformat(),
        "version": VERSION,
        "data": array,
    }

def printDatabase(db):
    print(json.dumps(db))

soup = readSourceHtml("moves.html")
db = buildDatabase(soup)
printDatabase(db)

