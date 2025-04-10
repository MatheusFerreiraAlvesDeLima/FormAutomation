import customtkinter as ctk
import threading

from auto import AutomatizadorCadastros

class Aplicacao(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Automatização Python')
        self.geometry('300x140')
        self.resizable(False, False)
        self._set_appearance_mode('system')
        self.attributes('-topmost', True)

        self.label = ctk.CTkLabel(self, text='Bem-vindo para o teste do projeto')
        self.label.pack(pady=10)

        self.porcentagem = ctk.CTkLabel(self, text='Progresso: 0%')
        self.porcentagem.pack(pady=2)

        self.progress_bar = ctk.CTkProgressBar(self, width=200)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=5)

        self.button = ctk.CTkButton(self, text='Iniciar teste', command=self.iniciar_auto)
        self.button.pack(pady=5)

    def iniciar_auto(self):
        self.button.pack_forget()  # Esconde o botão ao iniciar

        def executar_com_progresso():
            sistema = AutomatizadorCadastros()
            dados = sistema.planilha.carregar_dados()
            total = len(dados)

            sistema.navegador.abrir_HTML()

            for i, cliente in dados.iterrows():
                sistema.localizador.achar_clicar()
                sistema.preenchedor.preencher(cliente)

                porcentagem = int(((i + 1) / total) * 100)
                progresso = (i + 1) / total

                self.after(0, lambda p=porcentagem: self.porcentagem.configure(text=f'Progresso: {p}%'))
                self.after(0, lambda prog=progresso: self.progress_bar.set(prog))

            self.after(0, self.finalizar_interface)

        threading.Thread(target=executar_com_progresso, daemon=True).start()

    def finalizar_interface(self):
        self.label.configure(text='Cadastros finalizados!')
        self.porcentagem.configure(text='Progresso: 100%')
        self.progress_bar.set(1)

        self.button = ctk.CTkButton(self, text='Finalizar', command=self.destroy)
        self.button.pack(pady=5)

if __name__ == '__main__':
    app = Aplicacao()
    app.mainloop()
