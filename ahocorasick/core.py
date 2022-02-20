#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2022-02-20
"""
ahocorasick的python版，替换pyahocorasick的模块。
"""
import os


class node(object):
    def __init__(self):
        self.next = {}  # 相当于指针，指向树节点的下一层节点
        self.fail = None  # 失配指针，这个是AC自动机的关键
        self.isWord = False  # 标记，用来判断是否是一个标签的结尾
        self.word = ""  # 用来储存标签


class Automaton(object):
    """AC自动机python版本。"""

    def __init__(self, path=''):
        """
        path: 词表文件路径。
        词表格式：一行一个词语，可用空格或制表符分开为多个部分，第一部分是key，其他的是value。
        key即为需要检索的词语。
        例如：
        AC 1\t字母\n
        自动机\n

        key和value分别是：{'AC': '1\t字母', '自动机': None}
        """
        self.root = node()
        self.word_dict = {}
        self.user_dict_path = path
        self.make_automaton()

    def _add_word(self, key, value=None) -> bool:
        """"""
        self.word_dict[key] = value
        temp_root = self.root
        for char in key:
            if char not in temp_root.next:
                temp_root.next[char] = node()
            temp_root = temp_root.next[char]
        temp_root.isWord = True
        temp_root.word = key
        return True

    def _make_automaton(self):
        if not os.path.isfile(self.user_dict_path):
            return
        with open(self.user_dict_path, "rt", encoding="utf-8") as fin:
            for line in fin:
                parts = line.split(maxsplit=1)
                self.add_word(*parts)

    def _make_fail(self):
        temp_que = []
        temp_que.append(self.root)
        while len(temp_que) != 0:
            temp = temp_que.pop(0)
            p = None
            for key, value in temp.next.item():
                if temp == self.root:
                    temp.next[key].fail = self.root
                else:
                    p = temp.fail
                    while p is not None:
                        if key in p.next:
                            temp.next[key].fail = p.fail
                            break
                        p = p.fail
                    if p is None:
                        temp.next[key].fail = self.root
                temp_que.append(temp.next[key])

    def _iter(self, string, return_span=False):

        content = string
        p = self.root
        result = set()
        index = 0
        while index < len(content) - 1:
            currentposition = index
            while currentposition < len(content):
                word = content[currentposition]
                while word in p.next == False and p != self.root:
                    p = p.fail

                if word in p.next:
                    p = p.next[word]
                else:
                    p = self.root

                if p.isWord:
                    end_index = currentposition
                    if return_span:
                        yield (end_index + 1 - len(p.word), end_index + 1)
                    else:
                        yield (end_index, self.get(p.word))
                    # end_index = currentposition + 1
                    # result.add((p.word, end_index - len(p.word), end_index))
                    # break
                currentposition += 1
            p = self.root
            index += 1
        return result

    def search(self, string):
        return [(k, v) for k, v in self.iter(string, return_span=True)]

    def add_word(self, key, value=None) -> bool:
        """"""
        return self._add_word(key, value)

    def make_automaton(self):
        """"""
        self._make_automaton()

    def iter(self, string, ignore_white_space=False, return_span=False):
        """
        if return_span == False:
            return pyahocorssick默认返回的是：(end_index, value)。
        else:
            return 起止位置的范围：(start_index, end_index + 1)，类似正则表达式的finditer方法的span。
        """
        return self._iter(string, return_span=return_span)

    def get(self, key):
        """
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
        """
        return self.word_dict.get(key)

    def exists(self, key) -> bool:
        """
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
        """
        return key in self.word_dict

    def longest_prefix(self, string) -> int:
        """
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
        """

    def match(self, key) -> bool:
        """
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
        """

    def len(self) -> int:
        """
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
        """
        return len(self.word_dict)

    def remove_word(self) -> bool:
        """"""

    def pop(self, word):
        """"""

    def clear(self):
        """"""

    def keys(self):
        """"""
        return self.word_dict.keys()

    def values(self):
        """"""
        return self.word_dict.values()

    def items(self):
        """"""
        return self.word_dict.items()

    def iter_long(self, string):
        """"""

    def find_all(self, string, callback=None):
        """"""
        if callback is None:
            return list(self.iter(string))
        else:
            return [callback(w) for w in self.iter(string)]

    # def __reduce__(self):
    #     """"""

    def save(self, path):
        """pickle.dumps"""
        import pickle
        with open(path, 'wb') as fout:
            pickle.dump(self, fout)

    def load(self, path):
        """"""
        import pickle
        with open(path, 'rb') as fin:
            return pickle.load(fin)

    def get_stats(self) -> dict:
        """"""

    def dump(self):
        """"""
        import pickle
        return pickle.dumps(self)

    def set(self, string, reset=False):
        """"""


if __name__ == "__main__":
    print(__file__)
    M = Automaton()
    for i, w in enumerate('ab bc bcd'.split()):
        M.add_word(w, (i, w))

    string = 'a12bcd34'
    for w in M.iter(string):
        print(w)
        # (4, (1, 'bc'))

    print(M.find_all(string))
    # [(4, (1, 'bc')), (5, (2, 'bcd')), (4, (1, 'bc')), (5, (2, 'bcd')), (4, (1, 'bc')), (5, (2, 'bcd')), (4, (1, 'bc')), (5, (2, 'bcd'))]

    print(M.search(string))
    # [(3, 5), (3, 6), (3, 5), (3, 6), (3, 5), (3, 6), (3, 5), (3, 6)]
