import itertools
candidates = [2,3,6,7]
target = 7

# x = list(itertools.combinations(candidates,3))
# print(x)

for i,k in enumerate(candidates):
    if i >1:
        x = list(itertools.permutations(candidates,i))
        print(x)
        # x = [sum(x) for x in x]
        # print(x)