
from typing import Sized
import requests


def main():
    print('###Retorno de informações de CEP###')
    valida_cep = False
    repetidor = 's'    
    while valida_cep == False:
        cep_input = input('Digite o cep com 8 dígitos sem letras e traços! ')
        try:
            cep_input=int(cep_input)                            
            
            valida_cep=True    
        except:
            print("Formato do CEP inválido, tente novamente.", cep_input)
    
    request = requests.get(
        'https://viacep.com.br/ws/{}/json/'.format(cep_input))

    result_api = request.json()

    MenInicial = int(input('O que você deseja saber?\n1. Nome da rua, cidade e UF\n2. DDD do CEP\n3. Código do IBGE\n4. Todas informações possíveis\n'))

    if MenInicial == 1:
        
        if 'erro' not in result_api:
            print('CEP:', result_api['cep'], '\nLogradouro:', result_api['logradouro'], '\nBairro:',
              result_api['bairro'], '\nCidade:', result_api['localidade'], '\nUF:', result_api['uf'])
        else:
            print('{}: cep inválido!'.format(cep_input))
    elif MenInicial == 2:
        if 'erro' not in result_api:
            print('CEP:', result_api['cep'], '\nDDD:', result_api['ddd'])
        else:
            print('{}: cep inválido!'.format(cep_input))        
    elif MenInicial == 3:
        if 'erro' not in result_api:
            print('CEP:', result_api['cep'], 'IBGE', result_api['ibge'])
        else:
            print('{}: cep inválido!'.format(cep_input))
    elif MenInicial ==4:
        if 'erro' not in result_api:
            print(result_api)
        else:
            print('{}: cep inválido!'.format(cep_input))           
    else:
        print('Digite uma Opção válida!')
        main()

    option = int(input('Desjea realizar uma nova consulta?\n1. Sim\n2. Sair\n'))
    if option == 1:
        main()
    else:
        exit()


if __name__ == '__main__':
    main()
