import random
from datetime import datetime

# zakresy liczb
zakresy = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000]

# puste listy wygenerowane liczby w ilości od 2000 do 20000 liczb w liście

# listy na losowo generowane liczby
random2000 = []
random4000 = []
random6000 = []
random8000 = []
random10000 = []
random12000 = []
random14000 = []
random16000 = []
random18000 = []
random20000 = []

# listy na dane posortowane rosnąco
ascending2000 = []
ascending4000 = []
ascending6000 = []
ascending8000 = []
ascending10000 = []
ascending12000 = []
ascending14000 = []
ascending16000 = []
ascending18000 = []
ascending20000 = []

# listy na dane posortowane malejąco
descending2000 = []
descending4000 = []
descending6000 = []
descending8000 = []
descending10000 = []
descending12000 = []
descending14000 = []
descending16000 = []
descending18000 = []
descending20000 = []

# listy na dane V-kształtne
v2000 = []
v4000 = []
v6000 = []
v8000 = []
v10000 = []
v12000 = []
v14000 = []
v16000 = []
v18000 = []
v20000 = []

# listy na dane A-kształtne
a2000 = []
a4000 = []
a6000 = []
a8000 = []
a10000 = []
a12000 = []
a14000 = []
a16000 = []
a18000 = []
a20000 = []

# listy na dane stałe
const2000 = []
const4000 = []
const6000 = []
const8000 = []
const10000 = []
const12000 = []
const14000 = []
const16000 = []
const18000 = []
const20000 = []

# tablice pomocnicze
randomlisty = [random2000, random4000, random6000, random8000, random10000, random12000, random14000, random16000, random18000, random20000]
ascendinglisty = [ascending2000, ascending4000, ascending6000, ascending8000, ascending10000, ascending12000, ascending14000, ascending16000, ascending18000, ascending20000]
descendinglisty = [descending2000, descending4000, descending6000, descending8000, descending10000, descending12000, descending14000, descending16000, descending18000, descending20000]
vlisty = [v2000, v4000, v6000, v8000, v10000, v12000, v14000, v16000, v18000, v20000]
alisty = [a2000, a4000, a6000, a8000, a10000, a12000, a14000, a16000, a18000, a20000]
constlisty = [const2000, const4000, const6000, const8000, const10000, const12000, const14000, const16000, const18000, const20000]

# generowanie losowych liczb
def generaterandom():
    for a in randomlisty:
        for i in range(0, zakresy[randomlisty.index(a)]):
            x = random.randint(0, 20000)
            a.append(x)

generaterandom()

# generowanie posortowanych rosnąco liczb
for a in ascendinglisty:
    x = range(0, zakresy[ascendinglisty.index(a)])
    for i in x:
        a.append(i)

# generowanie posortowanych malejąco liczb
for a in descendinglisty:
    x = range(zakresy[descendinglisty.index(a)], 0, -1)
    for i in x:
        a.append(i)

# generowanie V-kształtnych liczb
for a in vlisty:
    x = range(zakresy[vlisty.index(a)]//2, 0 , -1)
    y = range(1, zakresy[vlisty.index(a)]//2+1)
    for i in x:
        a.append(i)
    for i in y:
        a.append(i)

# generowanie A-kształtnych liczb
for a in alisty:
    x = range(zakresy[alisty.index(a)]//2, 0 , -1)
    y = range(1, zakresy[alisty.index(a)]//2+1)
    for i in y:
        a.append(i)
    for i in x:
        a.append(i)

# generowanie stałych liczb ( ta funkcja nie zostanie wywołana ponownie aż do zakończenia programu - tworzymy dane stałe )
for a in constlisty:
    for i in range(0, zakresy[constlisty.index(a)]):
        x = random.randint(0, 20000)
        a.append(x)

"""
print("SELECTION SORT")
# selection sort (losowe dane)
for a in randomlisty:
    startTime = datetime.now()
    for i in range(len(a)):
        min = i
        for n in range(i+1, len(a)):
            if a[min] > a[n]:
                min = n
        a[i], a[min] = a[min], a[i]

    print("Losowe", len(a) , datetime.now() - startTime)
print("")

# selection sort (posortowane rosnąco dane)
for a in ascendinglisty:
    startTime = datetime.now()
    for i in range(len(a)):
        min = i
        for n in range(i+1, len(a)):
            if a[min] > a[n]:
                min = n
        a[i], a[min] = a[min], a[i]

    print("Rosnace", len(a) , datetime.now() - startTime)
print("")

# selection sort (posortowane malejąco dane)
for a in descendinglisty:
    startTime = datetime.now()
    for i in range(len(a)):
        min = i
        for n in range(i+1, len(a)):
            if a[min] > a[n]:
                min = n
        a[i], a[min] = a[min], a[i]

    print("Malejace", len(a) , datetime.now() - startTime)
print("")

# selection sort (V-kształtne dane)
for a in vlisty:
    startTime = datetime.now()
    for i in range(len(a)):
        min = i
        for n in range(i+1, len(a)):
            if a[min] > a[n]:
                min = n
        a[i], a[min] = a[min], a[i]

    print("V-ksztaltne", len(a) , datetime.now() - startTime)
print("")

# selection sort (A=kształtne)
for a in alisty:
    startTime = datetime.now()
    for i in range(len(a)):
        min = i
        for n in range(i+1, len(a)):
            if a[min] > a[n]:
                min = n
        a[i], a[min] = a[min], a[i]

    print("A-kształtne", len(a) , datetime.now() - startTime)
print("")

# selection sort (dane stałe)
for a in constlisty:
    startTime = datetime.now()
    for i in range(len(a)):
        min = i
        for n in range(i+1, len(a)):
            if a[min] > a[n]:
                min = n
        a[i], a[min] = a[min], a[i]

    print("Stale", len(a) , datetime.now() - startTime)
print("")
"""

print("INSERTION SORT")

for a in randomlisty:
    for i in range(1, len(a)):

        key = a[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = key

print(random2000)