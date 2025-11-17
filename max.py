from abc import ABC
from copy import copy
from re import S


s1 = input()
s2 = input()
s3 = input()
f = True

s = [s1, s2, s3]
s.sort(key=lambda x: x.count("A"), reverse=True)
print(s)

s1, s2, s3 = s[0], s[1], s[2]

a_s1, b_s1, c_s1 = s1.count("A"), s1.count("B"), s1.count("C")
a_s2, b_s2, c_s2 = s2.count("A"), s2.count("B"), s2.count("C")
a_s3, b_s3, c_s3 = s3.count("A"), s3.count("B"), s3.count("C")


if (a_s1 == b_s2) and (a_s1 == c_s3):
    s22 = s2.replace("B", "a").replace("C", "b").replace("A", "c")
    s33 = s3.replace("C", "a").replace("B", "c").replace("A", "b")
    s11 = s1.lower()
elif (a_s1 == c_s2) and (a_s1 == b_s3):
    s22 = s2.replace("C", "a").replace("B", "c").replace("A", "b")
    s33 = s3.replace("B", "a").replace("C", "b").replace("A", "c")
    s11 = s1.lower()
else:
    f = False


if f:
    res = []
    k2, k3 = 0, 0 # подгоняем под 1
    t1, t3 = 0, 0 # подгоняем под 2
    m1, m2 = 0, 0 # подгоняем под 3
    st1, sm1 = copy(s11), copy(s11)
    sk2, sm2 = copy(s22), copy(s22)
    sk3, st3 = copy(s33), copy(s33)
    for i in range(len(s11) + 1):
        if sk2 != s11:
            k2 += 1
            sk2 = sk2[1:] + sk2[:1]
        if sk3 != s11:
            k3 += 1
            sk3 = sk3[1:] + sk3[:1]
        if st1 != s22:
            t1 += 1
            st1 = st1[1:] + st1[:1]
        if st3 != s22:
            t3 += 1
            st3 = st3[1:] + st3[:1]
        if sm1 != s33:
            m1 += 1
            sm1 = sm1[1:] + sm1[:1]
        if sm2 != s33:
            m2 += 1
            sm2 = sm2[1:] + sm2[:1]
    if (k2 >= len(s11)) or (k3 >= len(s11)):
        f = False

if f:
    n = len(s11)
    res = [min(k2, n - k2) + min(k3, n - k3),min(t1, n - t1) + min(t3, n - t3), 
    min(m1, n - m1) + min(m2, n - m2)]
    print(min(res))
else:
    print(-1)
        
