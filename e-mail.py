#here we import required module
#sp=serviceProvider

import smtplib,webbrowser,getpass

#============================define function for get a email id from user==============================

def get_mail():
    servicesAvilable =['gmail','hotmail','yahoo','outlook']
    while True:
        mail_id = input("Enter your mail id : - ")
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos = mail_id.find("@")          #find operator is use for find the particular string or char from the senetces
    
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos+1:dotcom_pos]    #sp = mail_id[staring_index_no :ending index] 
            if sp in servicesAvilable:
                return mail_id , sp  
                break
            else:
                print("We don't provide services for " + sp)
                print("We provide services only for : hotmail/outlook,gmail,yahoo")
                continue


        else:
            print("Invalid E-mail retype again.........")
            continue


#============================= here we define a function for set the smtp ====================================
def set_smtp_domain(sp):
    if sp == 'gmail':
        return 'smtp.gmail.com'
    elif sp == 'outlook' or sp== 'hotmail':
        return 'smtp-mail.outlook.com'
    elif serviceProvider == 'gmail':
        return 'smtp.mail.yahoo.com'


#===============================Main programm start from here===========================================

print('=======================WELCOME SIR OUR PROGRAM=======================')
print('\nEnter your E-mail & password\n')
e_mail , sp = get_mail()
password = getpass.getpass("For security reason password not show so don't worry\n Enter ur password : ")

#=====================================================================================================

while True:
    try:
        smtpDomain = set_smtp_domain(sp)
        connection = smtplib.SMTP(smtpDomain , 587)
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail,password)

    except:
        if sp =='gmail':
            print('Login unsuccessful, There may be two possible reasons :- \n1]may be ur username or password worng')
            print("2]you are using Gmail there is an option in gmail 'allow less secure app may me not on' ")
            print("Do you want us to open a webpage from where you can enable this option")
            answer = input("Yes or No ? : ")
            if answer == "yes":
                webbrowser.open("https://myaccount.google.com/lesssecureapps")

            else:
                print("We won't open webpage for you, you also can goto 'https://myaccount.google.com/lesssecureapps'")
                print("please retype your e-mail and passeord also")
            e_mail,serviceProvider = get_mail()
            password = getpass.getpass("password : ")
            continue
           
        else:
            print("Login unsuccessful, most possible you types wrong username or password")
            print("please retype your e-mail address and password: ")
            e_mail , serviceProvider =get_mail()
            password = getpass.getpass("For security reason password not show so don't worry\n Enter ur password :")
            continue
   
    else:
        print("\nLogin successfull...............")
        break
    
#=====================================================================================================
print("\nPleae type receiver's E-mail address: ")
receiver, receiversp = get_mail()

print("\nNow please type Subject & Message")
Subject = input("Subject :")
Message = input("Message:\t")
try:
    #print("Sender meil address: ",e_mail,"\nReciver mail address : ",receiver,"\nMessage: ",Message)
    connection.sendmail(e_mail,receiver,("Subject : " +str(Subject)+"\n\n"+str(Message)))
except:
    if smtplib.SMTPRecipientsRefused:
        print("Error can't be found...")
    elif smtplib.SMTPConnectError:
        print("Connection error ")
else:
    print("Email send successfully...........")
connection.quit()

        
        
            
