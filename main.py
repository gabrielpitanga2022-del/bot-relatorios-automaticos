import os
from src.processador import processar_relatorio
from src.notifier import enviar_email_relatorio

def main():
    print("🚀 A iniciar o bot de automação de relatórios...")

    # 1. Definir o caminho do CSV de entrada
    caminho_csv = os.path.join("data", "input", "vendas_teste.csv")

    try:
        # 2. Processar os dados e gerar o relatório
        print("🔄 A processar os dados de vendas com Pandas...")
        relatorio = processar_relatorio(caminho_csv)
        print("\n--- Relatório Gerado ---")
        print(relatorio)
        print("------------------------\n")

        # 3. Enviar o relatório por e-mail
        print("📧 A enviar o relatório por e-mail (Gmail)...")
        enviar_email_relatorio(relatorio)

    except Exception as e:
        print(f"❌ Ocorreu um erro durante a execução: {e}")

if __name__ == "__main__":
    main()