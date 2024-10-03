import pandas as pd

# 1. Carregamento dos dados
path_vendas = r'D:\Projeto - GDM Marketing\data-engineer-test-main\files\Vendas.csv'
path_clientes = r'D:\Projeto - GDM Marketing\data-engineer-test-main\files\Clientes.csv'

# Ler os arquivos CSV
vendas = pd.read_csv(path_vendas)
clientes = pd.read_csv(path_clientes)

# Validando o nome das colunas
print("Colunas de vendas:", vendas.columns)
print("Colunas de clientes:", clientes.columns)

# 2. Limpeza dos dados
# Remover duplicados
vendas = vendas.drop_duplicates()
clientes = clientes.drop_duplicates()

# Preenchendo os valores ausentes
# Se faltou algum valor de venda, preenche com a média
vendas['ValorVenda'] = vendas['ValorVenda'].fillna(vendas['ValorVenda'].mean())
clientes['Idade'] = clientes['Idade'].fillna(
    clientes['Idade'].median())  # Para idade, estou usando a mediana
clientes['PreferenciaProduto'] = clientes['PreferenciaProduto'].fillna(
    'Indefinido')  # Preferência indefinida quando não soubermos

# Converter dados
vendas['DataVenda'] = pd.to_datetime(
    vendas['DataVenda'], format='%Y-%m-%d', errors='coerce')  # Convertendo datas
# Convertendo valores de venda em números
vendas['ValorVenda'] = pd.to_numeric(vendas['ValorVenda'], errors='coerce')
clientes['Idade'] = pd.to_numeric(
    clientes['Idade'], errors='coerce')  # Convertedo idade em número

# 3. Juntar as informações de vendas com as de clientes
# Combinar dados de vendas usando localização para o match
dados_completos = vendas.merge(
    clientes, left_on='LocalizacaoCliente', right_on='Localizacao', how='inner')

# Verificar se ta tudo ok
print("\nDados completos após o merge:")
print(dados_completos.head())

# 4. Análise dos Dados Tratados

# Receita dos últimos 6 meses
seis_meses_atras = pd.Timestamp.now() - pd.DateOffset(months=6)
vendas_ultimos_6_meses = vendas[vendas['DataVenda'] >= seis_meses_atras]

# Somando o valor dessas vendas
receita_total_6_meses = vendas_ultimos_6_meses['ValorVenda'].sum()
print(f"\nReceita total dos últimos 6 meses: R$ {receita_total_6_meses:.2f}")

# Produtos mais vendidos
# Contando quantas vezes cada produto foi vendido e trazer a receita gerada
produtos_mais_vendidos = vendas.groupby('ProdutoID').agg({'VendaID': 'count', 'ValorVenda': 'sum'}).rename(
    columns={'VendaID': 'QuantidadeVendas'}).sort_values(by='QuantidadeVendas', ascending=False).head(5)

print("\nTop 5 produtos mais vendidos:")
print(produtos_mais_vendidos)

# Receita total dos 5 produtos mais vendidos
receita_top_5_produtos = produtos_mais_vendidos['ValorVenda'].sum()
print(f"\nReceita total gerada pelos 5 produtos mais vendidos: R$ {
      receita_top_5_produtos:.2f}")

# Receita por localização
# Agrupando localização e somando receita
receita_por_localizacao = dados_completos.groupby(
    'Localizacao').agg({'ValorVenda': 'sum'}).reset_index()

print("\nReceita por localização dos clientes:")
print(receita_por_localizacao)

# 5. Exportação dos dados tratados para um arquivo CSV (deixei como comentario para nao erro no codigo.)
# dados_completos.to_csv(r'D:\Projeto - GDM Marketing\data-engineer-test-main\files\Vendas_Tratadas.csv', index=False)
