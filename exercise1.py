from collections import OrderedDict

my_dict = OrderedDict()

for n in range(int(input())):
    w = input()
    if w not in my_dict:
        my_dict[w] = 1
    else:
        my_dict[w] += 1

print(len(my_dict))
print(*my_dict.values())
