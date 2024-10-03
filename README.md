# Análise de Vendas e Clientes - Python

Este projeto tem como objetivo analisar dados de vendas e clientes utilizando a biblioteca **Pandas** no Python. A análise inclui a limpeza de dados, combinação de datasets, análise de vendas dos últimos 6 meses, produtos mais vendidos e receita por localização geográfica.

## Visão Geral
Este projeto faz uma análise detalhada de dados de vendas e clientes, com foco nos seguintes pontos:
- Limpeza e preparação dos dados.
- Análise da receita total dos últimos 6 meses.
- Identificação dos 5 produtos mais vendidos.
- Análise da receita gerada por localização dos clientes.
- Exportação dos dados tratados para um arquivo CSV.

## Estrutura do Projeto
Os arquivos utilizados neste projeto estão localizados nos seguintes caminhos:
- **Vendas.csv**: Contém os dados de transações de vendas.
- **Clientes.csv**: Contém as informações dos clientes.

## Bibliotecas Utilizadas
- **Pandas**: Para manipulação e análise de dados.


Processos Principais
1. Carregamento dos Dados
Os dados são carregados a partir de arquivos CSV utilizando o Pandas:

vendas = pd.read_csv(path_vendas)
clientes = pd.read_csv(path_clientes)

2. Limpeza dos Dados
Remoção de duplicatas: Linhas duplicadas são removidas de ambos os datasets.
Tratamento de valores ausentes: Preenchemos valores faltantes em ValorVenda com a média, em Idade com a mediana, e valores nulos em PreferenciaProduto com 'Indefinido'.
Conversão de tipos: As colunas DataVenda, ValorVenda e Idade foram convertidas para os tipos apropriados.

3. Combinação dos Dados
Os dados de vendas foram combinados com os dados de clientes com base na localização:

dados_completos = vendas.merge(clientes, left_on='LocalizacaoCliente', right_on='Localizacao', how='inner')


4. Análise dos Dados
Receita Total dos Últimos 6 Meses:
Calcula a receita gerada nos últimos 6 meses:

receita_total_6_meses = vendas_ultimos_6_meses['ValorVenda'].sum()


Produtos Mais Vendidos:
Identifica os 5 produtos mais vendidos e a receita gerada por eles:

produtos_mais_vendidos = vendas.groupby('ProdutoID').agg({'VendaID': 'count', 'ValorVenda': 'sum'}).sort_values(by='QuantidadeVendas', ascending=False).head(5)


Receita por Localização:
Agrupa as vendas por localização para calcular a receita gerada em cada local:

receita_por_localizacao = dados_completos.groupby('Localizacao').agg({'ValorVenda': 'sum'}).reset_index()

5. Exportação de Dados
Os dados tratados e combinados podem ser exportados para um novo arquivo CSV, descomentando a linha:

# dados_completos.to_csv(r'D:\Projeto - GDM Marketing\data-engineer-test-main\files\Vendas_Tratadas.csv', index=False)


Conclusão
Este projeto fornece uma visão clara dos dados de vendas e clientes, permitindo identificar tendências de produtos e regiões com maior receita. Ele também possibilita a personalização para exportar os dados tratados em formato CSV para outras análises.
