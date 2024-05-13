import numpy as np

# Numpy => array işlemleri ve matematiksel işlemler yapmak için geliştirilmiş bir kütüphanedir.
#(The Numpy library array operations and Maths operations for the do developed.)

# Array Tanımlama ==> (Array Definition)

my_list = [56,83,92,75]

print(type(my_list))
print(my_list)

print("-"*50)

my_arr = np.array(my_list)

print(type(my_arr))
print(my_arr)

# Sıfırdan array tanımlama ==> (From scratch array definition)
# dtype parametresini belirtirsek eğer o veri tipine özgü  elemanları ekler sadece
#(Dtype parameter if specified data type specific parameter adds)

my_arr2 = np.array([56,132],dtype=int)
print(my_arr2)
print(type(my_arr2))

# sadece 0 ve 1'lerden oluşan matris ==> (Only zero and from ones matrix formed)

my_arr3 = np.zeros((5,3))
print(my_arr3)
print(my_arr3.shape)

# Sadece 1'lerden oluşan 5 satır, 3 sütun boyutunda matris ==> (5 rows, 3 columns matrix consisting of only ones)
my_arr4 = np.ones((5,3))
print(my_arr4)
print(my_arr4.shape)

print("-"*50)

#0 ve 1 arasında rastgele sayılardan oluşan 5 satır 3 sütunluk matris
#(A matrix of 5 rows and 3 columns consisting of random numbers between 0 and 1)

print("0 ve 1 arasında rastgele sayılardan oluşan 5 satır 3 sütunluk matris")
print(np.random.rand(5,3))

print("-"*50)

# 5 ve 20 arasında (20 dahil değil) 5 satır 3 sütundan oluşan matris (int tipinde)
#(Matrix between 5 and 20 (20 not included) consisting of 5 rows and 3 columns (int type))

print("5 ve 20 arasında (20 dahil değil) 5 satır 3 sütundan oluşan matris (int tipinde)")
print(np.random.randint(5,20,(5,3)))

print("-"*50)

# -3 ve 4 arasında 2 satır ve 2 sütundan oluşan matris (float tipinde)
#(Matrix consisting of 2 rows and 2 columns between -3 and 4 (float type))

print("-3 ve 4 arasında 2 satır ve 2 sütundan oluşan matris (float tipinde)")
print(np.random.uniform(-3,4,(2,2)))

# Numpy ile matematiksel işlemler ==> (Math operations with Numpy)
# Numpy'ın matematiksel işlemler için kullandığı kendi özellikleri,fonksiyonları vardır
#(Numpy has functions it uses for math)

print("-"*50)

my_arr5 = np.random.randint(1,100,(10))
print(f"array = {my_arr5}")
print(f"ortalama = {np.mean(my_arr5)}")
print(f"toplam = {np.sum(my_arr5)}")
print(f"Çarpı 2 = {my_arr5 * 2}")

# 1 ile 50 arasında rastgele 5 elemandan oluşan 2 matrisin toplamı
#(Sum of 2 matrices consisting of 5 random elements between 1 and 50)

my_arr6 = np.random.randint(1,50,(5))
my_arr7 = np.random.randint(1,50,(5))

print(f"my_arr6 = {my_arr6}")
print(f"my_arr7 = {my_arr7}")

# shape ile ilgili önemli bir fark ==>(One important difference about shape is)
print(my_arr7)
print(my_arr7.shape)
print(my_arr7.ndim)

# shape = (X,) => vektör ==>(Vector)
# shape = (X,1) => matris ==>(Matrix)

my_arr8 = np.reshape(my_arr7,(5,1))

#ndim => n dimension => Kaç boyutlu olduğu bilgisini verir
#ndim==> n dimension => Dimension knowledge gives

print(my_arr8)
print(my_arr8.ndim)

# size => eleman sayısını verir (listedeki len() fonksiyonu gibi)
# size => Workmen the number of gives

print(my_arr8.size)


my_arr9 = np.random.randint(1,100,(8,8))
print(my_arr9)
print(my_arr9.shape)
print(my_arr9.ndim)

# reshape = yeniden boyutlandırma
# reshape = Resizing

# eleman sayısı (size) eğer reshape ile belirtilen satır ve sütun sayısının çarpımına eşit ise o zaman reshape işlemini yapabiliriz
#(If the number of elements (size) is equal to the product of the number of rows and columns specified by reshape, then we can perform the reeshape operation.)

my_arr10 = np.reshape(my_arr9,(4,16))
print(my_arr10)
print(my_arr10.shape)
print(my_arr10.ndim)
