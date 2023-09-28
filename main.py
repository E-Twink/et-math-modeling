import random

color_arr = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
sym_arr = ['X', 'N', 'Z', 'V', 'I', 'H', 'T', 'Y', ]

for x in range(16):
    for y in range(32):
        print(color_arr[random.randint(0, len(color_arr) - 1)] + sym_arr[random.randint(0, len(sym_arr) - 1)], end='')
    print()