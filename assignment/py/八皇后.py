def generate(l, list, layer):
    if layer == 8:
        l += [int(''.join([str(x + 1) for x in list]))]
        return 0
    for i in range(8):
        list[layer] = i
        for j in range(layer):
            if (list[j] == i) or (abs(i - list[j]) == layer - j):
                break
        else:
            generate(l, list, layer+1)
l = []
generate(l, [-1] * 8, 0)
for _ in range(int(input())):
    print(l[int(input()) - 1])