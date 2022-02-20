# ackit

ackit(aho-corasick kit) is a simple and pure python package and its method like pyahocorasick.

pyahocorasick is a fast and memory efficient library for exact or approximate multi-pattern string search meaning that you can find multiple key strings occurrences at once in some input text. The strings “index” can be built ahead of time and saved (as a pickle) to disk to re re-sed later. The library provides an ahocorasick Python module that you can use as a plain dict-like Trie or convert a Trie to an automaton for efficient Aho-Corasick search.

## Install

```
pip install ackit
```

## Version
v0.1.0

## API Reference
```
Automaton(value_type=ahocorasick.STORE_ANY, [key_type])
Create a new empty Automaton. Both value_type and key_type are optional.

value_type is one of these constants:

ahocorasick.STORE_ANY [default] : The associated value can be any Python object.
ahocorasick.STORE_LENGTH : The length of an added string key is automatically used as the associated value stored in the trie for that key.
ahocorasick.STORE_INTS : The associated value must be a 32-bit integer.
key_type defines the type of data that can be stored in an automaton; it is one of these constants and defines type of data might be stored:

ahocorasick.KEY_STRING [default] : string
ahocorasick.KEY_SEQUENCE : sequences of integers; The size of integer depends the version and platform Python, but for versions of Python >= 3.3, it is guaranteed to be 32-bits.
Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A
<ahocorasick.Automaton object at 0x7f1da1bdf7f0>
>>> B = ahocorasick.Automaton(ahocorasick.STORE_ANY)
>>> B
<ahocorasick.Automaton object at 0x7f1da1bdf6c0>
>>> C = ahocorasick.Automaton(ahocorasick.STORE_INTS, ahocorasick.KEY_STRING)
>>> C
<ahocorasick.Automaton object at 0x7f1da1527f10>
add_word(key, [value]) -> boolean
Add a key string to the dict-like trie and associate this key with a value. value is optional or mandatory depending how the Automaton instance was created. Return True if the word key is inserted and did not exists in the trie or False otherwise. The value associated with an existing word is replaced.

The value is either mandatory or optional:

If the Automaton was created without argument (the default) as Automaton() or with Automaton(ahocorasik.STORE_ANY) then the value is required and can be any Python object.
If the Automaton was created with Automaton(ahocorasik.STORE_INTS) then the value is optional. If provided it must be an integer, otherwise it defaults to len(automaton) which is therefore the order index in which keys are added to the trie.
If the Automaton was created with Automaton(ahocorasik.STORE_LENGTH) then associating a value is not allowed - len(word) is saved automatically as a value instead.
Calling add_word() invalidates all iterators only if the new key did not exist in the trie so far (i.e. the method returned True).

Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("pyahocorasick")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: A value object is required as second argument.
>>> A.add_word("pyahocorasick", (42, 'text'))
True
>>> A.get("pyhocorasick")
(42, 'text')
>>> A.add_word("pyahocorasick", 12)
False
>>> A.get("pyhocorasick")
12
>>> import ahocorasick
>>> B = ahocorasick.Automaton(ahocorasick.STORE_INTS)
>>> B.add_word("cat")
True
>>> B.get()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> B.get("cat")
1
>>> B.add_word("dog")
True
>>> B.get("dog")
2
>>> B.add_word("tree", 42)
True
>>> B.get("tree")
42
>>> B.add_word("cat", 43)
False
>>> B.get("cat")
43
exists(key) -> boolean
Return True if the key is present in the trie. Same as using the ‘in’ keyword.

Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("cat", 1)
True
>>> A.exists("cat")
True
>>> A.exists("dog")
False
>>> 'elephant' in A
False
>>> 'cat' in A
True
get(key[, default])
Return the value associated with the key string.

Raise a KeyError exception if the key is not in the trie and no default is provided.

Return the optional default value if provided and the key is not in the trie.

Example
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("cat", 42)
True
>>> A.get("cat")
42
>>> A.get("dog")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError
>>> A.get("dog", "good dog")
'good dog'
longest_prefix(string) => integer
Return the length of the longest prefix of string that exists in the trie.

Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("he", True)
True
>>> A.add_word("her", True)
True
>>> A.add_word("hers", True)
True
>>> A.longest_prefix("she")
0
>>> A.longest_prefix("herself")
4
match(key) -> bool
Return True if there is a prefix (or key) equal to key present in the trie.

For example if the key ‘example’ has been added to the trie, then calls to match(‘e’), match(‘ex’), …, match(‘exampl’) or match(‘example’) all return True. But exists() is True only when calling exists(‘example’).

Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("example", True)
True
>>> A.match("e")
True
>>> A.match("ex")
True
>>> A.match("exa")
True
>>> A.match("exam")
True
>>> A.match("examp")
True
>>> A.match("exampl")
True
>>> A.match("example")
True
>>> A.match("examples")
False
>>> A.match("python")
False
len() -> integer
Return the number of distinct keys added to the trie.

Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> len(A)
0
>>> A.add_word("python", 1)
True
>>> len(A)
1
>>> A.add_word("elephant", True)
True
>>> len(A)
2
remove_word(word) -> bool
Remove given word from a trie. Return True if words was found, False otherwise.

Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("cat", 1)
True
>>> A.add_word("dog", 2)
True
>>> A.remove_word("cat")
True
>>> A.remove_word("cat")
False
>>> A.remove_word("dog")
True
>>> A.remove_word("dog")
False
>>>
pop(word)
Remove given word from a trie and return associated values. Raise a KeyError if the word was not found.

Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("cat", 1)
True
>>> A.add_word("dog", 2)
True
>>> A.pop("elephant")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError
>>> A.pop("cat")
1
>>> A.pop("dog")
2
>>> A.pop("cat")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError
clear()
Remove all keys from the trie. This method invalidates all iterators.

Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("cat", 1)
True
>>> A.add_word("dog", 2)
True
>>> A.add_word("elephant", 3)
True
>>> len(A)
3
>>> A.clear()
>>> len(A)
0
keys([prefix, [wildcard, [how]]])
Return an iterator on keys. If the optional prefix string is provided, only yield keys starting with this prefix.

If the optional wildcard is provided as a single character string, then the prefix is treated as a simple pattern using this character as a wildcard.

The optional how argument is used to control how strings are matched using one of these possible values:

ahocorasick.MATCH_EXACT_LENGTH (default) Yield matches that have the same exact length as the prefix length.
ahocorasick.MATCH_AT_LEAST_PREFIX Yield matches that have a length greater or equal to the prefix length.
ahocorasick.MATCH_AT_MOST_PREFIX Yield matches that have a length lesser or equal to the prefix length.
items([prefix, [wildcard, [how]]])
Return an iterator on tuples of (key, value). Keys are matched optionally to the prefix using the same logic and arguments as in the keys() method.

values([prefix, [wildcard, [how]]])
Return an iterator on values associated with each keys. Keys are matched optionally to the prefix using the same logic and arguments as in the keys() method.

make_automaton()
Finalize and create the Aho-Corasick automaton based on the keys already added to the trie. This does not require additional memory. After successful creation the Automaton.kind attribute is set to ahocorasick.AHOCORASICK.

iter(string, [start, [end]], ignore_white_space=False)
Perform the Aho-Corasick search procedure using the provided input string.

Return an iterator of tuples (end_index, value) for keys found in string where:

end_index is the end index in the input string where a trie key string was found.
value is the value associated with the found key string.
The start and end optional arguments can be used to limit the search to an input string slice as in string[start:end].

The ignore_white_space optional arguments can be used to ignore white spaces from input string.

iter_long(string, [start, [end]])
Perform the modified Aho-Corasick search procedure which matches the longest words from set.

Return an iterator of tuples (end_index, value) for keys found in string where:

end_index is the end index in the input string where a trie key string was found.
value is the value associated with the found key string.
The start and end optional arguments can be used to limit the search to an input string slice as in string[start:end].

Example
The default Aho-Corasick algorithm returns all occurrences of words stored in the automaton, including substring of other words from string. Method iter_long reports only the longest match.

For set of words {“he”, “her”, “here”} and a needle “he here her” the default algorithm finds following words: “he”, “he”, “her”, “here”, “he”, “her”, while the modified one yields only: “he”, “here”, “her”.

>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("he", "he")
True
>>> A.add_word("her", "her")
True
>>> A.add_word("here", "here")
True
>>> A.make_automaton()
>>> needle = "he here her"
>>> list(A.iter_long(needle))
[(1, 'he'), (6, 'here'), (10, 'her')]
>>> list(A.iter(needle))
[(1, 'he'), (4, 'he'), (5, 'her'), (6, 'here'), (9, 'he'), (10, 'her')]
find_all(string, callback, [start, [end]])
Perform the Aho-Corasick search procedure using the provided input string and iterate over the matching tuples (end_index, value) for keys found in string. Invoke the callback callable for each matching tuple.

The callback callable must accept two positional arguments: - end_index is the end index in the input string where a trie key string was found. - value is the value associated with the found key string.

The start and end optional arguments can be used to limit the search to an input string slice as in string[start:end].

Equivalent to a loop on iter() calling a callable at each iteration.

__reduce__()
Return pickle-able data for this automaton instance.

save(path, serializer)
Save content of automaton in an on-disc file.

Serializer is a callable object that is used when automaton store type is STORE_ANY. This method converts a python object into bytes; it can be pickle.dumps.

load(path, deserializer) => Automaton
Load automaton previously stored on disc using save method.

Deserializer is a callable object which converts bytes back into python object; it can be pickle.loads.

Return the approximate size in bytes occupied by the Automaton instance in memory excluding the size of associated objects when the Automaton is created with Automaton() or Automaton(ahocorasick.STORE_ANY).

get_stats() -> dict
Return a dictionary containing Automaton statistics.

nodes_count - total number of nodes
words_count - number of distinct words (same as len(automaton))
longest_word - length of the longest word
links_count - number of edges
sizeof_node - size of single node in bytes
total_size - total size of trie in bytes (about nodes_count * size_of node + links_count * size of pointer).
Examples
>>> import ahocorasick
>>> A = ahocorasick.Automaton()
>>> A.add_word("he", None)
True
>>> A.add_word("her", None)
True
>>> A.add_word("hers", None)
True
>>> A.get_stats()
{'nodes_count': 5, 'words_count': 3, 'longest_word': 4, 'links_count': 4, 'sizeof_node': 40, 'total_size': 232}
dump()
Return a three-tuple of lists describing the Automaton as a graph of nodes, edges, failure links.

nodes: each item is a pair (node id, end of word marker)
edges: each item is a triple (node id, label char, child node id)
failure links: each item is a pair (source node id, node if connected by fail node)
For each of these, the node id is a unique number and a label is a number.

set(string, reset=False)
Set a new string to search. When the reset argument is False (default) then the Aho-Corasick procedure is continued and the internal state of the Automaton and end index of the string being searched are not reset. This allow to search for large strings in multiple smaller chunks.
```