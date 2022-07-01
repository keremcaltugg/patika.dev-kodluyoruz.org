l =[[1, 2], [3, 4], [5, 6, 7]]

new_l = l[::-1]

for i in range(len(new_l)):
    new_l[i] = new_l[i][::-1]
    
print(new_l)
