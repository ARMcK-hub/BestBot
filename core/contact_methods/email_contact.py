from core.network.smtp_server import SMTPServer


class EmailContact(SMTPServer):

    def __init__(self, notification_data, Config):
        self.contact = notification_data
        self.gateway = notification_data.split("@")[-1]
        self.contact_gateway = notification_data
        super().__init__(Config["smtp_server"]["user"], Config["smtp_server"]["password"])
