cnt = 1
serial = "5B134977135E7D13"

flag = ""
for i in range(0, len(serial), 2):
    v = chr(int(serial[i:i+2], 16) ^ (0x10 * cnt))
    
    if cnt == 3:
        cnt = 1
    else:
        cnt += 1
    flag += v
print("FLAG : {}".format(flag))

