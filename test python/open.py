with open("test.txt", "rw") as rek:
    if sek.readable(): 
        print(str(rek.read()))
    else :
        rek.write("hi yousef")