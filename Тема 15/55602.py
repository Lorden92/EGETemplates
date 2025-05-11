for a in range(1,256):
    for x in range(1,256):
        if not (((x & 114 != 0) or (x & 94 != 0)) <= ((x & 73 ==0) <= (x & a !=0))):
            break
    else:
        print(a)
        break
