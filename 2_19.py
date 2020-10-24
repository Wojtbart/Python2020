#2.19
if __name__ == "__main__":
    
    L = [1,10,100,356,16,234,8]

    for i in range(len(L)):
        L[i] = str(L[i]).zfill(3)
    print (L)