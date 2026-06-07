from binary_number import rand_key
from noise_awgn import noise

print(noise())

# Cria código binário
N = 3 # number of bits or symbols 10^6
ip = rand_key(N)


# Bpsk modulation
modulated_sgn = []
for i in ip:
    if i == "1":
        modulated_sgn.append(1)
    elif i=="0":
        modulated_sgn.append(-1)
    # print(i)
print(ip)
print(modulated_sgn)


# Adicionando Ruído AWGN

sgn_awgn = []

print(noise())



for i,j in zip(modulated_sgn, noise()):
    sgn_awgn.append(i + j)

# for i in modulated_sgn:

#     i = i + noise()
#     sgn_awgn.append(i)


print(sgn_awgn)
