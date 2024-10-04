import numpy as np

number1=np.random.randint(10,100,6) #10-100 arasi 6 elemanli dizi olusturuldu.
number2=np.random.randint(10,100,6) #10-100 arasi 6 elemanli dizi olusturuldu.

print(number1)
print(number2)

result=number1+number2 #iki numpy dizisi toplandi.
print(result)

result2=number1+10 #dizinin her elemanina 10 eklendi.
print(result2)

multiArray1=number1.reshape(2,3) #2x3 luk matris olusturuldu.
multiArray2=number2.reshape(2,3) #2x3 luk matris olusturuldu.
print(multiArray1)
print(multiArray2)

result3=np.vstack((multiArray1,multiArray2)) #iki dizi dikey olarak birlestirildi
print(result3)
result3=np.hstack((multiArray1,multiArray2)) #iki dizi dikey olarak birlestirildi
print(result3)

result4=number1>=50 #dizi elemanlari tek tek kontrol edildi.
print(result4)

