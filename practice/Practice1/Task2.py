import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy

#Белый шум
duration = 5
sample_rate = 4100

kb =  scipy.constants.k
h = scipy.constants.physical_constants['Planck constant'][0]
c = scipy.constants.c
print(kb)
print(h)
print(c)

T = 17*1/np.power(10, 9)  #Температура 17 нанокельвинов
G = 10
coef1 = 2*h/(c*c*T*T*T)
coef2 = h/(kb*T)
freq1 = 1000
num_samples = int(duration * freq1)

#Чёрный шум
for i in range(2):
    black_noise = np.zeros(num_samples)
    time_axis = np.arange(num_samples) / sample_rate

eq = 10 * np.log(coef1*np.power(freq1,3)/(np.exp(coef2*freq1)-1)) + 10
white_noise_g = np.random.normal(loc = 0, scale = 1, size = num_samples)
black_noise = white_noise_g + eq
black_noise /= np.max(np.abs(black_noise))

time_axis = np.linspace(0, duration, len(black_noise))
plt.figure(figsize=(20, 6))
plt.plot(time_axis, black_noise)
plt.title('Черный шум')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.show()
