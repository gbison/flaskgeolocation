from email.message import EmailMessage


class mailmessage(EmailMessage):
    msg = None

    def __init__(self):
        print("Creating message....")
        self.msg = EmailMessage()

    def set_subject(self, subject):
        self.msg['Subject'] = subject

    def set_from(self, originator):
        self.msg['From'] = originator

    def set_to(self, recipient):
        self.msg['To'] = recipient

    def set_msg(self, message):
        self.msg.set_content(message)
