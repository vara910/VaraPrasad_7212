from abc import ABC,abstractmethod
class Mail(ABC):
    @abstractmethod
    def send(self):
       pass
class Email(Mail):
    def send(self):
        print("email is one of the mail's child class")
class Sms(Mail):
    def send(self):
        print("sms works without the internet connection")
class Whatsapp(Mail):
    def send(self):
        print("whatsapp only works through internet")
e=Email()
e.send()
s=Sms()
s.send()
w=Whatsapp()
w.send()
