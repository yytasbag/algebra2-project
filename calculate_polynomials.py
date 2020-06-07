import matplotlib.pyplot as plt
R = QQ["x"]
f = x^7 + 11*x^6 + 42*x^5 + 45*x^4 + 34*x^3 + 31*x^2 + 24*x + 16
f = R(f)
ps = []
p = 2
l = 1000
for _ in range(l):
    ps.append(p)
    p = next_prime(p)


d = l
cs = set([(2, 3), (2, 2, 3), (2, 5), (2, 2, 2), (3, 3), (2,), (3,), (4,), (5,), (), (6,), (2, 2), (7,), (3, 4), (2, 4)])
cycles = dict()

for c in cs:
    cycles[c] = 0

for p in ps:
    if f.discriminant() % p == 0:
        d -= 1
        continue
    S = GF(p)["y"]
    f2 = S(f)
    fs = list(factor(f2))
    fs = filter(lambda s: s != 1, map(lambda s: s[0].degree(), fs))
    fs.sort()
    fs = tuple(fs)
    # print(fs)
    cycles[fs] += 1

for c in cs:
    cycles[c] = cycles[c] / d

calc = cycles.items()
calc.sort()

keys = map(lambda s: str(s[0]), calc)
values = map(lambda s: s[1], calc)
plt.ylabel("Cycles")
plt.xlabel("Frequency")
plt.title("Polynomial " + str(f))
plt.barh(keys, values)