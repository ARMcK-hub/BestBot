from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class SMTPServer():
    smtp = "smtp.gmail.com"
    port = 587

    def __init__(self, smtp_user: str, smtp_password: str) -> None:
        self.user = smtp_user
        self.password = smtp_password

    def construct_message(self, product):
        product.get_cart_url()
        self.message = f"""
        Product:  {product.alias}
        URL:  {product.cart_url}
        """

    def construct_except_message(self, exception):
        self.message = f"""
        ---Script Failure---

        Exception Logged: {exception}
        """

    def notify(self):
        server = SMTP(SMTPServer.smtp, SMTPServer.port)
        server.ehlo()
        server.starttls()
        server.login(self.user, self.password)
        msg = MIMEMultipart()
        msg['From'] = self.user
        msg['To'] = self.contact_gateway

        body = self.message

        msg.attach(MIMEText(body, 'plain'))
        message = msg.as_string()
        server.sendmail(self.user, self.contact_gateway, message)

        server.quit()
