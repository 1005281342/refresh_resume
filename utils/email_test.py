import smtplib
from email.header import Header
from email.mime.text import MIMEText

from utils.constant import FromEmail, ToEmail, PassWord, MailHost, WorkTitle


def send_email(*, content, title=WorkTitle):
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(FromEmail)
    message['To'] = ",".join(ToEmail)
    message['Subject'] = Header(title, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(MailHost, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(FromEmail, PassWord)  # 登录验证
        smtpObj.sendmail(FromEmail, ToEmail, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    send_email(content="发送邮件测试", title="python测试")
