def swapData():
    open1 = open("sample1.txt")
    open2 = open("sample2.txt")
    
    with open(open1, 'r') as a:
        data_a = a.read()
    
    with open(open2, 'r') as b:
        data_b = b.read()

    with open(open1, 'w') as a:
        a.write(data_b)
    
    with open(open2, 'w') as b:
        b.write(data_a)
