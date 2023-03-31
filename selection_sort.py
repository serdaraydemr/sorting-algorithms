# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:13:11 2023

@author: serdar
"""
"""
Selection Sort, listenin en küçük elemanını bulup, listenin başındaki elemanla yer değiştirdikten sonra 
diğer elemanları da sırayla gezerek listenin tamamını sıralayan bir sıralama algoritmasıdır. 
Algoritma, elemanların küçükten büyüğe veya büyükten küçüğe doğru sıralanmasını sağlar.

Selection Sort, bubble sorta benzer şekilde basit ve anlaşılır bir sıralama algoritmasıdır. 
Ancak, bubble sorttan farklı olarak, en küçük elemanı bulup listeye eklemesi sayesinde, 
ortalama durumda O(n^2) karmaşıklığına sahip olsa da, en kötü durumda da O(n^2) karmaşıklığına sahiptir.

!!!!! 
O(n^2) karmaşıklığına sahiptir:   
Sıralanacak listenin eleman sayısının karesine bağlı olarak çalışma süresinin arttığı anlamına gelir.
!!!!!


Selection Sort, küçük veri setleri üzerinde oldukça etkilidir. 
Bununla birlikte, büyük veri setleri üzerinde performansı oldukça kötüdür 
ve tercih edilecek daha verimli sıralama algoritmaları mevcuttur. 
Ayrıca, algoritmanın her iterasyonunda bir elemanın yer değiştirmesi gerektiğinden, 
swap işlemi maliyetli olduğu zamanlarda tercih edilmeyebilir. 
Bununla birlikte, özellikle öğrenme amaçlı veya sıralama öncesi bir ön işlem olarak kullanılabilir.
"""

# Örnek 1 

def selection_sort(arr):
    
    n = len(arr) # dizinin boyutunu al 
    for i in range (n): # dizinin tüm elemanlarına dngü ile eriş 
        min_index = i # dizinin i. elemanını minimum kabul et 
        for j in range (i+1,n): # dizinin i+1. elemanından son elemanına kadar dçngü ile eriş 
            if arr[j] < arr[min_index]: # eğer j. eleman i. elemandan küçükse
                min_index = j # j. elemanı minumum olarak kabul et 
        arr[i], arr[min_index] = arr[min_index],arr[i] # minimum elemanı dizinin başına al
    return arr # seıralanmış diziyi döndür

arr = [22,10,3,98,99,45,82,12,5,49]
print(selection_sort(arr))
# çıktı : [3, 5, 10, 12, 22, 45, 49, 82, 98, 99]

# örnek 2 

A = [] # boş A dizisi oluşturulur.
N = int(input("Dizinin Elaman sayısını Giriniz : ")) #C kullanıcıdan dizi boyutu istenir

for i in range (N): # girilen dizi boyutu kez döngü çalıştırılır. ve her seferinde kullanıcıdan bir sayı alınarak A dizisine eklenir
    print("A(%d) = "%(i+1),end="") 
    A.append(int(input()))
for i in range (N-1): # Selection sort algoritmasının ilk döngüsü başlar. N-1. elemana kadar kapsar.
    for j in range(i+1,N): # ikinci döngü, birinci döngünün elamanından sonraki tüm elamanları kapsar
        if (A[j]<A[i]): # Eğer bir sonraki eleman bir önceki elemandan küçükse bu iki elemanın yeri dğeiştirilir.
            g = A[i]
            A[i] = A[j]
            A[j] = g
print("\nSıralı Dizi \n ========")
for i in range (N): # Sıralanış diziyi ekrana yazdır.
    print("A(%d) = %d"%(i+1,A[i]))
    
    
    
