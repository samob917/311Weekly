def the_function():
    import smtplib

    # Connect to SMTP server
<<<<<<< HEAD
    smtp = smtplib.SMTP('smtp.example.com', 587)
    smtp.ehlo()
    smtp.starttls() 
    smtp.ehlo()
    smtp.login('username', 'password')

    # Send email  
    smtp.sendmail('from@email.com', 'to@email.com', html) 
=======
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls() 
    smtp.ehlo()
    smtp.login('weeklythreeoneone@gmail.com', 'abcde1234!') #Username and PW 

    # Send email  
    smtp.sendmail('weeklythreeoneone@gmail.com', 'andrew.dabinett@gmail.com', html) 
>>>>>>> d484a9a944386d4cf60831173acfbe6c825d4ad9
    smtp.quit()

the_function()
