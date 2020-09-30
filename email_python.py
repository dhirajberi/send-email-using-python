import smtplib
import getpass      #For security (Optional)

ob = smtplib.SMTP('smtp.zoho.com', 587)     #Connecting to SMTP server (smtp.gmail.com)
ob.starttls()       #Starting TLS connection

my_email = ''      #Your email
password = getpass.getpass()        #For Security

ob.login(my_email,password)     #Login in to the SMTP Server 

reciever_email = input('Enter Reciever Email: ') 

subject = input('Enter Subject: ')

body = input('Enter Body: ')

message = f'Subject:{subject}\n\n{body}' # or ('Subject: {} \n\n{}'.format(subject,body))

print('Sending email...')
ob.sendmail(my_email, reciever_email, message)       #Sending Email
print('Done.')

ob.quit()       #Disconnect

#Script by Dhiraj Beri.