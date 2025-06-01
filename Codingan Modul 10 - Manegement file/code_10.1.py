import re

text1 = open('text1.txt')
text2 = open('text2.txt')

kalimat = []
baris = 0

for line in text1 :
    kalimat.append(line)

for line in text2 :
    if line != kalimat[baris]:
        line = re.sub('\n', '', line)
        coba = re.sub('\n', '', kalimat[baris])
        print(f'Text 1 : {coba} | Text 2 : {line} --> Baris ke {baris}')
    baris += 1