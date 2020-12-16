from core.contact_methods.phone_contact import PhoneContact
from core.contact_methods.email_contact import EmailContact

test = ""

if test == "e":
    c = EmailContact("armck@ymail.com")
else:
    c = PhoneContact({"number" : "6154385609", "carrier" : "verizon"})

c.construct_message()
c.notify()