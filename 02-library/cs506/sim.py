def euclidean_dist(x, y):
    if len(x) != len(y):
        return "Invalid input."
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i]) ** 2
    res **= (1 / 2)
    return res

def manhattan_dist(x, y):
    if len(x) != len(y):
        return "Invalid input."
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    if x == y:
        return 0
    X = set(x)
    Y = set(y)
    res = 1 - len(X.intersection(Y)) / len(X.union(Y))
    return res

def cosine_sim(x, y):
    if len(x) != len(y):
        return "Invalid input."
    res = 0
    a = 0
    b = 0
    for i in range(len(x)):
        res += x[i] * y[i]
        a += x[i] ** 2
        b += y[i] ** 2
    a **= (1 / 2)
    b **= (1 / 2)
    if a == 0 or b == 0:
        return 0
    res = res / (a * b)
    return res

# Feel free to add more
