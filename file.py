def count_words():
    file=input("enter the file name")
    f=open(file,"r")
    number=0
    l=0
    for line in f:
        words=line.split()
        number=number+len(words)
        l+=1
    f.read()
    print(number)
    print("number of line=",l)
count_words()
