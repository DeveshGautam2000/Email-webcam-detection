import smtplib
import imghdr
import glob
import os
from email.message import EmailMessage

PASSWORD = "xfsiqzplgskufgiz"
SENDER = "deveshgautamwow@gmail.com"
RECEIVER = "deveshgautamking@gmail.com"

def clean_folder():
     images = glob.glob("images/*.png")
     for image in images:
          os.remove(image)

def send_mail(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Object Detected!"
    email_message.set_content("Hey, We just detected new object!!")

    with open(image_path, "rb") as file :
        content = file.read()
    
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    clean_folder()

if __name__ == "__main__":
    send_mail(image_path="images/53.png")