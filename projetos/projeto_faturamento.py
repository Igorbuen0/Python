import pandas as pd
import smtplib
import email.message

tabela_vendas = pd.read_excel('Vendas.xlsx')
pd.set_option('display.max_columns', None)

# calculo do ticket medio por item
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print('-' * 50)
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0:'Ticket médio'})


# enviar um email automaticamente
def enviar_email():
    corpo_email = f"""
    <p>Segue o relátorio solicitado de vendas por cada loja.</p>

        <p>Faturamento:</p>
        {faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}
        
        <p>Quantidade Vendida:</p>
        {quantidade.to_html}

        <p>Ticket médio dos produtos em cada loja:</p>
        {ticket_medio.to_html(formatters={'Ticket médio': 'R${:,.2f}'.format})}

        <p>qualquer duvida, estou a disposição.</p>
        <p>att...</p>
        <p>Igor</p>
 """

    msg = email.message.Message()
    msg['Subject'] = "Faturamento medio por loja"
    msg['From'] = 'xxxx@gmail.com'
    msg['To'] = 'xxxx@email.com'
    password = 'pass'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
enviar_email()

