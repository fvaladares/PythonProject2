# Fundamentos de Python: Aplicações em Internet das Coisas (IoT)

UniBH -- Capus Estoril, professor Fabrício Valadares.


Este repositório contém uma série de quatro exercícios práticos de nivelamento em Python. O projeto utiliza o contexto de uma Casa Inteligente (Smart Home) para aplicar conceitos progressivos de programação, evoluindo de estruturas de controle e repetição até a Orientação a Objetos.

O projeto conta com um menu interativo em console para a execução isolada de cada um dos cenários de teste.

## 🛠️ Tecnologias e Pré-requisitos

* **Python 3.10 ou superior:** Obrigatório devido ao uso da estrutura estrutural de repetição (`match/case`) no menu principal.
* Recomendado o uso de IDEs como **PyCharm** ou VS Code para execução e análise do código.

## 🗂️ Estrutura do Projeto

O código está modularizado para facilitar o estudo e a manutenção. A execução principal ocorre através do arquivo `main.py`, que atua como um controlador, importando a lógica das questões.

* `main.py`: Arquivo principal contendo o loop de execução e o menu interativo.
* `Questao1.py`: Lógica de variáveis e estruturas condicionais.
* `Questao2.py`: Lógica de laços de repetição e criação de funções.
* `Questao3.py`: Implementação do modelo da classe `LuminariaSmart` (Orientação a Objetos).
* `Questao4.py`: Implementação das classes `HubCentral` e `DispositivoIoT` (Integração de POO e coleções).

## 🚀 Cenários Práticos (Questões)

### 1. Aquecimento (Controle de Acesso)
Simula a verificação de permissões de uma fechadura eletrônica usando variáveis e estruturas condicionais (`if/else`). 

### 2. Intermediário (Processamento de Logs)
Analisa um conjunto de leituras simuladas de um sensor de clima. Utiliza laços de repetição (`for`) e funções para calcular médias e identificar alertas de temperatura.

### 3. Avançado (Orientação a Objetos)
Modelagem de uma luminária inteligente. Demonstra a criação de classes, métodos de instância, encapsulamento de estado (ligado/desligado) e validação de atributos (intensidade de luz de 0 a 100%).

### 4. Desafio de Integração (Hub Central)
Simula um painel de controle que gerencia múltiplos dispositivos IoT na rede. Explora a interação entre múltiplos objetos, armazenamento em listas e iteração de coleções para emitir um relatório de equipamentos com bateria baixa.

## ⚙️ Como executar

1. Clone este repositório para a sua máquina local:
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   
