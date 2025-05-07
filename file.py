import string
import numpy as np

alpha_set = '$' + string.ascii_lowercase
alpha_len = len(alpha_set)

enc_map = {}
dec_map = {}

for idx, symbol in enumerate(alpha_set):
    vec = np.zeros(alpha_len)
    vec[idx] = 1
    enc_map[symbol] = vec
    dec_map[tuple(vec)] = symbol

proc_names = []
input_seqs = []
target_seqs = []
