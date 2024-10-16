def check (start, finish, m):
    x1, y1 = start
    x2, y2 = finish
    m_x, m_y = m
    a = x2 - x1
    b = y2 - y1
    c = m_x - x1
    d = m_y - y1
    S = a*d - b*c
    return S
    # if S == 0:
    #     return True
    # else:
    #     return False
import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)