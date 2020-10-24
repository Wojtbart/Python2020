#2.17
if __name__ == "__main__":

    line = " lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua "
    words=line.split()
    list1=[]# lista na posortowane wilkosci liczb
    print("Wyrazy posortowane alfabetycznie: ",sorted(words)) # duze litery zawsze sortuje przed malymi
    for word in words:
        list1.append(len(word))
    print("Wyrazy posortowane wzgledem dlugosci",sorted(list1))


