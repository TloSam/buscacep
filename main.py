
from typing import Sized
import requests
import re

def main():

    def valida_cep():

        while valida_cep != True:
            cep = input('Digite o cep com 8 dígitos (sem letras e traços!): ')   
            validacao = re.search('^[0-9]{8}$', cep)

            if validacao:      
                validacao = True
                return cep 

            else:
                print("Formato do CEP inválido, tente novamente.\n")
    
    def busca(cep):

        url = f'https://viacep.com.br/ws/{cep}/json/'
        request = requests.get(url)
        result_api = request.json()

        return result_api

    print('###Retorno de informações de CEP###')

    cep = valida_cep()

    result = busca(cep)

    if 'erro' in result:
        print(f'CEP inválido!')
        cep = valida_cep()
        result = busca(cep)

        

    print(
        'O que você deseja saber?',
        '1. Nome da rua, cidade e UF', 
        '2. DDD do CEP', 
        '3. Código do IBGE', 
        '4. Todas informações possíveis', 
        sep='\n')

    menu = True
    while menu:
        opcao = int(input())

        if opcao == 1:
            print(f'''
            CEP: {result['cep']} 
            Logradouro: {result['logradouro']} 
            Bairro: {result['bairro']} 
            Cidade: {result['localidade']} 
            UF: {result['uf']}
            ''')
            menu = False
            
        elif opcao == 2:
            print(f'''
            CEP: {result['cep']} 
            DDD: {result['ddd']}
            ''')
            menu = False

        elif opcao == 3:
            print(f'''
            CEP: {result['cep']} 
            IBGE: {result['ibge']}
            ''')
            menu = False
            
        elif opcao == 4:
            print(f'''
            CEP: {result['cep']} 
            Logradouro: {result['logradouro']} 
            Bairro: {result['bairro']} 
            Cidade: {result['localidade']} 
            UF: {result['uf']}
            IBGE: {result['ibge']}
            GIA: {result['gia']}
            DDD: {result['ddd']}
            SIAFI: {result['siafi']}
            ''')
            menu = False
            
        else:
            print('Digite uma Opção válida!')

    print(
    'Deseja realizar uma nova consulta?',
    '1. Sim',
    '2. Sair', 
    sep='\n')
    nova_consulta = int(input())
    if nova_consulta == 1:
        main()
    else:
        exit()

if __name__ == '__main__':
    main()
