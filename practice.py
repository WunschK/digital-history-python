# 1 ) Gib alle Zahlen von 1 - 100 aus

n = 0
while(n < 100):
    n = n + 1
    print(n)



# 2) Ersetze alle Zahlen die durch drei teilbar sind durch "digital"
n = 0
while(n < 100):
    n = n + 1
    if(n % 3 == 0):
        print("digital")
    else:
        print(n)

# 3) Ersetze alle Zahlen die durch fünf teilbar sind durch "history"

n = 0
while(n < 100):
    n = n + 1
    if(n % 5 == 0):
        print("history")
    else:
        print(n)

# 4) Kombiniere die beiden obigen Schritte mit einem "elif"

n = 0
while(n < 100):
    n = n + 1
    if(n % 3 == 0):
        print("digital")
    elif(n % 5 == 0):
        print("history")
    else:
        print(n)


# 5) Ersetze alle Zahlen die durch drei teilbar sind durch "Digital" und die die durch fünf teilbar sind durch "history". Zahlen die durch beides teilbar sind durch "digital history"

n = 0
while(n < 100):
    n = n + 1
    if(n % 3 == 0 and n % 5 == 0):
        print("digital history")
    else:
        print(n)

