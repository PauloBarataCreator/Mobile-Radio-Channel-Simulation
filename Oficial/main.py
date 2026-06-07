from binary_number import rand_key
from noise_awgn import noise
from numpy import sqrt
import random

# Cria código binário - Limiar
N = 3 # number of bits or symbols 10^6
binary_input = rand_key(N)
binary_input_em_lista = [int(i) for i in list(binary_input)]

# Bpsk modulation
modulated_sgn = []
for i in binary_input:
    if i == "1":
        modulated_sgn.append(1)
    elif i=="0":
        modulated_sgn.append(-1)

# Adicionando Ruído AWGN
sgn_awgn = []

for i,j in zip(modulated_sgn, noise()):
    sgn_awgn.append(i + j)

# Rayleigh fading plus Noise
sgn_ray_awgn=[]
for i,j in zip(modulated_sgn, noise()):
    ch_coeff = sqrt(random.gauss(0,1)**2+random.gauss(0,1)**2)/sqrt(2)
    sgn_ray_awgn.append(i*ch_coeff +j)

# Correção e estimação
estimation=[]
for rx in sgn_ray_awgn:
    # Correlação
    c1 = 1*rx
    c2 = -1*rx
    # Estimação
    if c1>c2:
        estimation.append(1)
    else:
        estimation.append(0)

# Decisão
error=0 # This is no for no/ N
for i,j in zip(estimation,binary_input_em_lista):
    if i!=j:
        error = error + 1


# Calcula perro (ber)
perro = error/len(binary_input_em_lista)

# Eb/No


print(binary_input_em_lista)
print(modulated_sgn)
print(sgn_awgn)
print(sgn_ray_awgn)
print(estimation)
print(error)
