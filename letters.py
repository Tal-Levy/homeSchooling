import string
import numpy as np


class Letters(object):
    def __init__(self):
        self.lowercase_alphabet_list = string.ascii_lowercase
        self.indeces = np.arange(len(self.lowercase_alphabet_list))
        self.list_size = len(self.lowercase_alphabet_list)

    def re_init(self):
        self.indeces = np.arange(len(self.lowercase_alphabet_list))
        self.list_size = len(self.lowercase_alphabet_list)

    def pick_a_letter(self):
        ind = np.random.randint(0, self.list_size)
        random_index = self.indeces[ind]
        self.indeces[ind], self.indeces[self.list_size-1] = self.indeces[self.list_size-1], self.indeces[ind]
        self.list_size -= 1
        if self.list_size == 1:
            self.re_init()
        return self.lowercase_alphabet_list[random_index]
