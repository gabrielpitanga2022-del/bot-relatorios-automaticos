import os
import csv

def processar_relatorio(caminho_csv):
    """Lê o ficheiro CSV usando o módulo nativo csv, calcula métricas e devolve um resumo."""
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Ficheiro não encontrado: {caminho_csv}")

    faturacao_geral = 0.0
    total_itens_vendidos = 0
    vendas_por_produto = {}

    with open(caminho_csv, mode='r', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            quantidade = int(linha['Quantidade'])
            preco_unitario = float(linha['Preco_Unitario'])
            faturacao_linha = quantidade * preco_unitario
            
            faturacao_geral += faturacao_linha
            total_itens_vendidos += quantidade
            
            produto = linha['Produto']
            if produto not in vendas_por_produto:
                vendas_por_produto[produto] = 0
            vendas_por_produto[produto] += quantidade

    # Encontrar o produto mais vendido
    produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get)
    qnt_produto_mais_vendido = vendas_por_produto[produto_mais_vendido]

    relatorio = (
        f"📊 RELATÓRIO DIÁRIO DE VENDAS\n\n"
        f"• Faturação Total: {faturacao_geral:.2f} €\n"
        f"• Total de Itens Vendidos: {total_itens_vendidos}\n"
        f"• Produto Destaque: {produto_mais_vendido} ({qnt_produto_mais_vendido} unidades vendidas)\n"
    )

    return relatorio

if __name__ == "__main__":
    caminho = os.path.join("data", "input", "vendas_teste.csv")
    print(processar_relatorio(caminho))