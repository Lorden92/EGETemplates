for z in range(50):
    for y in range(50):
        for x in range(50):
            s = '0'+z*'1'+y*'2'+x*'3'
            while '01' in s or '02' in s or '03' in s:
                s=s.replace('01', '30',1)
                s=s.replace('02', '101', 1)
                s=s.replace('03','202',1)
            if s.count('1')==15 and s.count('2')==10 and s.count('3')==60:
                print(z)
                break