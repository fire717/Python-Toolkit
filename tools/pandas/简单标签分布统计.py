import cv2

import numpy as np
import pandas as pd
from PIL import Image



df = pd.read_csv("./train/train.csv")

print(len(df))


y = np.array(df['label'])
key = np.unique(y)
result = {}
counts = []
for k in key:
    mask = (y == k)
    y_new = y[mask]
    v = y_new.size
    result[k] = v
    counts.append(v)
print(result)


print("mean: ",np.mean(counts))
print("std: ",np.std(counts))
