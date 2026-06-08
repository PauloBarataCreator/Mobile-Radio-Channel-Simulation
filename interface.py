from binary_number import rand_key
from noise_awgn import noise
from numpy import sqrt
import random


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

def add_ruido_awgn(modulated_sgn):
    # Adicionando Ruído AWGN
    sgn_awgn = []
    for i,j in zip(modulated_sgn, noise()):
        sgn_awgn.append(i + j)

    return sgn_awgn

def add_rayleigh_plus_awgn(modulated_sgn, eb_no, rng):

    sgn_awgn = gaussiana_awgn(eb_no, len(modulated_sgn), rng)

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



## Fixing adding
import math 
import numpy as np

def gaussiana_awgn(eb_no_db: float, quantidade: int, rng: np.random.Generator) -> np.ndarray:
    """Gera ruido Gaussiano branco aditivo para um dado Eb/No em dB."""
    eb_no_linear = 10.0 ** (eb_no_db / 10.0)

    # Para BPSK com energia de bit Eb = 1, temos N0 = 1 / (Eb/No).
    n0 = 1.0 / eb_no_linear

    # Em banda base real, a variancia do ruido e N0/2.
    sigma = math.sqrt(n0 / 2.0)

    # O ruido AWGN e modelado por uma variavel aleatoria normal de media zero.
    ruido = rng.normal(loc=0.0, scale=sigma, size=quantidade)
    return ruido

def canal_awgn(tx: np.ndarray, eb_no_db: float, rng: np.random.Generator) -> np.ndarray:
    """Aplica o canal AWGN padrao: sinal recebido = sinal transmitido + ruido."""
    ruido = gaussiana_awgn(eb_no_db, tx.size, rng)
    rx = tx + ruido
    return rx