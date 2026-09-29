def analisar_temperaturas(lista_temperaturas):
    soma = 0
    alertas_calor = 0

    # Laço para percorrer a lista
    for temp in lista_temperaturas:
        soma += temp
        if temp > 30.0:
            alertas_calor += 1

    # Cálculo da média
    media = soma / len(lista_temperaturas) if len(lista_temperaturas) > 0 else 0

    return media, alertas_calor



if __name__ == '__main__':
    # Testando a função
    leituras_do_dia = [22.5, 25.0, 31.2, 28.4, 19.8, 32.1]
    media_dia, total_alertas = analisar_temperaturas(leituras_do_dia)

    print(f"Média de temperatura: {media_dia:.1f}°C")
    print(f"Quantidade de alertas (acima de 30°C): {total_alertas}")


















#
# import numpy as np
#
# # Criando o array baseado no exemplo anterior
# dados = np.array([10, 20, 30, 40, 50])
#
# # Filtrando os elementos maiores que 30
# maiores_que_30 = dados[dados > 30]
#
# print(maiores_que_30)
# # Saída: [40 50]