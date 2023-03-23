import pickle
import time
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
x = time.localtime()
month = x[1]
day = x[2]
md = {1:31,2:28,3:31,4:30,5:31,7:31,8:31,10:31,12:31,6:30,9:30,11:30}
today = 22
num = 72
if month == 3:
    num = day - today


if month-3>0:
    k = month-4
    num = 31 - today
    for i in range(k):
        num = num + md[month-1]
    num = num + day
send_data = """<h1 align=\"center\">Today's words</h1>
<style>
a:link {
  color: black;
}
</style>"""

for i in range(10):
    send_data = send_data + "<a href=\"https://dict.youdao.com/result?word=" + word[10*num + i] + "&lang=en\">" + word[10*num + i] + "</a>\n"  \
                          + "<p>" + meaning[10*num + i] + "</p>\n"


host_server = ''

sender_qq = ''

pwd = ''

sender_qq_mail = ''

receiver = ''
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







