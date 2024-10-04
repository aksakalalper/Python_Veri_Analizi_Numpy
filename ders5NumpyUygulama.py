import numpy as np
import math as math

#1 (10,15,30,45,60) degerlerine sahip numpy dizisini olusturunuz.
npArray1=([10,15,30,45,60])

#2 (5-15) arasindaki sayilarla numpy dizisi olusturunuz.
npArray2=np.arange(5,15)

#3 (5-100) arasindaki sayilari 5 er 5 er artarak dizi olusturunuz.
npArray3=np.arange(5,100,5)

#4 10 elemanli sifirlardan olusan dizi olusturunuz.
npArray4=np.zeros(10)

#5 (0-100) arasini 5 esit parcaya bolen diziyi yazdiriniz.
npArray5=np.linspace(0,100,5)

#6 (10-30) arasi 5 sayi uretin.
npArray6=np.random.randint(10,30,5)

#7[-1,1] arasi 10 sayi uret
npArray7=np.random.randn(10)

#8 (3x5) noyutlarinda (10-50) arasinda rastgele sayi olsun.
npArray8=np.random.randint(10,50,15)
npArray8New=npArray8.reshape(3,5)
print(npArray8New)
#uretilen matrisin satir ve sutun eleman toplamlarini bulunuz
sumV=npArray8New.sum(axis=1)
sumH=npArray8New.sum(axis=0)
#en buyuk, en kutuk ve eleman ortalamasi nedir?
enBuyuk=npArray8New.max()
enKucuk=npArray8New.min()
print(enBuyuk,enKucuk)
#ortalama=sumV+sumH
#print(ortalama)
print(sumH)
ortalama=npArray8New.mean()
print(ortalama)
#en buyuk degerin indeks numarasi nedir?
indeks=npArray8New.argmax()
print(indeks)
#uretilen matrisin ilk satirini yazdirin.
print(npArray8New[0])
#uretilen matrisin 2.satir 3.elemanini yazdirin.
print(npArray8New[1,2])
#tum satirlardaki ilk elemani seciniz.
print(npArray8New[:,0])
#her elemanin kokunu aliniz
result=npArray8New**2
print(result)