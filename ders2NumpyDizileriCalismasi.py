import numpy as np

result=np.array([1,2,3,4,66,5]) #belirlenen elemanlar ile numpy dizisi olusturuldu
result2=np.arange(1,10) #1-10 arasi elemanlarla dizi olusturuldu.
result3=np.zeros(10) #10 tane sifir iceren numpy dizisi olusturuldu.
result4=np.ones(5) #5 tane 1 iceren numpy dizisi olusturuldu.
result5=np.linspace(0,100,5) #0-100 arasini 5 parcaya bolerek dizi olusturuldu.
result6=np.random.randint(0,11) #0-11 arasi rastgele bir sayi olusturdu.
result7=np.random.randn(5) #negatif de dahil olmak uzere (-1)-1 arasi dizi olusturuldu.
npArray=np.arange(15) #0-15 arasi elemanlar ile dizi olusturuldu.
result8=npArray.reshape(3,5) #ustteki dizi 3x5 matris haline getirildi.
print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result8.sum(axis=0)) #sutunları toplar
print(result8.sum(axis=1)) #satirlari toplar