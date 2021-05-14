import random
from datetime import datetime
import csv
from csv import writer

# pozwala na zmierzenie czasu wykonania całego programu
startTimeFull = datetime.now()

# towrzymy plik csv z nazwami tabel
with open("wynik.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Algorytm', 'Ilość elementów', 'Typ elementów', 'Czas wykonania'])

# zakresy liczb
zakresy = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000]


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

# funkcja czyszcząca listy i generująca nowe dane
def clear():
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

# generowanie stałych liczb ( lista o długości x składająca się x z powtórzeń jednej liczby )
def generateconst():
    for a in constlisty:
        for i in range(0, zakresy[constlisty.index(a)]):
            x = random.randint(1, 1)
            a.append(x)

generateconst()

# funkcja do mierzenia czasu wykonania algorytmu oraz zapisania wyniku do pliku csv
def saveExecutionTime(algorytm, sortowanie, printPosortowanie, startTime):
    time =  datetime.now() - startTime
    with open('wynik.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([algorytm, len(a), sortowanie, time])
        f_object.close()
    print(printPosortowanie, len(a) , time)




# SELECTION SORT
def selection(algorytm, sortowanie, printPosortowanie):
    startTime = datetime.now()
    for i in range(len(a)):
        min = i
        for n in range(i+1, len(a)):
            if a[min] > a[n]:
                min = n
        a[i], a[min] = a[min], a[i]

    saveExecutionTime(algorytm, sortowanie, printPosortowanie, startTime)



print("SELECTION SORT")
# selection sort (losowe dane)
for a in randomlisty:
    selection('Selection sort', 'Posortowane losowo', 'Losowe')
print("")

# selection sort (posortowane rosnąco dane)
for a in ascendinglisty:
   selection('Selection sort', 'Posortowane rosnąco', 'Rosnace')
print("")

# selection sort (posortowane malejąco dane)
for a in descendinglisty:
    selection('Selection sort', 'Posortowane malejąco', 'Malejace')
print("")

# selection sort (V-kształtne dane)
for a in vlisty:
   selection('Selection sort', 'V-kształtne', 'V-ksztaltne')
print("")

# selection sort (A-kształtne)
for a in alisty:
    selection('Selection sort', 'A-kształtne', 'A-ksztaltne')
print("")

# selection sort (dane stałe)
for a in constlisty:
    selection('Selection sort', 'Stałe', 'Stale')
print("")







# INSERTION SORT
def insertion(algorytm, sortowanie, printPosortowanie):
    startTime = datetime.now()
    for i in range(1, len(a)):
        
        key = a[i]

        x = i-1
        while x >= 0 and key < a[x] :
                a[x+1] = a[x]
                x -= 1
        a[x+1] = key

    saveExecutionTime(algorytm, sortowanie, printPosortowanie, startTime)



print("INSERTION SORT")

clear()

# insertion sort (losowe dane)
for a in randomlisty:
    insertion('insertion sort', 'Posortowane losowo', 'Losowe')
print("")

# insertion sort (posortowane rosnąco dane)
for a in ascendinglisty:
   insertion('insertion sort', 'Posortowane rosnąco', 'Rosnace')
print("")

# insertion sort (posortowane malejąco dane)
for a in descendinglisty:
    insertion('insertion sort', 'Posortowane malejąco', 'Malejace')
print("")

# insertion sort (V-kształtne dane)
for a in vlisty:
   insertion('insertion sort', 'V-kształtne', 'V-ksztaltne')
print("")

# insertion sort (A-kształtne)
for a in alisty:
    insertion('insertion sort', 'A-kształtne', 'A-ksztaltne')
print("")

# insertion sort (dane stałe)
for a in constlisty:
    insertion('insertion sort', 'Stałe', 'Stale')
print("")



print("Merge Sort")

clear()

def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
 
        L = arr[:mid]
 
        R = arr[mid:]
 
        mergeSort(L)

        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1





# Merge Sort (losowe dane)
for a in randomlisty:
    startTime = datetime.now()
    mergeSort(a)
    saveExecutionTime('Merge Sort', 'Posortowane losowo', 'Losowe', startTime)
print("")


# Merge Sort (posortowane rosnąco dane)
for a in ascendinglisty:
    startTime = datetime.now()
    mergeSort(a)
    saveExecutionTime('Merge Sort', 'Posortowane rosnąco', 'Rosnace', startTime)
print("")


# Merge Sort (posortowane malejaco dane)
for a in descendinglisty:
    startTime = datetime.now()
    mergeSort(a)
    saveExecutionTime('Merge Sort', 'Posortowane malejąco', 'Malejace', startTime)
print("")


# Merge Sort (V-kształtne)
for a in vlisty:
    startTime = datetime.now()
    mergeSort(a)
    saveExecutionTime('Merge Sort', 'V-kształtne', 'V-ksztaltne', startTime)
print("")


# Merge Sort (A-kształtne)
for a in alisty:
    startTime = datetime.now()
    mergeSort(a)
    saveExecutionTime('Merge Sort', 'A-kształtne', 'A-ksztaltne', startTime)
print("")


# Merge Sort (dane stałe)
for a in constlisty:
    startTime = datetime.now()
    mergeSort(a)
    saveExecutionTime('Merge Sort', 'Stałe', 'Stale', startTime)
print("")






print("HeapSort")

clear()

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
    saveExecutionTime('Heap Sort', 'Posortowane losowo', 'Losowe', startTime)
print("")

# HeapSort (posortowane rosnąco dane)
for a in ascendinglisty:
    startTime = datetime.now()
    heapSort(a)
    saveExecutionTime('Heap Sort', 'Posortowane rosnąco', 'Rosnace', startTime)
print("")

# HeapSort (posortowane malejaco dane)
for a in descendinglisty:
    startTime = datetime.now()
    heapSort(a)
    saveExecutionTime('Heap Sort', 'Posortowane malejąco', 'Malejace', startTime)
print("")

# HeapSort (V-kształtne)
for a in vlisty:
    startTime = datetime.now()
    heapSort(a)
    saveExecutionTime('Heap Sort', 'V-kształtne', 'V-ksztaltne', startTime)
print("")

# HeapSort (A-kształtne)
for a in alisty:
    startTime = datetime.now()
    heapSort(a)
    saveExecutionTime('Heap Sort', 'A-kształtne', 'A-ksztaltne', startTime)
print("")

# HeapSort (dane stałe)
for a in constlisty:
    startTime = datetime.now()
    heapSort(a)
    saveExecutionTime('Heap Sort', 'Stałe', 'Stale', startTime)
print("")






print("ShellSort")

clear()

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
    saveExecutionTime('Shell Sort', 'Posortowane losowo', 'Losowe', startTime)
print("")

# ShellSort (posortowane rosnąco dane)
for a in ascendinglisty:
    startTime = datetime.now()
    shellSort(a)
    saveExecutionTime('Shell Sort', 'Posortowane rosnąco', 'Rosnace', startTime)
print("")

# ShellSort (posortowane malejaco dane)
for a in descendinglisty:
    startTime = datetime.now()
    shellSort(a)
    saveExecutionTime('Shell Sort', 'Posortowane malejąco', 'Malejace', startTime)
print("")

# ShellSort (V-kształtne)
for a in vlisty:
    startTime = datetime.now()
    shellSort(a)
    saveExecutionTime('Shell Sort', 'V-kształtne', 'V-ksztaltne', startTime)
print("")

# ShellSort (A-kształtne)
for a in alisty:
    startTime = datetime.now()
    shellSort(a)
    saveExecutionTime('Shell Sort', 'A-kształtne', 'A-ksztaltne', startTime)
print("")

# ShellSort (dane stałe)
for a in constlisty:
    startTime = datetime.now()
    shellSort(a)
    saveExecutionTime('Shell Sort', 'Stałe', 'Stale', startTime)
print("")


# wypisuje jak długo wykonywał się program
print("Calosc zajela: ", datetime.now() - startTimeFull)
