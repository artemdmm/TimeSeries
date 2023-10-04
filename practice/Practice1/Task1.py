import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

#Белый шум
duration = 5
sample_rate = 4100
num_samples = int(duration * sample_rate)
white_noise_g = np.random.normal(loc = 0, scale = 1, size = num_samples)

#Розовый шум
N = len(white_noise_g)
N2 = N//2
print(N)
print(N2)
pink_noise_f = []
for el in white_noise_g:
    s = 0
    for k in range(1,N2):
        s += 1/np.sqrt(k) * np.cos(2*np.pi*k*(el-1)/N)
    s *=2
    s = s + 1 + np.cos(np.pi*(el-1))/np.sqrt(N2)
    pink_noise_f.append(s/N)
    print(len(pink_noise_f))

time_axis = np.linspace(0, duration, len(pink_noise_f))
plt.figure(figsize=(20, 6))
plt.plot(time_axis[:2000], pink_noise_f[:2000])
plt.title('Розовый шум (свертка белого шума)')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.show()
