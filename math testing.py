s = 1
t = 0
for i in range(2,100):
    t = t + s
    s = ((-1)**i)*(i)
    print(t)