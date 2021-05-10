import random
from datetime import datetime
import csv
from csv import writer

startTimeFull = datetime.now()

with open("wynik.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Algorytm', 'Ilość elementów', 'Typ elementów', 'Czas wykonania'])

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
def generateascending():
    for a in ascendinglisty:
        x = range(0, zakresy[ascendinglisty.index(a)])
        for i in x:
            a.append(i)

generateascending()

# generowanie posortowanych malejąco liczb
def generatedescending():
    for a in descendinglisty:
        x = range(zakresy[descendinglisty.index(a)], 0, -1)
        for i in x:
            a.append(i)

generatedescending()

# generowanie V-kształtnych liczb
def generatev():
    for a in vlisty:
        x = range(zakresy[vlisty.index(a)]//2, 0 , -1)
        y = range(1, zakresy[vlisty.index(a)]//2+1)
        for i in x:
            a.append(i)
        for i in y:
            a.append(i)

generatev()

# generowanie A-kształtnych liczb
def generatea():
    for a in alisty:
        x = range(zakresy[alisty.index(a)]//2, 0 , -1)
        y = range(1, zakresy[alisty.index(a)]//2+1)
        for i in y:
            a.append(i)
        for i in x:
            a.append(i)

generatea()

# generowanie stałych liczb ( zawsze będą to te same losowe liczby )
seed = 1
def generateconst():
    for a in constlisty:
        for i in range(0, zakresy[constlisty.index(a)]):
            random.seed(seed + i)
            x = random.randint(0, 20000)
            a.append(x)

generateconst()





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

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Selection sort', len(a), 'Posortowane losowo', time])
        f_object.close()
    print("Losowe", len(a) , time)
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

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Selection sort', len(a), 'Posortowane rosnąco', time])
        f_object.close()
    print("Rosnace", len(a) , time)
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

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Selection sort', len(a), 'Posortowane malejąco', time])
        f_object.close()
    print("Malejace", len(a) , time)
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

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Selection sort', len(a), 'V-kształtne', time])
        f_object.close()
    print("V-kształtne", len(a) , time)
print("")

# selection sort (A-kształtne)
for a in alisty:
    startTime = datetime.now()
    for i in range(len(a)):
        min = i
        for n in range(i+1, len(a)):
            if a[min] > a[n]:
                min = n
        a[i], a[min] = a[min], a[i]

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Selection sort', len(a), 'A-kształtne', time])
        f_object.close()
    print("A-kształtne", len(a) , time)
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

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Selection sort', len(a), 'Stałe', time])
        f_object.close()
    print("Stale", len(a) , time)
print("")







print("INSERTION SORT")

random2000.clear()
random4000.clear()
random6000.clear()
random8000.clear()
random10000.clear()
random12000.clear()
random14000.clear()
random16000.clear()
random18000.clear()
random20000.clear()

ascending2000.clear()
ascending4000.clear()
ascending6000.clear()
ascending8000.clear()
ascending10000.clear()
ascending12000.clear()
ascending14000.clear()
ascending16000.clear()
ascending18000.clear()
ascending20000.clear()

descending2000.clear()
descending4000.clear()
descending6000.clear()
descending8000.clear()
descending10000.clear()
descending12000.clear()
descending14000.clear()
descending16000.clear()
descending18000.clear()
descending20000.clear()

v2000.clear()
v4000.clear()
v6000.clear()
v8000.clear()
v10000.clear()
v12000.clear()
v14000.clear()
v16000.clear()
v18000.clear()
v20000.clear()

a2000.clear()
a4000.clear()
a6000.clear()
a8000.clear()
a10000.clear()
a12000.clear()
a14000.clear()
a16000.clear()
a18000.clear()
a20000.clear()

const2000.clear()
const4000.clear()
const6000.clear()
const8000.clear()
const10000.clear()
const12000.clear()
const14000.clear()
const16000.clear()
const18000.clear()
const20000.clear()

generaterandom()
generateascending()
generatedescending()
generatev()
generatea()
generateconst()

# insertion sort (losowe dane)
for a in randomlisty:
    startTime = datetime.now()
    for i in range(1, len(a)):
        
        key = a[i]

        x = i-1
        while x >= 0 and key < a[x] :
                a[x+1] = a[x]
                x -= 1
        a[x+1] = key

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Insertion sort', len(a), 'Posortowane losowo', time])
        f_object.close()
    print("Losowe", len(a) , time)
print("")

# insertion sort (posortowane rosnąco dane)
for a in ascendinglisty:
    startTime = datetime.now()
    for i in range(1, len(a)):
        
        key = a[i]

        x = i-1
        while x >= 0 and key < a[x] :
                a[x+1] = a[x]
                x -= 1
        a[x+1] = key

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Insertion sort', len(a), 'Posortowane rosnąco', time])
        f_object.close()
    print("Rosnace", len(a) , time)
print("")

# insertion sort (posortowane malejaco dane)
for a in descendinglisty:
    startTime = datetime.now()
    for i in range(1, len(a)):
        
        key = a[i]

        x = i-1
        while x >= 0 and key < a[x] :
                a[x+1] = a[x]
                x -= 1
        a[x+1] = key

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Insertion sort', len(a), 'Posortowane malejąco', time])
        f_object.close()
    print("Malejace", len(a) , time)
print("")

# insertion sort (V-kształtne)
for a in vlisty:
    startTime = datetime.now()
    for i in range(1, len(a)):
        
        key = a[i]

        x = i-1
        while x >= 0 and key < a[x] :
                a[x+1] = a[x]
                x -= 1
        a[x+1] = key

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Insertion sort', len(a), 'V-kształtne', time])
        f_object.close()
    print("V-ksztaltne", len(a) , time)
print("")

# insertion sort (A-kształtne)
for a in alisty:
    startTime = datetime.now()
    for i in range(1, len(a)):
        
        key = a[i]

        x = i-1
        while x >= 0 and key < a[x] :
                a[x+1] = a[x]
                x -= 1
        a[x+1] = key

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Insertion sort', len(a), 'A-kształtne', time])
        f_object.close()
    print("A-ksztaltne", len(a) , time)
print("")

# insertion sort (dane stałe)
for a in constlisty:
    startTime = datetime.now()
    for i in range(1, len(a)):
        
        key = a[i]

        x = i-1
        while x >= 0 and key < a[x] :
                a[x+1] = a[x]
                x -= 1
        a[x+1] = key

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['Insertion sort', len(a), 'Stałe', time])
        f_object.close()
    print("Stale", len(a) , time)
print("")









print("QuickSort")

random2000.clear()
random4000.clear()
random6000.clear()
random8000.clear()
random10000.clear()
random12000.clear()
random14000.clear()
random16000.clear()
random18000.clear()
random20000.clear()

ascending2000.clear()
ascending4000.clear()
ascending6000.clear()
ascending8000.clear()
ascending10000.clear()
ascending12000.clear()
ascending14000.clear()
ascending16000.clear()
ascending18000.clear()
ascending20000.clear()

descending2000.clear()
descending4000.clear()
descending6000.clear()
descending8000.clear()
descending10000.clear()
descending12000.clear()
descending14000.clear()
descending16000.clear()
descending18000.clear()
descending20000.clear()

v2000.clear()
v4000.clear()
v6000.clear()
v8000.clear()
v10000.clear()
v12000.clear()
v14000.clear()
v16000.clear()
v18000.clear()
v20000.clear()

a2000.clear()
a4000.clear()
a6000.clear()
a8000.clear()
a10000.clear()
a12000.clear()
a14000.clear()
a16000.clear()
a18000.clear()
a20000.clear()

const2000.clear()
const4000.clear()
const6000.clear()
const8000.clear()
const10000.clear()
const12000.clear()
const14000.clear()
const16000.clear()
const18000.clear()
const20000.clear()

generaterandom()
generateascending()
generatedescending()
generatev()
generatea()
generateconst()

def partition(array, start, end):
    pivot = array[(start + end)//2]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high
  
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


# QuickSort (losowe dane)
for a in randomlisty:
    startTime = datetime.now()
    n = len(a)
    quick_sort(a, 0, n-1)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['QuickSort', len(a), 'Posortowane losowo', time])
        f_object.close()
    print("Losowe", len(a) , time)
print("")


# QuickSort (posortowane rosnąco dane)
for a in ascendinglisty:
    startTime = datetime.now()
    n = len(a)
    quick_sort(a, 0, n-1)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['QuickSort', len(a), 'Posortowane rosnąco', time])
        f_object.close()
    print("Rosnace", len(a) , time)
print("")

# QuickSort (posortowane malejaco dane)
for a in descendinglisty:
    startTime = datetime.now()
    n = len(a)
    quick_sort(a, 0, n-1)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['QuickSort', len(a), 'Posortowane malejąco', time])
        f_object.close()
    print("Malejace", len(a) , time)
print("")

# QuickSort (V-kształtne)
for a in vlisty:
    startTime = datetime.now()
    n = len(a)
    quick_sort(a, 0, n-1)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['QuickSort', len(a), 'V-kształtne', time])
        f_object.close()
    print("V-ksztaltne", len(a) , time)
print("")

# QuickSort (A-kształtne)
for a in alisty:
    startTime = datetime.now()
    n = len(a)
    quick_sort(a, 0, n-1)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['QuickSort', len(a), 'A-kształtne', time])
        f_object.close()
    print("A-ksztaltne", len(a) , time)
print("")

# QuickSort (dane stałe)
for a in constlisty:
    startTime = datetime.now()
    n = len(a)
    quick_sort(a, 0, n-1)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['QuickSort', len(a), 'Stałe', time])
        f_object.close()
    print("Stale", len(a) , time)
print("")








print("HeapSort")

random2000.clear()
random4000.clear()
random6000.clear()
random8000.clear()
random10000.clear()
random12000.clear()
random14000.clear()
random16000.clear()
random18000.clear()
random20000.clear()

ascending2000.clear()
ascending4000.clear()
ascending6000.clear()
ascending8000.clear()
ascending10000.clear()
ascending12000.clear()
ascending14000.clear()
ascending16000.clear()
ascending18000.clear()
ascending20000.clear()

descending2000.clear()
descending4000.clear()
descending6000.clear()
descending8000.clear()
descending10000.clear()
descending12000.clear()
descending14000.clear()
descending16000.clear()
descending18000.clear()
descending20000.clear()

v2000.clear()
v4000.clear()
v6000.clear()
v8000.clear()
v10000.clear()
v12000.clear()
v14000.clear()
v16000.clear()
v18000.clear()
v20000.clear()

a2000.clear()
a4000.clear()
a6000.clear()
a8000.clear()
a10000.clear()
a12000.clear()
a14000.clear()
a16000.clear()
a18000.clear()
a20000.clear()

const2000.clear()
const4000.clear()
const6000.clear()
const8000.clear()
const10000.clear()
const12000.clear()
const14000.clear()
const16000.clear()
const18000.clear()
const20000.clear()

generaterandom()
generateascending()
generatedescending()
generatev()
generatea()
generateconst()


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 

        heapify(arr, n, largest)
 
 
def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# HeapSort (losowe dane)
for a in randomlisty:
    startTime = datetime.now()
    heapSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['HeapSort', len(a), 'Posortowane losowo', time])
        f_object.close()
    print("Losowe", len(a) , time)
print("")

# HeapSort (posortowane rosnąco dane)
for a in ascendinglisty:
    startTime = datetime.now()
    heapSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['HeapSort', len(a), 'Posortowane rosnąco', time])
        f_object.close()
    print("Rosnące", len(a) , time)
print("")

# HeapSort (posortowane malejaco dane)
for a in descendinglisty:
    startTime = datetime.now()
    heapSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['HeapSort', len(a), 'Posortowane malejąco', time])
        f_object.close()
    print("Malejace", len(a) , time)
print("")

# HeapSort (V-kształtne)
for a in vlisty:
    startTime = datetime.now()
    heapSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['HeapSort', len(a), 'V-kształtne', time])
        f_object.close()
    print("V-ksztaltne", len(a) , time)
print("")

# HeapSort (A-kształtne)
for a in alisty:
    startTime = datetime.now()
    heapSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['HeapSort', len(a), 'A-kształtne', time])
        f_object.close()
    print("A-ksztaltne", len(a) , time)
print("")

# HeapSort (dane stałe)
for a in constlisty:
    startTime = datetime.now()
    heapSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['HeapSort', len(a), 'Stałe', time])
        f_object.close()
    print("Stale", len(a) , time)
print("")









print("ShellSort")

random2000.clear()
random4000.clear()
random6000.clear()
random8000.clear()
random10000.clear()
random12000.clear()
random14000.clear()
random16000.clear()
random18000.clear()
random20000.clear()

ascending2000.clear()
ascending4000.clear()
ascending6000.clear()
ascending8000.clear()
ascending10000.clear()
ascending12000.clear()
ascending14000.clear()
ascending16000.clear()
ascending18000.clear()
ascending20000.clear()

descending2000.clear()
descending4000.clear()
descending6000.clear()
descending8000.clear()
descending10000.clear()
descending12000.clear()
descending14000.clear()
descending16000.clear()
descending18000.clear()
descending20000.clear()

v2000.clear()
v4000.clear()
v6000.clear()
v8000.clear()
v10000.clear()
v12000.clear()
v14000.clear()
v16000.clear()
v18000.clear()
v20000.clear()

a2000.clear()
a4000.clear()
a6000.clear()
a8000.clear()
a10000.clear()
a12000.clear()
a14000.clear()
a16000.clear()
a18000.clear()
a20000.clear()

const2000.clear()
const4000.clear()
const6000.clear()
const8000.clear()
const10000.clear()
const12000.clear()
const14000.clear()
const16000.clear()
const18000.clear()
const20000.clear()

generaterandom()
generateascending()
generatedescending()
generatev()
generatea()
generateconst()


def shellSort(arr):

    n = len(arr)
    gap = n//2
  
    while gap > 0:
  
        for i in range(gap,n):

            temp = arr[i]

            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
  

            arr[j] = temp
        gap //= 2


# ShellSort (losowe dane)
for a in randomlisty:
    startTime = datetime.now()
    shellSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['ShellSort', len(a), 'Posortowane losowo', time])
        f_object.close()
    print("Losowe", len(a) , time)
print("")

# ShellSort (posortowane rosnąco dane)
for a in ascendinglisty:
    startTime = datetime.now()
    shellSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['ShellSort', len(a), 'Posortowane rosnąco', time])
        f_object.close()
    print("Rosnace", len(a) , time)
print("")

# ShellSort (posortowane malejaco dane)
for a in descendinglisty:
    startTime = datetime.now()
    shellSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['ShellSort', len(a), 'Posortowane losowo', time])
        f_object.close()
    print("Losowe", len(a) , time)
print("")

# ShellSort (V-kształtne)
for a in vlisty:
    startTime = datetime.now()
    shellSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['ShellSort', len(a), 'V-kształtne', time])
        f_object.close()
    print("V-ksztaltne", len(a) , time)
print("")

# ShellSort (A-kształtne)
for a in alisty:
    startTime = datetime.now()
    shellSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['ShellSort', len(a), 'A-kształtne', time])
        f_object.close()
    print("A-ksztaltne", len(a) , time)
print("")

# ShellSort (dane stałe)
for a in constlisty:
    startTime = datetime.now()
    shellSort(a)

    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['ShellSort', len(a), 'Stałe', time])
        f_object.close()
    print("Stale", len(a) , time)
print("")

print("Calosc zajela: ", datetime.now() - startTimeFull)