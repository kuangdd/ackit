#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2022-02-20
"""# ackit

ackit(aho-corasick kit) is a simple and pure python package and its method like pyahocorasick.

pyahocorasick is a fast and memory efficient library for exact or approximate multi-pattern string search meaning that you can find multiple key strings occurrences at once in some input text. The strings “index” can be built ahead of time and saved (as a pickle) to disk to re re-sed later. The library provides an ahocorasick Python module that you can use as a plain dict-like Trie or convert a Trie to an automaton for efficient Aho-Corasick search.

## Install

```
pip install ackit
```
"""
__version__ = '0.1.2'

from .core import Automaton

if __name__ == "__main__":
    print(__file__)
