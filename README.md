# treehaus

Pure python3 based file-based datastore.  Current status is version 0.1 / alpha.

*  zero dependencies
*  supports multiple key-value indexes
*  commit and rollback semantics
*  iterate over (key,value) pairs in key order
*  iterate over previously assigned values of a key
*  open and browse store at previous versions
*  append only file-writes minimises risk of datastore corruption

Installation from pypi using

`pip3 install treehaus`

API Documentation available at [https://niallmcc.github.io/treehaus/](https://niallmcc.github.io/treehaus/)

Simple Example:

```
from treehaus import TreeHaus

TreeHaus.create("/tmp/test.th")
with TreeHaus.open("/tmp/test.th") as th:
    i = th.getIndex("my index")
    i["key1"] = "some value"
    i["key2"] = { "meta1":"meta2" }
```
