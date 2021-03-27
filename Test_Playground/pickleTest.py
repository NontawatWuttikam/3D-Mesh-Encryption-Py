import pickle
import sys
sys.path.append("/3D-Encrypt")
from ecc.curve import Point

with open("points.txt", "rb") as fp:   # Unpickling
    b = pickle.load(fp)

print(b)
print()