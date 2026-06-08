from binary_number import rand_key
from numpy import sqrt
import random
import math 
import numpy as np

def gera_codigo_binario(limiar):
    # Cria código binário - Limiar
    N = limiar # number of bits or symbols 10^6
    binary_input = rand_key(N)
    binary_input_em_lista = [int(i) for i in list(binary_input)]

    return binary_input_em_lista

def modula_sgn(binary_input_em_lista):   
    # Bpsk modulation
    modulated_sgn = []
    for i in binary_input_em_lista:
        if i == 1:
            modulated_sgn.append(1)
        elif i==0:
            modulated_sgn.append(-1)
    return modulated_sgn

def noise_distribution(Eb_No, tamanho, rng: np.random.Generator):
    # De acordo com Eb/No gera um ruído AWGN

    # Lineariza o Eb/No
    Eb_No_linear = 10.0 ** (Eb_No / 10.0)

    # Energia para q bit de BPSK, inverso de Eb_No.
    n0 = 1.0 / Eb_No_linear

    # Extrai a variância do ruído a partir de n0/2.
    variance = math.sqrt(n0 / 2.0)

    # Ruido branco AWGN com distruição gaussiana.
    noise = rng.normal(loc=0.0, scale=variance, size=tamanho)

    return noise

def add_ruido_awgn(modulated_sgn, Eb_No, rng):
    # Adiciona ruído branco AWGN ao sinal recebido.
    noise = noise_distribution(Eb_No, len(modulated_sgn), rng)
    sgn_awgn = modulated_sgn + noise
    return sgn_awgn

def add_rayleigh_plus_awgn(modulated_sgn, eb_no, rng):

    sgn_awgn = noise_distribution(eb_no, len(modulated_sgn), rng)

    # Rayleigh fading plus Noise
    sgn_ray_awgn=[]
    for i,j in zip(modulated_sgn, sgn_awgn):
        ch_coeff = sqrt(random.gauss(0,1)**2+random.gauss(0,1)**2)/sqrt(2)
        sgn_ray_awgn.append(i*ch_coeff +j)
    return sgn_ray_awgn

def correlation_estimation(sgn_ray_awgn):
    # Correlação e estimação
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
    
    return estimation

def error_decisao(estimation,binary_input_em_lista):
    # Decisão
    error=0 # This is no for no/ N
    for i,j in zip(estimation,binary_input_em_lista):
        if i!=j:
            error = error + 1
    
    return error

def perro(error, binary_input_em_lista):
    # Calcula perro (ber)
    perro = error/len(binary_input_em_lista)
    return perro



