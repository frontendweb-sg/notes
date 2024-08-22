# What is an iterable:

An object capable of returning its members one at a time.

Iterables include all `sequence` types (such as `list`,`str`, and `tuple`) and some `non-sequence` types like (`dict` and `file objects`) and objects of any classes you define with
`__iter__()` method or with a `__getitem__()` method that implements `Sequence` semantics.

Iterable can be used in `for` loop.

`Example:`

```py
items = [1,2,3,4,5] # an iterable list

for item in items:
    print(item)
```
