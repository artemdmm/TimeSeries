import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy

#Сигнал
duration = 5
sample_rate = 4100
num_points = duration*sample_rate
time_points = np.linspace(0, duration, num_points)
white_noise_base = np.random.normal(0,1,size=num_points)
values = 10*np.sin(4*time_points*np.pi)
values_noise = values + white_noise_base

fig, axs = plt.subplots(3, 1, figsize=(20, 10))
fig.suptitle('Сигналы', fontsize=19, fontweight='bold')
labels = ["гауссовский белый шум", "Чистый сигнал", "Зашумленный сигнал"]
c0 = axs[0].plot(time_points, white_noise_base, color="red")
axs[0].set_xlabel('Время')
axs[0].set_ylabel('Амплитуда')
c1 = axs[1].plot(time_points, values, color="green")
axs[1].set_xlabel('Время')
axs[1].set_ylabel('Амплитуда')
c2 = axs[2].plot(time_points, values_noise, color="green")
axs[2].set_xlabel('Время')
axs[2].set_ylabel('Амплитуда')
fig.legend([c0, c1, c2],labels=labels,loc='upper left',borderaxespad=0.1)
