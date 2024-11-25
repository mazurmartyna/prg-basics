import re

email_file = 'email.txt'

with open(email_file, 'r') as file:
    email = file.read()


pattern_sender = 'From: \w+ \w+ <(.+)>'

pattern_recipient = 'To: \w+ \w+ <(.+)>'

pattern_subject = 'Subject:(.+)'

pattern_body = '(^\n[\s\S]+\d)'
#'\r?(^\n[\s|\S|\n]+\d$)\n'
# '(^\n[\s\S]+\d$)'

def email_sender(email, pattern_sender):
    sender = re.findall(pattern_sender, email)
    return sender

def email_recipient(email, pattern_recipient):
    recipient = re.findall(pattern_recipient, email)
    return recipient

def email_subject(email, pattern_subject):
    subject = re.findall(pattern_subject, email)
    return subject

def email_body(email, pattern_body):
    body = re.findall(pattern_body, email, re.MULTILINE)
    return body

print("Sender: ", email_sender(email, pattern_sender))
print("Recipient: ", email_recipient(email, pattern_recipient))
print("Subject: ", email_subject(email, pattern_subject))
print("Body: ", email_body(email, pattern_body))