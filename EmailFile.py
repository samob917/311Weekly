def the_function():
    import smtplib

    # Connect to SMTP server
    smtp = smtplib.SMTP('smtp.example.com', 587)
    smtp.ehlo()
    smtp.starttls() 
    smtp.ehlo()
    smtp.login('username', 'password')

    # Send email  
    smtp.sendmail('from@email.com', 'to@email.com', html) 
    smtp.quit()

the_function()
