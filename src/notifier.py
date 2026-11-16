import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Carregar variáveis do ficheiro .env
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")

def enviar_email_relatorio(conteudo_relatorio):
    """Envia o relatório gerado por e-mail via servidor SMTP do Gmail."""
    if not EMAIL_USER or not EMAIL_APP_PASSWORD or not EMAIL_TO:
        raise ValueError("As credenciais de e-mail não estão configuradas corretamente no ficheiro .env!")

    msg = EmailMessage()
    msg.set_content(conteudo_relatorio)
    msg['Subject'] = "🤖 Relatório Automático de Vendas - Python"
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO

    # Conexão segura com o Gmail (porta 465 com SSL)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_APP_PASSWORD)
            smtp.send_message(msg)
        print("✅ E-mail enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar o e-mail: {e}")

if __name__ == "__main__":
    # Teste rápido local
    enviar_email_relatorio("Teste de mensagem do bot de relatórios.")