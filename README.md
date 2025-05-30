# Relatórios de Desempenho de Campanhas de Tráfego Pago no Meta

Este projeto é uma aplicação desenvolvida em Streamlit para gerar relatórios de desempenho a partir de arquivos Excel (XLSX) de campanhas de tráfego pago no Meta.

## Funcionalidades Principais

- **Importação de Pacotes:**
  - *Pandas*: Manipulação e análise de dados.
  - *Streamlit*: Criação da interface web interativa.
  - *Jinja2*: Renderização de relatórios personalizados.
  - *Datetime*: Manipulação de datas.
  - *io*: Manipulação de dados de texto em memória.

- **Template do Relatório:**
  - Utiliza Jinja2 para definir o template que irá compor os relatórios de campanhas.

- **Interface do Usuário:**
  - Construída com Streamlit.
  - Título e instruções para upload de arquivos são exibidos no início.
  - Upload de múltiplos arquivos XLSX através de um uploader de arquivos.

- **Processamento de Dados:**
  - Leitura e renomeação de colunas para padronização.
  - Validação para garantir a presença de todas as colunas obrigatórias.
  - Filtragem para incluir apenas os dados dos últimos 7 dias.

- **Geração de Relatórios:**
  - Preenchimento do template Jinja2 com dados das campanhas.
  - Relatórios gerados para cada arquivo são exibidos na interface como text areas.

- **Download dos Relatórios:**
  - Relatórios são concatenados e disponibilizados para download como um único arquivo de texto.

- **Tratamento de Erros:**
  - Exibição de mensagens em caso de colunas faltantes ou erros de leitura nos arquivos.

## Ideal para

Este código é ideal para analistas de marketing que precisam avaliar rapidamente o desempenho recente de suas campanhas por meio de uma interface intuitiva e fácil de usar.

![Interface]
![alt text](image.png)

## Como usar

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/dcampillo05/Automate_Read_Files