import pyautogui
import pandas as pd
import webbrowser
import time

class LerPlanilha:
    def __init__(self, caminho_arquivo='cadastros_100.xlsx'):
        self.caminho_arquivo = caminho_arquivo

    def carregar_dados(self):
        #Carrega a planilha.
        df = pd.read_excel(self.caminho_arquivo)
        return df.dropna(how='all')

class NavegadorHTML:
    def __init__(self, caminho_html='index.html'):
        self.caminho_html = caminho_html  # Nome padrão do arquivo HTML

    def abrir_HTML(self):
        webbrowser.open(self.caminho_html)
        time.sleep(2)

class AcharImagem:
    def __init__(self, imagem='Imagem/nome.png', timeout=15):
        self.imagem = imagem  # Guardando as funções 
        self.timeout = timeout
    def achar_clicar(self):
        inicio = time.time()
        while time.time() - inicio < self.timeout:
            posicao = pyautogui.locateOnScreen(self.imagem, confidence=0.7)
            if posicao:
                pyautogui.click(pyautogui.center(posicao))
                return
            time.sleep(0.1)
        raise TimeoutError(f'Campo não encontrado: {self.imagem}')

class PreencherFormulario:
    def preencher(self, dados):
        for valor in dados:
            pyautogui.write(str(valor))
            pyautogui.press('tab')
        pyautogui.press('enter')

class AutomatizadorCadastros:
    def __init__(self):
        self.planilha = LerPlanilha()
        self.navegador = NavegadorHTML()
        self.localizador = AcharImagem()
        self.preenchedor = PreencherFormulario()

    def executar(self):
        dados_clientes = self.planilha.carregar_dados()
        self.navegador.abrir_HTML()
        
        for indice, cliente in dados_clientes.iterrows():
            self.localizador.achar_clicar()
            self.preenchedor.preencher(cliente)
            print(f'Cadastro {indice+1}/{len(dados_clientes)} concluído')


if __name__ == '__main__':
    sistema = AutomatizadorCadastros() 
    sistema.executar()