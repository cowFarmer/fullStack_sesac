import smtplib


smtp = smtplib.SMTP_SSL('smtp.naver.com', 465)

smtp.ehlo()

my_password = open("secret.txt", "r").read()
smtp.login('nhh9692@naver.com', my_password)


from email.message import EmailMessage


msg = EmailMessage()

msg['Subject'] = '메일제목'
msg['From'] = 'nhh9692@naver.com'
msg['To'] = 'noehyeanhoo@gmail.com'
msg.set_content('메일 본문, 멀티 라인도 가능, 메세지 작성하기')

smtp.send_message(msg)

smtp.quit()
