# contains special functions for reading and writing to tinydb (maybe)
from tinydb import TinyDB, Query
from tdlist import tdlist

tdb = TinyDB('tdb.json')
lists = tdb.table("tdlists")

def save_lists():
    table.upsert(tdlist.to_dict_of_dicts(), db.name == tdlist.name)

def showlists():
    print(tdb.all)
