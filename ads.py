#!/usr/bin/env python3
# A B S T R A C T   D A T A   S T R U C T U R E S

# Project   Abstract Data Structures (Stack and Queue)
# Author    Barnabas Markus
# Email     barnabasmarkus@gmail.com
# Date      14.09.2016
# Python    3.5.1
# License   MIT


class AbstractDataStructure:

    def __init__(self, storage, max_size):
        self._size = max_size
        self._storage = list(storage) if storage != None else []

    @property
    def size(self):
        return self._size

    def is_full(self):
        if self._size:
            return True if len(self._storage) >= self._size else False
        else:
            return False

    def is_empty(self):
        return True if len(self._storage) == 0 else False

    def __len__(self):
        return len(self._storage)


class Stack(AbstractDataStructure):

    def __init__(self, storage=None, max_size=None):
        super().__init__(storage, max_size)

    @property
    def stack(self):
        return self._storage

    def peek(self):
        if not self.is_empty():
            return self._storage[-1]

    def push(self, item):
        if not self.is_full():
            self._storage.append(item)

    def pop(self):
        if not self.is_empty():
            return self._storage.pop()


class Queue(AbstractDataStructure):

    def __init__(self, storage=None, max_size=None):
        super().__init__(storage, max_size)

    @property
    def queue(self):
        return self._storage

    def peek(self):
        if not self.is_empty():
            return self._storage[0]

    def enqueue(self, item):
        self._storage.append(item)
        if self.is_full():
            pop = self._storage[0]
            self._storage = self._storage[1:]
            return pop

    def dequeue(self):
        if not self.is_empty():
            pop = self._storage[0]
            self._storage = self._storage[1:]
            return pop
