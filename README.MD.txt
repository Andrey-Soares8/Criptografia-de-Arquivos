# Criptografia de Arquivos com Tkinter

## Descrição
Este é um aplicativo desenvolvido em Python usando a biblioteca Tkinter para fornecer uma interface gráfica simples para criptografar e descriptografar arquivos usando a biblioteca `cryptography`.

## Funcionalidades
- Selecionar um arquivo do sistema
- Criptografar o arquivo selecionado e salvar com a extensão `.enc`
- Descriptografar um arquivo criptografado e restaurar seu formato original
- Geração e armazenamento de uma chave de criptografia segura

## Tecnologias Utilizadas
- Python 3
- Tkinter (Interface gráfica)
- Cryptography (Fernet para criptografia segura)

## Instalação
### Pré-requisitos
- Python 3 instalado

### Dependências
Instale as dependências necessárias com:
```sh
pip install cryptography
```

## Como Usar
1. Execute o programa:
   ```sh
   python app.py
   ```
2. Clique em "Selecionar Arquivo" para escolher um arquivo
3. Clique em "Criptografar" para proteger o arquivo
4. Para recuperar o arquivo original, selecione o arquivo criptografado (`.enc`) e clique em "Descriptografar"

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.