word_4 = 0x70
serial = "76876-77776"


for word_1 in range(0x61, 0x7b):
    v8 = (word_1 & 1) + 5
    v59 = ((word_1 >> 4) & 1) + 5
    v53 = ((word_1 >> 1) & 1) + 5
    v55 = ((word_1 >> 2) & 1) + 5
    v57 = ((word_1 >> 3) & 1) + 5

    for word_2 in range(0x61, 0x7b):
        v45 = (word_2 & 1) + 1
        v51 = ((word_2 >> 4) & 1) + 1
        v47 = ((word_2 >> 1) & 1) + 1
        v10 = ((word_2 >> 2) & 1) + 1
        v49 = ((word_2 >> 3) & 1) + 1

        if v8 + v10 == int(serial[0]):
            if v57 + v49 == int(serial[1]):
                if v53 + v51 == int(serial[2]):
                    if v55 + v45 == int(serial[3]):
                        if v59 + v47 == int(serial[4]):
                            print('word_1 = {}, word_2 = {}\n'.format(chr(word_1), chr(word_2)))

print('- - - - - - - - - - - - - - - -\n')

for word_3 in range(0x61, 0x7b):
    v27 = (word_3 & 1) + 5
    v60 = ((word_3 >> 4) & 1) + 5
    v54 = ((word_3 >> 1) & 1) + 5
    v56 = ((word_3 >> 2) & 1) + 5
    v58 = ((word_3 >> 3) & 1) + 5

    v46 = (word_4 & 1) + 1
    v52 = ((word_4 >> 4) & 1) + 1
    v48 = ((word_4 >> 1) & 1) + 1
    v29 = ((word_4 >> 2) & 1) + 1
    v50 = ((word_4 >> 3) & 1) + 1

    if v27 + v29 == int(serial[6]):
        if v58 + v50 == int(serial[7]):
            if v54 + v52 == int(serial[8]):
                if v56 + v46 == int(serial[9]):
                    if v60 + v48 == int(serial[10]):
                        print('word_3 = {}, word_4 = {}\n'.format(chr(word_3), chr(word_4)))

                

    
    
    
    
