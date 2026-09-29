from calendar import prmonth


def primeira_questao():
    porta_destavada = False
    nivel_acesso = int(input('Informe seu nível de acesso: '))

    if nivel_acesso > 5:
        print('Acesso librado.')
        porta_destavada = False
    else:
        porta_destavada = True
        print('Acesso negado: Permissão insuficiente.')

    def segunda_questao():
        pass


if __name__ == '__main__':
    primeira_questao()