L=[]
for i in range(1,101):
    if i/8 == 1:
        L.append(i)
    elif i == 18:
        L.append(i)
    elif i == 28:
        L.append(i)
    elif i == 38:
        L.append(i)
    elif i==48:
        L.append(i)
    elif i == 58:
        L.append(i)
    elif i==68:
        L.append(i)
    elif i == 78:
        L.append(i)
    elif i in range(80,90):
        L.append(i)
    elif i == 98:
        L.append(i)
else:
    print(L)
    print(len(L))
