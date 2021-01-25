
## Resolvi o desafio em 3 passos:

    1- Preechi o dicionário inserindo cada email da lista como chave, e seu valor 
    como sendo o valor da parte inteira da divisão entre o "valor total da compra" 
    pela "quantidade de pessoas", através do operador "//".

    2- Em seguida obti o valor restante (N), também por meio da divisão entre o 
    "valor total da compra" pela "quantidade de pessoas", através do operador "%".
    Tendo esse o valor restante, ainda é preciso distribuir de forma mais igual 
    possível entre as pessoas da lista de emails.

    3- Então, percorri novamente com um loop, cuja parada vai até N (valor restante),
    adicionando mais um (+1) ao valor do dicionário, pois basta adicionar o valor 
    atual do dicionário +1 para que a divisão que resultaria em uma dízima infinita, 
    por exemplo, fique justa.


#### Foi utilizado Python 3.9.0 para resolver o Desafio, então executá-lo é necessário instalá-lo nessa versão. 

## Para executar o Desafio, estando no diretório do projeto basta rodar o comando:

```shell script
  python main.py
```

## Para AVALIAÇÃO do desafio basta mudar pelas listas geradas, as variáveis "items" e "emails" no arquivo main.py




    
