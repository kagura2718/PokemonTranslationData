#!/usr/bin/env python3

import sys
import json
import datetime
import re

from bs4 import BeautifulSoup

VERSION = '0.0.2'

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
        num = canonicalizeNumberNode(row[0])
        if num == None:
            return None
    
        ja = canonicalizeNameNode(row[1])
        if (re.search("Type:.*Null", row[2].getText())):
            en = "Type:Null"
            it = "Tipo Zero"
            es = "Código Cero"
        else:
            en = canonicalizeNameNode(row[2])
            it = None
            es = None
        de = canonicalizeNameNode(row[3])
        fr = canonicalizeNameNode(row[4])
        kr = canonicalizeNameNode(row[5])
        zh_ch = canonicalizeNameNode(row[6])
        zh_tw = canonicalizeNameNode(row[7])
    
        obj = {
            "number": num,
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

        if (it):
            obj['it'] = it

        if (es):
            obj['es'] = es

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

soup = readSourceHtml("pokemon.html")
db = buildDatabase(soup)
printDatabase(db)

