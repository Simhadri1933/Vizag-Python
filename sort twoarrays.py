X = [5, 3, 7, 9, 0, 1, 4, 2, 6, 8]
Y = [10, 1, 26, 18, 53, 15, 3, 2, 8, 6,23]

new_list = []

for x, y in zip(X, Y):
    new_list.append((x, y))

new_list = sorted(new_list)
X, Y = [], []

for x, y in new_list:
    X.append(x)
    Y.append(y)
print(new_list)