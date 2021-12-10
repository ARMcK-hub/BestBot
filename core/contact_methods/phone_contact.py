from core.network.smtp_server import SMTPServer

class PhoneContact(SMTPServer):
    gateway = {
        "verizon": "vtext.com",
        "at&t": "txt.att.net",
        "tmobile": "tmomail.net",
        "sprint": "messaging.sprintpcs.com",
        "xfinity": "vtext.com",
        "virgin": "vmobl.com",
    }

    def __init__(self, notification_data, Config):
        self.contact = notification_data["number"]
        self.gateway = PhoneContact.gateway[notification_data["carrier"].lower()]
        self.contact_gateway = self.contact + "@" + self.gateway
        super().__init__(Config["smtp_server"]["user"], Config["smtp_server"]["password"])
