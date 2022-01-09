from os import error
import sqlite3
from etherphire.settings import DATABASES
from poetrysite.models import Poems

def sortByDate():
    return True
'''
poemNames = db['NAME']
tags = db.get_tags

def db_connect(database_name):
        connection = None

        try:
            connection = sqlite3.connect(database_name)

        except error as e:

            print(e)
        
        return connection

def main():
    items = []
    connection = db_connect(db)
    with connection.cursor() as cursor:
        while(cursor.next() is not None):
            items.append(cursor.next())
            cursor = cursor.next()
    return items

'''

'''
def addSpace(fullText:str) -> str:

    while(fullText.find("~") != -1):
        temp = fullText.find("~")
        fullText = fullText[0:temp] + '\n' + fullText[temp+1:len(fullText)]
        print(fullText)

    return fullText
'''
        
'''def filter(keyword):
    for name in poemNames:'''