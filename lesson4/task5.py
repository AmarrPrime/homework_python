# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов


f1 = open("file1.txt", "r+")
f2 = open("file2.txt", "r+")
f3 = open("file3.txt", "w+")

f3.write(f1.read()+"+"+f2.read())
