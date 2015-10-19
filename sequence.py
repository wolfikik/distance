# coding: utf8

def bmPredCompil(x):
    d = {}
    lenx = len(x)
    for i in xrange(len(x)):
        d[ord(x[i])] = lenx - i
    return d

def boyerMurSearch(s, x):
    d = bmPredCompil(x)

    lenX = i = j = k = len(x)
    while j > 0 and i<=len(s):
        if s[k-1] == x[j-1]:
            k -= 1
            j -= 1
        else:
            i += d[ord(s[i])]
            j = lenX
            k = i
    if j <= 0:
        return k
    return None

def searchInf(word):
    i = 10
    s = ''
    while True:
        i += 1
        s += str(i)
        pos = boyerMurSearch(str(s), str(word))

        if pos:
            print(pos)


def init():
    while True:
        try:
            search = int(raw_input("Введите искомое число:"))
            pos = searchInf(search)
            print(pos)
        except:
            break

init()