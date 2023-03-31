# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:13:21 2023

@author: serdar
"""
"""
Insertion Sort, bir dizi elemanı tek tek tarayarak, 
sıradaki elemanı doğru konuma yerleştirerek sıralayan bir sıralama algoritmasıdır. 
Listenin bir kısmı sıralı hale getirilirken, diğer elemanlar sırayla alınarak doğru konuma yerleştirilir. 
Algoritma, özellikle küçük veri setleri üzerinde oldukça etkilidir.

Insertion Sort, veri seti küçük olduğunda, diğer sıralama algoritmalarına kıyasla oldukça hızlıdır. 
Ayrıca, dizi neredeyse sıralı ise, yani dizi elemanları zaten neredeyse doğru konumda ise, 
bu algoritmanın performansı oldukça iyi olacaktır. 
Bu nedenle, sıralanacak veri setinin boyutu küçük olduğunda veya veri seti neredeyse sıralı ise, 
Insertion Sort tercih edilebilir.

Insertion Sort, özellikle veri seti nispeten küçük olduğunda, 
aynı zamanda sıralama işlemi sırasında listeyi değiştirmek istemediğiniz zamanlarda da kullanılabilir.
Bu algoritma, en iyi durumda O(n) karmaşıklığına sahipken, ortalama ve en kötü durumda O(n^2) karmaşıklığına sahiptir.

en iyi durum : verilerin zaten sıralı olduğu durumda algoritmanın çalışma zamanını gösterir. O(n) -> dizinin elaman sayısına bağlıdır.
ortalama durum : verilerin rastgele sıralı olduğu durumlarda algoritmanın performansını ifade eder.
en kötü durumda : sıralı değil veya ters  sıralı olduğu durumlarda algoritmanın performansını ifade eder.
"""

# örnek 1 : 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i] # listenin sonraki elemanını kaydediyoruz
        j = i - 1 # geçerli pozisyondan bir önceki pozisyonu kaydediyoruz
        while j >= 0 and arr[j] > key_item: # listenin önceki elemanlarını tarayarak key_item'dan daha büyük olanları kaydırıyoruz
            arr[j + 1] = arr[j] # bir sonraki pozisyona kaydırıyoruz
            j -= 1 # bir önceki pozisyona geri gidiyoruz
        arr[j + 1] = key_item # doğru pozisyona yerleştiriyoruz
    return arr

arr = [5, 2, 7, 4, 0, 9, 8, 6, 1, 3] # örnek bir liste oluşturuyoruz
print("Sırasız liste: ", arr)
arr = insertion_sort(arr) # insertion sort'u kullanarak listenin elemanlarını sıralıyoruz
print("Sıralı liste: ", arr)


"""
Bu kod, arr adlı bir dizi veya liste alır ve Insertion Sort algoritmasını kullanarak dizi öğelerini sıralar.
Algoritma, listenin ilk elemanını sıralanmış kabul eder ve ikinci elemandan başlayarak geri kalan elemanları sıralamaya ekler.

Insertion Sort'un karmaşıklığı, 
en iyi durumda O(n) (dizi zaten sıralı) ve en kötü durumda O(n^2) (dizi tersten sıralı) olabilir.
"""


# örnek 2 : 

print("Diziyi [a b c d] şeklinde giriniz : ")
a = [int(i) for i in input().split()] # kullanıcıdan diziyi girmesi istenir ve .split() ile parçalara ayrılarak a'ya eklenir.
n = len(a) # dizinin boyutu hesaplanır ve n değişkeninde tutulur.

for i in range (1,n):
    g = a[i]
    j = i-1
    while ((j>-1)&(a[j]>g)):
        a[j+1] = a[j]
        j = j-1
        a[j+1] = g
print("\nSıralı Dizi \n ========")
for i in range (n):
    print("%d\t"%a[i], end = "")