# coding: utf-8
l = ["București", "Cluj", "Timișoara", "Iași", "Constanța"]
print(*l)
print(*l, sep=' || ')
print("elem 1", "elem 2")
print("elem 1", "elem 2", sep='   !   ')
print("elem 1", "elem 2", sep='   |   ')
print(*l, sep='   |   ')
print(*range(10), sep='   |   ')
print(*"mă, ce-i asta?", sep='   |   ')
print(*l, sep='   |   ')
print("București", "Cluj", "Timișoara", "Iași", "Constanța", sep='   |   ')
print(*l, sep='   |   ', end="\n")
print(*l, sep='   |   ', end="  «««\n")
d = {}
d = {
  sep: '   |   ',
  end: "  «««\n"
}
d = {
  'sep': '   |   ',
  'end': "  «««\n"
}
print(*l, **d) # positional argument unpacking from any iterable; keyword argument unpacking from dictionary.
help(print)
help("".format)
def func(arg1, arg2, kwarg1="1 default", kwarg2="2 default"):
    for el in 'arg1', 'arg2', 'kwarg1', 'kwarg2':
        print(el, )
locals()
type(locals())
{ k:v for k, v in locals().items() if not k.startswith('_') }
{ k:v for k, v in locals().items() if not k.startswith('_') and k not in ('In', 'Out') }
def func(arg1, arg2, kwarg1="1 default", kwarg2="2 default"):
    for el in 'arg1', 'arg2', 'kwarg1', 'kwarg2':
        locals = locals()
        print(el, locals[el], sep=" :: ")
func()
func("aa", "bb")
locals
locals = {}
def func(arg1, arg2, kwarg1="1 default", kwarg2="2 default"):
    for el in 'arg1', 'arg2', 'kwarg1', 'kwarg2':
        _locs = locals()
        print(el, _locs[el], sep=" :: ")
func("aa", "bb")
locals
print = "wow! miau!"
__builtins__
builtins
from builtins import print, locals
print = "wow! miau!"
builtins = "ceva"
from builtins import *
__builtins__.print
__builtins__.locals
__builtins__.locals is locals
__builtins__.print is print
def func(arg1, arg2, kwarg1="1 default", kwarg2="2 default"):
    for el in 'arg1', 'arg2', 'kwarg1', 'kwarg2':
        _locs = locals()
        print(el, _locs[el], sep=" :: ")
func("aa", "bb")
def func(arg1, arg2, kwarg1="1 default", kwarg2="2 default"):
    _locs = locals()
    for k, v in _locs:
        print(k, v, sep=" :: ")
func("aa", "bb")
def func(arg1, arg2, kwarg1="1 default", kwarg2="2 default"):
    _locs = locals()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
func("aa", "bb")
def func(arg1, arg2, kwarg1="1 default", kwarg2="2 default"):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
get_ipython().run_line_magic('pinfo', 'locals')
def func(arg1, arg2, kwarg1="1 default", kwarg2="2 default"):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
func("aa", "bb")
def func(arg1, arg2, kwarg1="one default", kwarg2="two default"):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
func("aa", "bb")
func("aa", "bb", "cc")
def func(arg1, arg2, *, kwarg1="one default", kwarg2="two default"):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
func("aa", "bb", "cc")
func("aa", "bb", kwarg1="cc")
def func(arg1, arg2, kwarg1="one default", kwarg2="two default"):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
func("aa", "bb")
func("aa", "bb", "cc")
func("aa", "bb", "cc", "dd")
func("aa", "bb", "cc", kwarg1="dd")
func(kwarg2="aa", arg2="bb", arg1="cc", kwarg1="dd")
def func(arg1, arg2, kwarg1="one default", kwarg2="two default"):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
func(arg2="bb", arg1="cc")  
# positional arguments, keyword arguments
# și la definiție, și la chemare
func("aa", "bb", kwarg1="ultimul", kwarg1="penultimul")
get_ipython().run_line_magic('pinfo', 'sorted')
sorted([1, 2, 3], str)
sorted([1, 2, 3], key=str)
func("aa", "bb", kwarg1="ultimul", kwarg1="penultimul")
func("aa", "bb", kwarg1="ultimul", kwarg2="penultimul")
get_ipython().run_line_magic('pinfo', 'func')
get_ipython().run_line_magic('pinfo', 'print')
def func(arg1, arg2, kwarg1="one default", kwarg2="two default"):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
def func(arg1, arg2, *args, kwarg1="one default", kwarg2="two default"):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
func("aa", "bb", kwarg1="ultimul", kwarg2="penultimul")
func("aa", "bb", "cc")
func("aa", "bb", "cc", "dd")
def func(arg1, arg2, *args, kwarg1="one default", kwarg2="two default", **kwargs):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
func("aa", "bb", "cc", "dd")
func("aa", "bb", "cc", "dd", de_la_mine="o valoare", de_la_tine="altă valoare")
print(*l, sep="...", end="....\n") # positional argument unpacking from any iterable; keyword argument unpacking from dictionary.
"".format(k1="my val", k2=55)
"{k1}, {k2}".format(k1="my val", k2=55)
l.append #<-- 
class MyLst(list):
    pass
def func(arg1, arg2, *args, kwarg1="one default", kwarg2="two default", **kwargs):
    _locs = locals().copy()
    for k, v in _locs.items():
        print(k, v, sep=" :: ")
l = ["București", "Cluj", "Timișoara", "Iași", "Constanța"]
d = {
    "stuff 1": "this is stuff",
    "stuff 2": "this is more stuff",
    "kwarg1": "this is kwarg stuff"
}
func(*l, **d) 
