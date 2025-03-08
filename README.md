# Criptografia de Arquivos

Este projeto é uma aplicação em Python que permite criptografar e descriptografar arquivos utilizando a biblioteca `cryptography`. A interface gráfica foi desenvolvida com `tkinter`.

## 📌 Funcionalidades

- Selecionar um arquivo do sistema
- Criptografar o arquivo selecionado
- Descriptografar um arquivo criptografado
- Gerar e armazenar automaticamente a chave de criptografia

## 🛠 Tecnologias Utilizadas

- Python 3
- Tkinter (interface gráfica)
- Cryptography (criptografia de arquivos)

## 🚀 Como Usar

### 1. Instalar Dependências

Antes de executar o programa, instale as dependências necessárias:

```bash
pip install cryptography
```

### 2. Executar o Programa

Salve o código em um arquivo `.py` e execute:

```bash
python nome_do_arquivo.py
```

### 3. Uso

1. Abra o programa.
2. Clique no botão "Selecionar Arquivo" e escolha um arquivo.
3. Clique em "Criptografar" para proteger o arquivo.
4. Para recuperar o arquivo original, selecione o arquivo criptografado e clique em "Descriptografar".

## 🔑 Sobre a Chave de Criptografia

O programa gera automaticamente uma chave e a armazena no arquivo `chave.key`. Essa chave é necessária para descriptografar arquivos criptografados. Se esse arquivo for perdido, não será possível recuperar os dados.

## ⚠️ Observações

- O arquivo criptografado terá a extensão `.enc`.
- Apenas arquivos criptografados por este programa podem ser descriptografados com a chave correspondente.
- O programa impede a criptografia de arquivos já criptografados.

## 📜 Licença

Este projeto está disponível sob a licença MIT.
