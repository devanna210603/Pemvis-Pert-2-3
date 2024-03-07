import matplotlib.pyplot as plt

# Koordinat titik-titik garis pertama
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 1, 5, 4]

# Koordinat titik-titik garis kedua
x2 = [1, 2, 3, 4, 5]
y2 = [5, 4, 3, 2, 1]

# Menggambar garis pertama
plt.plot(x1, y1, label='Garis 1', color='blue')

# Menggambar garis kedua
plt.plot(x2, y2, label='Garis 2', color='red')

# Menampilkan legenda
plt.legend()

# Menentukan judul dan label sumbu
plt.title('Grafik Dua Garis')
plt.xlabel('X')
plt.ylabel('Y')

# Menampilkan plot
plt.grid(True)
plt.show()

# Menampilkan koordinat titik-titik untuk setiap garis
print("Koordinat titik-titik garis pertama:")
for i in range(len(x1)):
   plt.grid(True)
