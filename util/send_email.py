#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class SendEmail:

    def send_mail(self, user_list, sub, content):
        send_user = "191707485@qq.com"
        password = "urlekrvnlzvabgch"
        msg = MIMEMultipart()
        msg["Subject"] = sub
        msg["From"] = send_user
        msg["To"] = ";".join(user_list)
        part_content = MIMEText(content)
        msg.attach(part_content)

        #---这是附件部分---
        #xml类型附
        # part = MIMEApplication(open('D:\\test_zhuzi.xml','rb').read())
        #
        # part.add_header('Content-Disposition', 'attachment', filename="D:\\test_zhuzi.xml")
        #
        # msg.attach(part)
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 连接smtp邮件服务器,端口默认是465
        server.login(send_user, password)  # 登陆服务器
        server.sendmail(send_user, user_list, msg.as_string())  # 发送邮件
        server.close()


    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num/count_num*100)
        fail_result = "%.2f%%" % (fail_num/count_num*100)
#["1573533054@qq.com", "youmengting@swartz.cn"
        user_list = ["1573533054@qq.com"]

        sub = "接口自动化报告"
        content = "此次运行了%s接口测试用例, 通过%s, 失败%s, 通过率%s, 失败率%s" % (count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, sub, content)

# if __name__ == "__main__":
#     s = SendEmail()
#     s.send_main([1, 2, 3], [4, 5])