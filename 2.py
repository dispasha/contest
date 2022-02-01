with open('input.txt', 'r') as input:
    inp = [i for i in input]
    a = list(map(int, inp[0].split()))
    k = int(inp[1])

mat_init = sum(a)/len(a)
mat_modif = 0
for i in a:
    for j in a:
        if i != j:
            mat_modif += i
mat_modif = mat_modif/36
mat = mat_init
for i in range(1,k):
        mat+=mat_modif
print(mat)