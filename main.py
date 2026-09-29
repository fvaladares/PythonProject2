import Questao1 as q1
import Questao2
from Questao3 import LuminariaSmart
from Questao4 import HubCentral, DispositivoIoT # DispositivoIOT poderia estar em outro arquivo.


def menu():
    print('='*22)
    # '{:<25}' left alignment default '{:>25}' right alignment '{:^25}' centered alignment
    saidaFormatada20Caracteres = '|{:<20}|'
    print(saidaFormatada20Caracteres.format(' 1 - Questão 1'))
    print(saidaFormatada20Caracteres.format(' 2 - Questão 2'))
    print(saidaFormatada20Caracteres.format(' 3 - Questão 3'))
    print(saidaFormatada20Caracteres.format(' 4 - Questão 4'))
    print(saidaFormatada20Caracteres.format(' 0 - SAIR '))
    print('=' * 22)

def invocarQuestao3():
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

def invocarQuestao4():
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

if __name__ == '__main__':

    continuar = True
    while continuar:
        menu()
        opcao = input('Opção: ')

        match opcao:
            case '1':
                q1.primeira_questao()

            case '2':
                Questao2.inicializacao()

            case '3':
                invocarQuestao3()

            case '4':
                invocarQuestao4()

            case '0':
                print('Até a próxima 🖖🏽')
                continuar = False

            case _:
                print('😕 A opção informada é inválida, tente novamente.')






