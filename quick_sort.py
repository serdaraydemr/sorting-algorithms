# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:13:35 2023

@author: serdar
"""
"""
Quick Sort, bir dizi elemanını parçalara ayırarak ve her parçayı ayrı ayrı sıralayarak, 
sonunda tüm parçaları birleştirerek sıralama yapan bir sıralama algoritmasıdır. 
Bu parçalar, bir pivot elemanı seçilerek oluşturulur. 
Pivot elemanından küçük olanlar sol tarafa, büyük olanlar ise sağ tarafa yerleştirilir. 
Bu işlem bölünmüş olan parçalar için de tekrarlanır ve sonunda parçalar birleştirilerek sıralanmış dizi elde edilir.

Quick Sort, en hızlı sıralama algoritmalarından biridir ve ortalama durumda O(n log n) karmaşıklığına sahiptir. 
Ancak, en kötü durumda O(n^2) karmaşıklığına da sahiptir. 
Algoritma, özellikle büyük veri setleri üzerinde oldukça etkilidir.


Quick Sort, sıralama işlemini in-place olarak gerçekleştirdiği için, ekstra bellek kullanımı yapmadan sıralama yapabilir. 
Ayrıca, algoritma, veri setindeki elemanların birbirine çok yakın olmadığı durumlarda oldukça hızlı çalışır.
Ancak, pivot elemanının seçimi, algoritmanın performansını önemli ölçüde etkiler. 
Pivot elemanı, dizi elemanları arasında rastgele bir şekilde seçilebilir veya belirli bir stratejiye göre seçilebilir. 
Bu seçim, algoritmanın performansı üzerinde önemli bir etkiye sahip olabilir.
 
Quick Sort, genellikle büyük veri setleri üzerinde sıralama işlemlerinde kullanılır. 
Ayrıca, diğer sıralama algoritmaları tarafından sıralanamayan özel veri tipleri üzerinde de kullanılabilir. 
Ancak, veri seti nispeten küçükse ve diğer sıralama algoritmaları da yeterli performansı sağlıyorsa, 
Quick Sort tercih edilmeyebilir.
"""

# örnek 

def quick_sort(arr):
    if len(arr) <= 1: # Eğer dizinin boyutu 1 veya daha azsa, zaten sıralıdır.
        return arr
    else:
        pivot = arr[0] # Pivot olarak ilk elemanı seçiyoruz.
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i]) # Pivot'tan küçük olan elemanları sol tarafa ekliyoruz.
            else:
                right.append(arr[i]) # Pivot'tan büyük veya eşit olan elemanları sağ tarafa ekliyoruz.
        return quick_sort(left) + [pivot] + quick_sort(right) # Sol ve sağ tarafı rekürsif olarak sıralıyoruz ve pivot ile birleştiriyoruz.

# Örnek kullanım
arr = [5, 2, 9, 1, 5, 6,25,410,2023,25,85,74,46,49,61]
sorted_arr = quick_sort(arr)
print(sorted_arr)
