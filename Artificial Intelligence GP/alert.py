
import smtplib
from email.message import EmailMessage

def send_alert(studentid, name, email, school, programme, gpa):
    sender_email="jnelle.bailey@gmail.com"
    smtp_server="smtp.gmail.com"
    port=465
    sender_password="rano euek nkib lmle"
    student_email=email
    programmedirector_email='johnbr@gmail.com'
    faculty_administrator='marysu@gmail.com'
    recipients=[student_email, programmedirector_email, faculty_administrator]


    
    #Creating message
    message=EmailMessage()
    message['From']=sender_email
    message['To']=', '.join(recipients)
    message['Subject']="University of Technology, Academic Probation"
    message.set_content(f"""Good day {name}\n\nThank you for choosing the University of Technology for your studies.\nAfter a thorough analysis of your GPA we are concerned with the direction it seems to be going and would like to give a formal warning. See below for your information going forward and we look forward to seeing your improvements.\n\nStudent ID: {studentid}\nStudent Name: {name}\nSchool: {school}\nProgramme: {programme}\nCurrent GPA: {gpa}\n\nBest Regards,\n\n\nJohn Brown\nProgramme Director\nUniversity of Technology, Jamaica\n237 Old Hope Road, Kingston 6\n\nDirect Line: (876) 927-1680\nEmail: johnbr@gmail.com""")
    try:

        #context=ssl.create_default_context()

        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_password)
        server.send_message(message)
        print("Successfully sent")
        server.quit




    except Exception as e:
        print(e)

