from matplotlib import pyplot as plt

n, mn, mx = map(int, input().split())

arr1_x = []
arr2_x = []
arr1_y = []
arr2_y = []
present1 = []
present2 = []

print("First:\n")

for i in range(0, n):
    arr1_x.append(int(input()))

print("Second:\n")

for i in range(0, n):
    arr2_x.append(int(input()))

for i in sorted(arr1_x):
    if i not in present1:
        present1.append(i)
        arr1_y.append(arr1_x.count(i))

for i in sorted(arr2_x):
    if i not in present2:
        present2.append(i)
        arr2_y.append(arr2_x.count(i))

arr1_x = list(set(sorted(arr1_x)))
arr2_x = list(set(sorted(arr2_x)))

fig, (axis1, axis2) = plt.subplots(2, 1, figsize=(5, 5))
axis1.grid(True)
axis1.bar(arr1_x, arr1_y, label="Наш алгоритм")
axis1.set_xlabel("Число")
axis1.set_ylabel("Сколько раз появляется в последовательности")
axis1.legend()

axis2.grid(True)
axis2.bar(arr2_x, arr2_y, label="rand")
axis2.set_xlabel("Число")
axis2.set_ylabel("Сколько раз появляется в последовательности")
axis2.legend()

plt.show()

