import smtplib as s
ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()
ob.login("puspita.public@gmail.com", "DADA4@dadi")


subject = "Sending email using python"
body = "This is tutorial of sending email using python script"
message = "Subject:{} \n\n {}".format(subject, body)


listofAddress = ['er.subarnasahoo@gmail.com', 'ssoyansu@gmail.com', 'puspita.public@gmail.com']
ob.sendmail('puspita.public@gmail.com', listofAddress, message)


print('Send successfully...')
ob.quit()

