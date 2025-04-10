# Automatizador de Cadastros

Um projeto em Python que automatiza o preenchimento de formulários HTML utilizando dados obtidos de uma planilha Excel. A automação é feita com o auxílio de **pyautogui** para interação com a tela e **pandas** para manipulação dos dados, enquanto uma interface gráfica (GUI) construída com **customtkinter** exibe o progresso da operação.

## Funcionalidades

- **Carregamento de Dados**:  
  Lê os dados de uma planilha Excel (arquivo `cadastros_100.xlsx`), removendo linhas vazias, para obter os registros que serão utilizados.

- **Automatização do Formulário**:  
  - Abre um arquivo HTML (`index.html`) em um navegador padrão.
  - Utiliza **pyautogui** para localizar elementos na tela (através de imagens) e simular cliques e digitação para preencher os formulários automaticamente.

- **Interface Gráfica**:  
  Uma aplicação GUI construída com **customtkinter** para acompanhar o progresso dos cadastros, com:
  - Barra de progresso que indica o percentual de finalização.
  - Mensagens de status e botão de finalização.
  
- **Execução Paralela**:  
  A automação é realizada em uma thread separada, permitindo que a interface permaneça responsiva durante o processo.

## Tecnologias Utilizadas

- **Python**
- **Pandas**: Para manipulação dos dados da planilha.
- **PyAutoGUI**: Para automação de interação com a tela (cliques, digitação).
- **Webbrowser e Time**: Para abrir o HTML e controlar os tempos de espera.
- **CustomTkinter**: Para criação de uma interface gráfica moderna e funcional.

## Pré-requisitos

- Ter o Python 3.x instalado.
- Instalar as seguintes bibliotecas, preferencialmente em um ambiente virtual:
  - pandas
  - pyautogui
  - customtkinter
  
Você pode instalá-las via `pip`:
bash
pip install pandas pyautogui customtkinter

