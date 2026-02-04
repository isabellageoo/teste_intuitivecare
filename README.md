# Teste Técnico – Processamento de Dados da ANS

Este projeto foi desenvolvido como parte de um teste técnico com o objetivo de acessar, processar e consolidar dados públicos disponibilizados pela Agência Nacional de Saúde Suplementar (ANS).

O foco do trabalho é o processamento de arquivos de Demonstrações Contábeis e a consolidação de informações relacionadas a despesas com eventos/sinistros dos últimos três trimestres disponíveis.

---

## 🎯 Objetivo do Projeto

- Acessar os dados abertos da ANS
- Identificar e baixar os arquivos dos últimos 3 trimestres disponíveis
- Extrair automaticamente os arquivos compactados (ZIP)
- Processar os dados contábeis
- Consolidar as informações em um único arquivo CSV
- Compactar o resultado final em um arquivo ZIP

---

## 📁 Estrutura do Projeto

.
├── data
│ ├── raw
│ │ ├── 2T2024
│ │ ├── 3T2024
│ │ ├── 4T2024
│ │ └── arquivos .zip originais
│ └── output
│ ├── consolidado_despesas.csv
│ └── consolidado_despesas.zip
├── src
│ ├── download_ans.py
│ └── processar_dados.py
├── requirements.txt
└── README.md

---

## 🛠 Tecnologias Utilizadas

- Python 3
- pandas
- requests
- zipfile (biblioteca padrão do Python)

---

## ▶️ Como Executar o Projeto

### 1️⃣ Criar o ambiente virtual

```bash
python -m venv .venv

### 2️⃣ Ativar o ambiente virtual

No Windows:
.venv\Scripts\activate

---

3️⃣ Instalar as dependências

pip install -r requirements.txt

---

4️⃣ Executar o download dos dados

python src/download_ans.py

---

5️⃣ Processar e consolidar os dados

python src/processar_dados.py

---

Ao final da execução, o arquivo consolidado_despesas.zip será gerado na pasta data/output.

---

📊 Processamento dos Dados

- Os arquivos ZIP são extraídos automaticamente
- Caso um arquivo já tenha sido extraído anteriormente, ele não é processado novamente
- Os dados dos três trimestres são lidos e unidos em um único DataFrame
- Foi adicionada uma coluna de trimestre para identificar a origem de cada registro

---

📄 Estrutura do Arquivo Final

O arquivo CSV final contém as seguintes colunas:

Coluna	        Descrição
CNPJ	        Código da operadora (REG_ANS)
Ano	            Ano de referência
Trimestre	    Trimestre de referência
ValorDespesas	Valor total das despesas com eventos/sinistros

---

⚠️ Tratamento de Inconsistências

Durante o desenvolvimento, algumas inconsistências foram identificadas e tratadas da seguinte forma:

- CNPJs duplicados com razões sociais diferentes
Foi utilizado o campo REG_ANS como identificador principal. O relacionamento com CNPJ e razão social completa não foi realizado por não fazer parte do escopo do teste.
- Valores zerados ou negativos
Esses registros foram mantidos, pois podem representar ajustes ou estornos contábeis válidos.
- Formatação de valores e datas
Os valores monetários foram convertidos para o tipo numérico (float) e as datas foram utilizadas para identificar ano e trimestre.

---

⚖️ Decisão Técnica

- Os dados foram processados em memória utilizando a biblioteca pandas.
Essa escolha foi feita por simplicidade de implementação e por o volume de dados ser compatível com o processamento local.
- Em um cenário com maior volume de dados, poderia ser avaliado o processamento incremental ou o uso de outras ferramentas.

---

📝 Observações Finais

Este projeto teve como foco demonstrar a capacidade de organizar dados, lidar com diferentes formatos de arquivos e implementar um fluxo simples de ETL utilizando Python.