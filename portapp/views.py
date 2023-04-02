from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import AllowAny


import smtplib
import time
import pandas as pd


import urllib

@api_view(['GET'])
def all(request):
    mail=request.query_params['mail']
    apppass=request.query_params['apppass']
    name=request.query_params['name']
    sheet_id=request.query_params['id']
    sheet_name=request.query_params['sname']

    res=send_email(mail,apppass,name,sheet_id,sheet_name)
    #file(sheet_id,sheet_name)
    return Response({"STATUS":res})



# def file(sheet_id,sheet_name):
#     url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
#     df=pd.read_csv(url)
#     print(df['NAME'])
    

def send_email(mail,apppass,name,sheet_id,sheet_name):
    res=[]
    your_password =apppass
    your_email = mail

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(your_email, your_password) 
    

    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    email_list=pd.read_csv(url)

    all_names = email_list['NAME']
    all_emails = email_list['MAIL']
    all_messages=email_list['MESSAGE']
    all_subject = email_list['SUBJECT']

    for idx in range(len(all_emails)):
    # Get each records name, email, subject and message
        sheet_name = all_names[idx]
        email = all_emails[idx]
        message = all_messages[idx]
        subject = all_subject[idx]

        msg=f"Dear {sheet_name},\n"


        # Create the email to send
        full_email = ("From: {0} <{1}>\n"
                      "To: {2} <{3}>\n"
                      "Subject: {4}\n\n"
                      "{5}{6}"
                      .format(name, your_email, sheet_name, email, subject, msg, message))#name change

        # In the email field, you can add multiple other emails if you want
        # all of them to receive the same text
        try:
            server.sendmail(your_email, [email], full_email)
            res.append(f' --> Email to {name},{email} successfully sent!')
            time.sleep(1)
        except Exception as e:
            res.append('Email to {} could not be sent--------------------------------------------------------------because {}'.format(name, str(e)))
            
    return res