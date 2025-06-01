import re

handel = open('soal.txt')
for line in handel:
    line = line.split('||')
    pisah_jawaban = re.sub('\n','',line[1])
    jawab = pisah_jawaban.split()
    jawab = ' '.join(jawab)
    print(line[0])
    masuk = input('Jawaban: ')
    if masuk.lower() == jawab.lower():
        print('Jawaban benar!')
    else:
        print('Jawaban salah!')