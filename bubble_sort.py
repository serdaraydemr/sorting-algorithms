# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:12:52 2023

@author: serdar
"""

"""
Bubble Sort, iki elemanın yer değiştirmesi gerektiğinde 
bunları birbirleriyle karşılaştırarak sıralama yapan basit bir sıralama algoritmasıdır. 
İki eleman karşılaştırıldığında, eğer birincisi ikincisinden büyükse, yer değiştirilir. 
Bu işlem, dizi elemanlarının tamamı sıralanana kadar tekrarlanır. 
Her iterasyonda en büyük eleman listenin sonuna doğru taşındığından, 
bu algoritmanın en iyi performansı sağlamak için tam olarak 
n elemanlı bir listeyi sıralamak için n-1 iterasyon yapması gerekir.

Bubble Sort, basit ve anlaşılır olmasından dolayı öğrenme amaçlı kullanılabilir. 
Ancak, veri setinin boyutu arttıkça performansı düşer ve daha verimli sıralama algoritmaları tercih edilir. 
Bubble Sort, en iyi durumda O(n), ortalama ve en kötü durumda ise O(n^2) karmaşıklığına sahiptir. 
Bu nedenle, büyük veri setleri veya performans gerektiren uygulamalarda kullanılması önerilmez.

"Karmaşıklığına sahiptir" ifadesi, 
bir algoritmanın çalışma zamanının ne kadar olduğunu veya ne kadar hızlı olduğunu ifade etmektedir. 
"Bubble Sort, en iyi durumda O(n), ortalama ve en kötü durumda ise O(n^2) karmaşıklığına sahiptir" ifadesi ise, 
Bubble Sort algoritmasının en iyi durumda n kadar adımda, 
ortalama ve en kötü durumlarda ise n^2 kadar adımda çalıştığını belirtmektedir. 
Yani, veri setinin boyutu arttıkça, Bubble Sort'un çalışma zamanı daha da artacaktır.
"""

# örnek 1 

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Her iterasyonda en büyük eleman zaten sona gitmiştir
        # Bu yüzden son elemanlar tekrar incelenmez
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # İki eleman yer değiştirilir
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

arr = [2,21,20,69,45,32,61,78,94,15,26]
print(bubble_sort(arr))
# çıktı = [2, 15, 20, 21, 26, 32, 45, 61, 69, 78, 94]


# Örnek 2 : 
    
print("Diziyi [a b c d] şeklinde giriniz : ")
a = [int(i) for i in input().split()] # kullanıcıdan diziyi girmesi istenir ve .split() ile parçalara ayrılarak a'ya eklenir.
n = len(a) # dizinin boyutu hesaplanır ve n değişkeninde tutulur.
for i in range (n):
    for j in range (n-1):
        if a [j+1]<a[j]: # bir sonraki eleman şuanki elemandan küçükse,
            a[j],a[j+1] = a[j+1],a[j] # iki elemanın yerleri değiştirilir.
        
print("\nSıralı Dizi \n ========")
for i in range (n):
    print("%d\t"%a[i], end = "")