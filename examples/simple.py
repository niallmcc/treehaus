
import os.path
from treehaus import TreeHaus

path = "simple.th"

if os.path.exists(path):
    os.unlink(path)

TreeHaus.create(path)

with TreeHaus.open(path) as th1:
    books = th1["books"]
    books["9780140449136"] = { "title": "Crime and Punishment", "author":"Fyodor Mikhailovich Dostoyevsky" }
    books["9781853260629"] = { "title":"War and Peace", "author":"Leo Tolstoy" }

with TreeHaus.open(path,readOnly=True) as th2:
    books = th2["books"]
    for (k,v) in books:
        print(str(k) + " -> " + str(v))

    # prints
    # 9780140449136 -> {'title': 'Crime and Punishment', 'author': 'Fyodor Mikhailovich Dostoyevsky'}
    # 9781853260629 -> {'title': 'War and Peace', 'author': 'Leo Tolstoy'}