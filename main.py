import pickle
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
a = open("./word","rb")
word = pickle.load(a)
b = open("./meaning","rb")
meaning = pickle.load(b)
a.close()
b.close()
## test word and meaning
# print(word[0])
# print(meaning[0])

## day + 1 for run once  
x = open("./flag","r")
day = int(x.read())
x.close()
y = open("./flag","w")
y.write(str(day+1))
y.close()
send_data = """<h1 align=\"center\">Today's words</h1>
<style>
a:link {
  color: black;
}
</style>"""

for i in range(10):
    send_data = send_data + "<a href=\"https://dict.youdao.com/result?word=" + word[10*day + i] + "&lang=en\">" + word[10*day + i] + "</a>\n"  \
                          + "<p>" + meaning[10*day + i] + "</p>\n"


host_server = 'smtp.163.com'

sender_qq = 'wpw12138@163.com'

pwd = 'ARLYBVGDHDJELLSC'

sender_qq_mail = 'wpw12138@163.com'

receiver = 'ssnape@qq.com'
# receiver1 = '2926083239@qq.com'
        
mail_content = send_data

mail_title = 'Day word'


smtp = SMTP_SSL(host_server)

smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender_qq_mail, pwd)

msg = MIMEText(mail_content, "html", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = 'Word'
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
# smtp.sendmail(sender_qq_mail,receiver1, msg.as_string())
smtp.quit()







