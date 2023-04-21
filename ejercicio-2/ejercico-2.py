multi_7=0
multi_9=0

for i in range(1000, 5000):
    if i % 7 ==0:
        multi_7=multi_7+1
    if i % 9 ==0:
        multi_9=multi_9+1

print("entre 1000 y 5000 hay " + str (multi_7) + " multiplos en 7")
print("entre 1000 y 5000 hay " + str (multi_9) + " multiplos en 9")
