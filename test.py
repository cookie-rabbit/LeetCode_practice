a = [1,2,3,4,5]
b = [1,1,1,3,5,2,3,4,5,4]

for i in a:
    b.remove(i)
    try:
        b.pop(i)
    except ValueError:
        continue
    else:
        print(i)
