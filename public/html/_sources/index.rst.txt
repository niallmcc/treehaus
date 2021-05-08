.. TreeHaus documentation

TreeHaus
========

TreeHaus is a lightweight zero-dependency, pure python3 library for persistent tree-based indexes.

:class:`treehaus.TreeHaus` can be used to create and open files containing a set of dict-like TreeHaus treebased indices represented by :class:`treehaus.Index` instances.  

-----------
Limitations
-----------

TreeHaus aims to provide tree-based storage with simplicity and robustness.  Look elsewhere if high performance is a high priority.

Calls to an individual store instance and associated index instances should not be invoked concurrently from multiple threads.

Multiple TreeHaus stores can be opened concurrently on the same file, but only one instance should be opened for writing.  

When a TreeHaus store is opened it will see only the latest committed changes.

TreeHaus uses a python3 serialization protocol.  It will not be possible to read a TreeHaus file using other programming languages (including earlier versions of python).

Keys and values may be of any type supported by the python3 pickle protocol.  However keys within each index should use the same type and be comparable with the python > and < operators. 

-------
Example
-------

.. literalinclude:: ../examples/simple.py
    :language: python

TreeHaus is a data store consisting of indexes persisted to a file.  Use `TreeHaus.create` to create a store and then `TreeHaus.create` to open and return a `TreeHaus` instance 

.. automethod:: treehaus.TreeHaus.create
.. automethod:: treehaus.TreeHaus.open

TreeHaus methods:

.. automethod:: treehaus.TreeHaus.getIndex
.. automethod:: treehaus.TreeHaus.getIndices
.. automethod:: treehaus.TreeHaus.removeIndex
.. automethod:: treehaus.TreeHaus.getUpdates
.. automethod:: treehaus.TreeHaus.commit
.. automethod:: treehaus.TreeHaus.rollback
.. automethod:: treehaus.TreeHaus.close
.. automethod:: treehaus.TreeHaus.getVersion


=====
Index
=====

a TreeHaus Index is a dict-like container within a TreeHaus store and returned from a call to `treehaus.TreeHaus.getIndex`

Methods to retrieve information:

.. automethod:: treehaus.Index.__getitem__
.. automethod:: treehaus.Index.__contains__
.. automethod:: treehaus.Index.get
.. automethod:: treehaus.Index.traverse
.. automethod:: treehaus.Index.rtraverse
.. automethod:: treehaus.Index.history

Methods to update the index:

.. automethod:: treehaus.Index.__setitem__
.. automethod:: treehaus.Index.__delitem__
.. automethod:: treehaus.Index.pop
.. automethod:: treehaus.Index.update
.. automethod:: treehaus.Index.clear


