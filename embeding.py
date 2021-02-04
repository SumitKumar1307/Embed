import smtplib

def main():
    try:
        s = smtplib.SMTP('smtp.gmail.com', 25)
        s.starttls()
        s.login('chatwithcodech@gmail.com', '711172371117')
        message = "Python is Succesfully Embed into cpp"
        s.sendmail('chatwithcodech@gmail.com', 'sk8861620@gmail.com', message)
        s.quit()
        return 1
    finally:
        return 0
