#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E



def encode(s):
    encoding = "" 
    i = 0
    while i < len(s):
        count = 1 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1 
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding
 
 
if __name__ == '__main__':
 
    s = 'aaafffqwepppppp'
    print(encode(s))