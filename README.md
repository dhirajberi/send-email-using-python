# send-email-using-python
You are able to send email using python. No need to open gmail dashboard again.
Download Python
https://www.python.org/downloads/
Application of Python
Web Development
Game Development
ML and AI
Data Science and Data Visualization
Desktop GUI
Web Scraping
Automate daily tasks etc.
How to send email using Python
Requirements
Laptop/PC
Internet
Python
IDE (Sublime, Visual Studio, PyCharm etc.)
Email ID
Libraries: smtplib, getpass(optional)
Steps
1. Install and import libraries.
(Open terminal or CMD)
pip install smtplib
pip install getpass
2. If you have Gmail ID then go to
https://myaccount.google.com/lesssecureapps​ and turn it on.
3. Connect to SMTP Server.
4. Start TLS connection.
5. Login.
6. Send Mail.
7. Disconnect.
Source Code
import​ smtplib
import​ getpass
#For security (Optional)
ob = smtplib.SMTP(​ 'smtp.zoho.com'​ , ​ 587​ )
(smtp.gmail.com)
ob.starttls()
#Starting TLS connection
#Connecting to SMTP servermy_email = ​ 'admin@digitalberi.com'
password = getpass.getpass()
ob.login(my_email,password)
#Your email
#For Security
#Login in to the SMTP Server
reciever_email = ​ input​ ( ​ 'Enter Receiver Email: '​ )
subject = ​ input​ ( ​ 'Enter Subject: '​ )
body = ​ input​ ( ​ 'Enter Body: '​ )
message = ​ f ​ 'Subject:​ { ​ subject​ } ​ \n\n​ { ​ body​ } ​ '
print​ ( ​ 'Sending email...'​ )
ob.sendmail(my_email, reciever_email, message)
print​ ( ​ 'Done.'​ )
ob.quit()
#Disconnect
#Script by Dhiraj Beri.

Thank You!
Regards,
Dhiraj Beri.
