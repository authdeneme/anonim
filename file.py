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

for i in range(1, 6):
    proc_names.append(f"proc_{i}")
    input_seqs.append(f"input_seq_{i}")
    target_seqs.append(f"target_seq_{i}")