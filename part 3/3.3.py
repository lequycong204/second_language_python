import numpy as np
import math
def cosineb2v(u, v):
    u = np.array(u)
    v = np.array(v)
    dot_uv = u * v
    rs = sum(i for i in dot_uv)
    norm_u = math.sqrt(sum(i ** 2 for i in u))
    norm_v = math.sqrt(sum(i ** 2 for i in v))
    return rs / (norm_u * norm_v)

# u=[1, 2, 3, 4, 5, 6]
# v=[2, 4, 6, 8, 10, 12]
# rs=cosineb2v(u,v)
# print(rs)