# https://github.com/spro/practical-pytorch

import string
import random
import time
import math
import torch
from torch.autograd import Variable

# Reading and un-unicode-encoding data

def read_file(filename):
    file = open(filename).read()
    char_set = set(file);
    char_list = list(char_set)
    all_characters = "".join(c for c in char_list)
    n_characters = len(all_characters)
    print(n_characters)
    return file, len(file), all_characters, n_characters

# Turning a string into a tensor

def char_tensor(string, all_characters):
    tensor = torch.zeros(len(string)).long()
    for c in range(len(string)):
        tensor[c] = all_characters.index(string[c])
    return Variable(tensor)

# Readable time elapsed

def time_since(since):
    s = time.time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

