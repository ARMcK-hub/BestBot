from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.network.g import p, u



class SMTPServer():
    smtp = "smtp.gmail.com"
    port = 587

    def construct_message(self, product):
        product.get_cart_url()
        self.message = f"""
        ONE SALE!!! - {product.Name}

        URL - {product.cart_url}
        """

    def notify(self):
        server = SMTP(SMTPServer.smtp, SMTPServer.port)
        server.ehlo()
        server.starttls()
        server.login(u, p)
        msg = MIMEMultipart()
        msg['From'] = u
        msg['To'] = self.contact_gateway

        body = self.message

        msg.attach(MIMEText(body, 'plain'))
        message = msg.as_string()
        server.sendmail(u, self.contact_gateway, message)

        server.quit()
