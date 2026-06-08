
from interface import *
import time
from pathlib import Path
import matplotlib.pyplot as plt
import os

#Simula
def transmission(limiar, resultados):

    Eb_No = 0
    while Eb_No < 10:

            i = 0

            binary_code = gera_codigo_binario(limiar)

            modulated_sgn_tx = modula_sgn(binary_code)

            # Add AWGN noise
            sgn_awgn = add_ruido_awgn(modulated_sgn_tx, Eb_No, np.random.default_rng(2026))

            # Add Rayleigh Fading plus AWGN noise
            sgn_ray_awgn = add_rayleigh_plus_awgn(modulated_sgn_tx, Eb_No, np.random.default_rng(2026))

            # Estimation

            ## AWGN
            estimation_awgn = correlation_estimation(sgn_awgn)
            i += limiar
            ## Rayleigh
            estimation_ray_awgn = correlation_estimation(sgn_ray_awgn)

            # Decision error

            # Error AWGN
            error_awgn = error_decisao(estimation_awgn, binary_code)

            # Error Rayleigh plus AWGN
            error_ray_awgn = error_decisao(estimation_ray_awgn, binary_code)

            # Perro

            # Perro AWGN
            perro_awgn = perro(error_awgn, binary_code)

            # Perro Rayleigh plus AWGN
            perro_ray_awgn = perro(error_ray_awgn, binary_code)

            # print(perro_ray_awgn)
            Eb_No+=1


            resultados.append(
                {
                    "Eb_No": float(Eb_No),
                    "bits_simulados": float(i),
                    "BER_AWGN": perro_awgn,
                    "BER_Rayleigh_AWGN": perro_ray_awgn,
                }
            )
            
            # print(resultados)
            time.sleep(0.01)

    
    # Salvando o resultado gráfico em imagem
    cwd = os.getcwd()
    path_store = Path(cwd+"\\output.png")
    gera_grafico(resultados,path_store)

    return resultados

def gera_grafico(resultados, caminho_png):
    # Gera um grafico BER x Eb/No

    eb_no = [linha["Eb_No"] for linha in resultados]

    plt.figure(figsize=(9, 6))
    plt.semilogy(eb_no, [linha["BER_AWGN"] for linha in resultados], "o-", label="AWGN")
    plt.semilogy(
        eb_no,
        [linha["BER_Rayleigh_AWGN"] for linha in resultados],
        "s-",
        label="Rayleigh plus AWGN",
    )

    plt.grid(True, which="both", linestyle=":")
    plt.xlabel("Eb/No (dB)")
    plt.ylabel("BER / Perro")
    plt.title("Mobile Radio Channel Simulation")
    plt.legend()
    plt.tight_layout()

    caminho_png.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(caminho_png, dpi=160)
    plt.close()

def mostrar_resultados(resultados):
   # Apenas mostrar os resultados obtidos
    print("Eb/No(dB) | BER AWGN | BER Rayleigh plus AWGN")
    print("-" * 86)

    for linha in resultados:
        print(
            f"{linha['Eb_No']:8.0f} | "
            f"{linha['BER_AWGN']:.6e} | "
            f"{linha['BER_Rayleigh_AWGN']:.6e}       | "
        )

# Para rodar todo projeto por aqui
# resultados = []
# resultados = transmission(200000)

# import os
# cwd = os.getcwd()
# path_store = Path(cwd+"\\output.png")
# print(cwd+"\\output.png")


# gera_grafico(resultados,path_store)

# mostrar_resultados(resultados)