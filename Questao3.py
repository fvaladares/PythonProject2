class LuminariaSmart:
    def __init__(self, id_dispositivo):
        self.id_dispositivo = id_dispositivo
        self.ligada = False
        self.intensidade = 0

    def alternar_estado(self):
        # Inverte o valor booleano atual
        self.ligada = not self.ligada

    def ajustar_intensidade(self, novo_valor):
        # Validação do intervalo


        if 0 <= novo_valor <= 100:
            self.intensidade = novo_valor
        else:
            print("Erro: O valor da intensidade deve estar entre 0 e 100.")


# Instanciando e testando o objeto
minha_luminaria = LuminariaSmart("LUM-SALA-01")

print('-' * 20)
print(f"Dispositivo: {minha_luminaria.id_dispositivo}")
print(f"Ligada: {minha_luminaria.ligada}")
print(f"Intensidade: {minha_luminaria.intensidade}%")
print('-' * 20)

minha_luminaria.alternar_estado()  # Liga a luminária
minha_luminaria.ajustar_intensidade(75)  # Ajusta para 75%

print(f"Dispositivo: {minha_luminaria.id_dispositivo}")
print(f"Ligada: {minha_luminaria.ligada}")
print(f"Intensidade: {minha_luminaria.intensidade}%")