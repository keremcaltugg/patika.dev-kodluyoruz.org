list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list = []

def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            lnew.append(i)

flatten(list)
print(flatten_list)
