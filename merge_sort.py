# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:13:48 2023

@author: serdar
"""
"""
Merge Sort, bir dizi elemanını önce ortadan ikiye bölerek, 
ardından her bir parçayı ayrı ayrı sıralayarak ve sonunda parçaları birleştirerek sıralayan bir sıralama algoritmasıdır.
Parçalar, sıralanmış bir şekilde birleştirilir. Bu işlem, her bir parça tek eleman kalmayana kadar tekrarlanır.

Merge Sort, istikrarlı bir sıralama algoritmasıdır ve her zaman O(n log n) karmaşıklığına sahiptir.
Algoritma, büyük veri setleri üzerinde oldukça etkilidir.
Ancak, diğer sıralama algoritmaları gibi in-place olarak gerçekleştirilemez ve ekstra bellek kullanımı gerektirir.

Merge Sort, veri seti boyutundan bağımsız olarak hızlı ve istikrarlı sıralama yapar. 
Ayrıca, diğer sıralama algoritmalarının aksine, en kötü durumda bile O(n log n) karmaşıklığına sahiptir.
Bu nedenle, büyük veri setleri üzerinde sıralama yaparken Merge Sort tercih edilebilir.

Merge Sort, ayrıca, dizi elemanları arasında karşılaştırma işlemi yaparak sıralama yaptığı için, 
özellikle karşılaştırılabilir veri tipleri üzerinde kullanılır.
Bununla birlikte, veri seti nispeten küçükse ve diğer sıralama algoritmaları da yeterli performansı sağlıyorsa,
Merge Sort tercih edilmeyebilir.
"""

def merge_sort(arr):
    # Eğer dizi 1 ya da daha az elemana sahipse sıralanmış olarak kabul edilir.
    if len(arr) <= 1:
        return arr
    
    # Diziyi ortadan ikiye bölmek için orta nokta hesaplanır.
    middle = len(arr) // 2
    
    # Dizinin sol yarısı için merge_sort fonksiyonu tekrar çağrılır.
    left_half = merge_sort(arr[:middle])
    
    # Dizinin sağ yarısı için merge_sort fonksiyonu tekrar çağrılır.
    right_half = merge_sort(arr[middle:])
    
    # İki yarıyı birleştirmek için merge fonksiyonu çağrılır.
    return merge(left_half, right_half)

def merge(left, right):
    # İki yarının birleştirilmesi için kullanılacak yeni bir boş liste oluşturulur.
    result = []
    
    # Sol ve sağ yarılar için, elemanlar karşılaştırılır ve küçük olan önce yeni listeye eklenir.
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    
    # Sol yarıdaki elemanlar bitene kadar yeni listeye eklemeye devam edilir.
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    
    # Sağ yarıdaki elemanlar bitene kadar yeni listeye eklemeye devam edilir.
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]
    
    # Yeni oluşturulan listeyi geri döndürürüz.
    return result

arr = [20,1,0,25,98,45,63,25,14,78]
print(merge_sort(arr))