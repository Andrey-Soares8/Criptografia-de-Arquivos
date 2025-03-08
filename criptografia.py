import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

class AppCriptografia:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Criptografia de Arquivos")
        self.janela.geometry("450x350")
        self.janela.resizable(False, False)
        
        self.chave = self.carregar_ou_gerar_chave()
        self.cipher_suite = Fernet(self.chave)
        
        self.arquivo_selecionado = None
        self.criar_widgets()
    
    def carregar_ou_gerar_chave(self):
        chave_arquivo = "chave.key"
        if os.path.exists(chave_arquivo):
            with open(chave_arquivo, 'rb') as f:
                return f.read()
        else:
            chave = Fernet.generate_key()
            with open(chave_arquivo, 'wb') as f:
                f.write(chave)
            return chave
    
    def criar_widgets(self):
        tk.Label(self.janela, text="Criptografia de Arquivos", font=("Arial", 14, "bold")).pack(pady=10)
        
        self.btn_selecionar = tk.Button(self.janela, text="Selecionar Arquivo", command=self.selecionar_arquivo)
        self.btn_selecionar.pack(pady=10)
        
        self.lbl_arquivo = tk.Label(self.janela, text="Nenhum arquivo selecionado", wraplength=400)
        self.lbl_arquivo.pack(pady=5)
        
        self.btn_criptografar = tk.Button(self.janela, text="Criptografar", command=self.criptografar)
        self.btn_criptografar.pack(pady=10)
        
        self.btn_descriptografar = tk.Button(self.janela, text="Descriptografar", command=self.descriptografar)
        self.btn_descriptografar.pack(pady=10)
    
    def selecionar_arquivo(self):
        self.arquivo_selecionado = filedialog.askopenfilename()
        if self.arquivo_selecionado:
            self.lbl_arquivo.config(text=f"Arquivo: {os.path.basename(self.arquivo_selecionado)}")
    
    def criptografar(self):
        if not self.arquivo_selecionado:
            messagebox.showerror("Erro", "Selecione um arquivo primeiro!")
            return
        
        try:
            with open(self.arquivo_selecionado, 'rb') as arquivo:
                dados = arquivo.read()
            
            dados_criptografados = self.cipher_suite.encrypt(dados)
            nome_arquivo = self.arquivo_selecionado + ".enc"
            
            with open(nome_arquivo, 'wb') as arquivo:
                arquivo.write(dados_criptografados)
                
            messagebox.showinfo("Sucesso", f"Arquivo criptografado salvo como:\n{nome_arquivo}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criptografar: {str(e)}")
    
    def descriptografar(self):
        if not self.arquivo_selecionado:
            messagebox.showerror("Erro", "Selecione um arquivo primeiro!")
            return
        
        try:
            with open(self.arquivo_selecionado, 'rb') as arquivo:
                dados_criptografados = arquivo.read()
            
            dados_descriptografados = self.cipher_suite.decrypt(dados_criptografados)
            nome_arquivo_original = self.arquivo_selecionado.replace(".enc", "")
            
            with open(nome_arquivo_original, 'wb') as arquivo:
                arquivo.write(dados_descriptografados)
                
            messagebox.showinfo("Sucesso", f"Arquivo descriptografado salvo como:\n{nome_arquivo_original}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao descriptografar: {str(e)}")
    
    def executar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = AppCriptografia()
    app.executar()