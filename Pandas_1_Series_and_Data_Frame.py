import pandas as pd

#Bu haftaki dersimizde pandas kütüphanesinin bize sunmuş olduğu Series ve DataFrame özelliklerini kullanacağız.
#(Series and DataFrame features offered by the Pandas library will be used.)

# 1) Series (Seriler) ==> (Series)
# Seriler, adından da anlaşılacağı gibi seri bir şekilde girilen verilerin
# bir arada tutulmasını ve işlenmesini sağlayan özel bir yapıdır.
# İndeksleme mantığına göre çalışır.
#(It is a special structure that allows serially entered data to be kept together and processed.)

# Numpy'daki array konseptine çok benzer. ==>(Very similar to the array concept in Numpy)
# Tek farkı, buradaki verilerin birer indeksinin olmasıdır.
#(The only difference is that the data here has an index.)

# Pandas kütüphanesi (modülü), Dictionary veri yapısını sıklıkla kullanır.
#(The Pandas library (module), frequently uses the Dictionary data structure.)

# İlk serimizi oluşturalım ==> (First serie)

seri_1 = pd.Series([1,2,3,4,5])
print(seri_1)

print("-"*50)

print(seri_1.index)


seri_2 = pd.Series([175,160,180,182,168],index=['Ahmet','Ali','Ayşe','Mehmet','Yusuf'])

print(seri_2)

seri_2.index = ["Sıra_1","Sıra_2","Sıra_3","Sıra_4","Sıra_5",]
print(seri_2)

#Örnek
# İndeks olarak öğrenci numaralarının son 4 hanesi
# ve değer olarak da vize notlarını içeren bir Seri yazın
# 5 öğrenciyi temsil eden veriler olacak

#(exmample)
#(Write a Series containing the last 4 digits of student numbers as index and visa grades as value)
#(There will be data representing 5 students)

seri_notlar= pd.Series([67,46,75,38,98],index=[3066,3068,3070,3072,3074])
print(seri_notlar)
