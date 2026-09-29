class DispositivoIoT:
    def __init__(self, nome, bateria):
        self.nome = nome
        self.bateria = bateria


class HubCentral:
    def __init__(self):
        self.dispositivos_conectados = []

    def adicionar_dispositivo(self, dispositivo):
        self.dispositivos_conectados.append(dispositivo)

    def relatorio_bateria_baixa(self):
        print("--- Relatório de Bateria Baixa ---")
        for dispositivo in self.dispositivos_conectados:
            if dispositivo.bateria < 20:
                print(f"Alerta: {dispositivo.nome} está com apenas {dispositivo.bateria}% de bateria.")


# Instanciando o Hub
hub = HubCentral()

# Criando dispositivos com diferentes níveis de bateria
sensor_janela = DispositivoIoT("Sensor Janela Quarto", 85)
fechadura = DispositivoIoT("Fechadura Entrada", 15)
termostato = DispositivoIoT("Termostato Sala", 8)

# Adicionando ao Hub
hub.adicionar_dispositivo(sensor_janela)
hub.adicionar_dispositivo(fechadura)
hub.adicionar_dispositivo(termostato)

# Gerando o relatório
hub.relatorio_bateria_baixa()