def the_function(html):
    import smtplib

    # Connect to SMTP server
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login("weeklythreeoneone", "abcde1234!")  # Username and PW

    # Send email
    smtp.sendmail("weeklythreeoneone@gmail.com", "andrew.dabinett@gmail.com", html)
    smtp.quit()
