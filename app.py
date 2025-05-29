import pandas as pd
import streamlit as st
from jinja2 import Template
from datetime import datetime, timedelta
import io

# Template do relatório
TEMPLATE = """
Relatório de Desempenho -  {{ Data }}

Anúncio: {{ Anúncio }}
Alcance: {{ Alcance }}
Impressões: {{ Imp }}
Frequência média: {{ Frequência }}
Valor investido: R${{ Gasto }}
Cliques no link: {{ Cliques }}
CTR (taxa de cliques no link): {{ CTR }}%
Conversas iniciadas por mensagem: {{ Resultado }}
Tipo de resultado: {{ TipoResultado }}
Resultados obtidos: {{ TotalResultados }}
Custo por resultado: R${{ CPR }}
"""

st.title("📊 RCL Analytics - Relatório de Campanhas")
st.markdown("Faça o upload de **um ou mais arquivos Excel (.xlsx)** com os dados de campanhas.")

uploaded_files = st.file_uploader("Upload dos arquivos Excel", type=["xlsx"], accept_multiple_files=True)

if uploaded_files:
    # Defina as colunas obrigatórias após o rename
    required_columns = {
        "Data", "Anúncio", "Alcance", "Imp", "Frequência", "Gasto",
        "Cliques", "CTR", "Resultado", "TipoResultado", "TotalResultados", "CPR"
    }

    textInFile = {}

    for file in uploaded_files:
        try:
            df = pd.read_excel(file)
            file_name = file.name
            df.columns = df.columns.str.strip()

            # Mapeamento das colunas do Excel para as colunas usadas no código
            rename_map = {
                "Nome do anúncio": "Anúncio",
                "Dia": "Data",
                "Impressões": "Imp",
                "Valor usado (BRL)": "Gasto",
                "CTR (taxa de cliques no link)" : "CTR",
                "Cliques no link": "Cliques",
                "Conversas por mensagem iniciadas": "Resultado",
                "Tipo de resultado": "TipoResultado",
                "Resultados": "TotalResultados",
                "Custo por resultado": "CPR"
                # Se precisar, adicione mais mapeamentos aqui
            }

            df.rename(columns=rename_map, inplace=True)

            missing_cols = required_columns.difference(df.columns)
            if missing_cols:
                st.error(f"❌ O arquivo '{file_name}' está faltando as colunas: {', '.join(missing_cols)}")
                continue

            # Converte a coluna Data para datetime
            df["Data"] = pd.to_datetime(df["Data"], errors='coerce')
            last_7_days = datetime.today() - timedelta(days=7)
            df_filtered = df[df["Data"] >= last_7_days]

            if df_filtered.empty:
                st.warning(f"⚠️ O arquivo '{file_name}' não possui dados dos últimos 7 dias.")
                continue

            template = Template(TEMPLATE)
            texts = []

            for _, row in df_filtered.iterrows():
                text = template.render(
                    Data=row["Data"].strftime("%d/%m/%Y") if pd.notna(row["Data"]) else "",
                    Anúncio=row["Anúncio"],
                    Alcance=int(row["Alcance"]) if pd.notna(row["Alcance"]) else 0,
                    Imp=int(row["Imp"]) if pd.notna(row["Imp"]) else 0,
                    Frequência=f"{row['Frequência']:.2f}",
                    Gasto=f"{row['Gasto']:.2f}",
                    Cliques=int(row["Cliques"]) if pd.notna(row["Cliques"]) else 0,
                    CTR=f"{row['CTR']:.2f}",
                    Resultado=int(row["Resultado"]) if pd.notna(row["Resultado"]) else 0,
                    TipoResultado=row["TipoResultado"],
                    TotalResultados=int(row["TotalResultados"]) if pd.notna(row["TotalResultados"]) else 0,
                    CPR=f"{row['CPR']:.2f}"
                )
                texts.append(text)

            textUnique = "\n\n".join(texts)
            textInFile[file_name] = textUnique

        except Exception as e:
            st.error(f"❌ Erro ao processar o arquivo '{file.name}': {e}")

    if textInFile:
        buffer = io.StringIO()
        for nome_arquivo, texto in textInFile.items():
            # Gera o campo do resumo
            st.text_area(f"📄 Relatório - {nome_arquivo}", value=texto, height=300)
            buffer.write(f"### {nome_arquivo} ###\n{texto}\n\n")
            

            

        st.download_button(
            label="📥 Baixar todos os relatórios em .txt",
            data=buffer.getvalue(),  # aqui pegamos a string diretamente
            file_name="relatorios_campanhas.txt",
            mime="text/plain"
        )       
