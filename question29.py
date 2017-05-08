import numpy as np

a = np.arange(2, 101, dtype='f8')
print(len(set(np.array(a.repeat(len(a)) ** np.tile(a, len(a))))))