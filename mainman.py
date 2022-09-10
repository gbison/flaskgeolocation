import configparser
import smtplib

from mailmessage import mailmessage


class mailman:
    passw = ""
    user = ""
    login = False
    smtp = None

    def __init__(self):
        print("Mail initializing...")

    def mail_setup(self):
        self.smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        #     # smtp.ehlo()
        #     # smtp.starttls()
        #     # smtp.ehlo()  # Have to re-run due to encryption.

    def mail_send(self, msg):
        if self.smtp is not None:
            self.smtp.send_message(msg)
        else:
            raise RuntimeError("No SMTP server was configured!")

    def build_mail(self) -> mailmessage:
        emailmsg = mailmessage()
        return emailmsg

    def mail_login(self) -> bool:
        # Login
        if self.get_config():
            print("Attempting login...")
            if self.smtp is not None:
                self.smtp.login(self.user, self.passw)
            else:
                raise RuntimeError("No SMTP server was configured!")
            return True
        else:
            raise RuntimeError("NO login information was defined! Could not LOGIN!")

    def get_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.passw = config['mailcred']['passw'].strip()
        self.user = config['mailcred']['user'].strip()
        if self.passw is not None and self.user is not None:
            return True
        else:
            raise RuntimeError("NO login information was defined! Could not LOGIN!")

        # print("List all contents")
        # for section in config.sections():
        #     print("Section: %s" % section)
        #     for options in config.options(section):
        #         print(
        #             "x %s:::%s:::%s"
        #             % (options, config.get(section, options), str(type(options)))
        #         )
