from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import AllowAny


import smtplib
import time
import pandas as pd
from datetime import datetime
from csv import writer
from portapp.models import QUESTION
from django.http import JsonResponse

def home(request):

    return render(request,'graph.html')
    # return JsonResponse({"d":list(d.values())})


def goodhome(request):

    return render(request,'acchagraph.html')
def getting(request):
    d=QUESTION.objects.all()
    
    #return render(request,'graph.html',context)
    return JsonResponse({"d":list(d.values())})
@api_view(['GET'])
def test(request):
    # time=request.query_params['time']
    temp=request.query_params['temp']
    currentDateAndTime = datetime.now()

    time = int(currentDateAndTime.strftime("%M%S"))

    data=QUESTION(q1=time,q2=temp)
    data.save()
    # with open('event.csv', 'a') as f:
    #     f.write(f'last update at {datetime.datetime.now()} ans {x} \n')

    return Response("temp received")


# @api_view(['GET'])
# def static(request):
#     mail=request.query_params['mail']
#     apppass=request.query_params['apppass']
#     name=request.query_params['name']
#     sheet_id=request.query_params['id']
#     sheet_name=request.query_params['sname']

#     res=send_email_static(mail,apppass,name,sheet_id,sheet_name)
#     #file(sheet_id,sheet_name)
#     return Response({"STATUS":"res"})

# @api_view(['GET'])
# def dynamic(request):
#     mail=request.query_params['mail']
#     apppass=request.query_params['apppass']
#     name=request.query_params['name']
#     sheet_id=request.query_params['id']
#     sheet_name=request.query_params['sname']

#     res=send_email_dynamic(mail,apppass,name,sheet_id,sheet_name)
#     #file(sheet_id,sheet_name)
#     return Response({"STATUS":res})



# def file(sheet_id,sheet_name):
#     url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
#     email_list=pd.read_csv(url)
#     # print(email_list.columns.tolist())

#     all_emails = email_list['MAIL']
#     all_messages=email_list['MESSAGE']
#     df=pd.read_csv(url)
#     print(df)
#     new_df=df.iloc[:,4:]
#     ndf_blank=new_df.fillna('')
#     print(ndf_blank)
    

    
#     for idx in range(len(all_emails)):
#         dicts = {}
#         keys = range(len(ndf_blank.columns))
#         for i in keys:
#           x='A' + str(i)
#           dicts[x] = ndf_blank[x][i]

#         message = all_messages[idx].format(**dicts)
#         print(dicts)
#         print(message)

    
# def send_email_dynamic(mail,apppass,name,sheet_id,sheet_name):
#     res=[]
#     your_password =apppass
#     your_email = mail

#     server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#     server.ehlo()
#     server.login(your_email, your_password) 
    

#     url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
#     email_list=pd.read_csv(url)

#     all_names = email_list.loc[:,'NAME']
#     all_emails = email_list['MAIL']
#     all_messages=email_list['MESSAGE']
#     all_subject = email_list['SUBJECT']

#     df=pd.read_csv(url)
#     print(df)
#     new_df=df.iloc[:,4:]
#     ndf_blank=new_df.fillna(' ')
#     print(ndf_blank)

#     for idx in range(len(all_emails)):
#         dicts = {}
#         keys = range(len(ndf_blank.columns))
#         for i in keys:
#         #   print(i)
#           x='A' + str(i)
#           dicts[x] = ndf_blank[x][idx]

#         message = all_messages[idx].format(**dicts)
#         subject = all_subject[idx].format(**dicts)
#         print(dicts)
#         print(message)
#     # Get each records name, email, subject and message
#         sheet_name = all_names[idx]
#         email = all_emails[idx]
        

#         msg=f"Dear {sheet_name},\n"


#         # Create the email to send
#         full_email = ("From: {0} <{1}>\n"
#                       "To: {2} <{3}>\n"
#                       "Subject: {4}\n\n"
#                       "{5}{6}"
#                       .format(name, your_email, sheet_name, email, subject, msg, message))#name change

#         # In the email field, you can add multiple other emails if you want
#         # all of them to receive the same text
#         try:
#             server.sendmail(your_email, [email], full_email)
#             res.append(f' --> Email to {name},{email} successfully sent!')
#             time.sleep(1)
#         except Exception as e:
#             res.append('Email to {} could not be sent--------------------------------------------------------------because {}'.format(name, str(e)))
            
#     return res    

# def send_email_static(mail,apppass,name,sheet_id,sheet_name):
#     res=[]
#     your_password =apppass
#     your_email = mail

#     server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#     server.ehlo()
#     server.login(your_email, your_password) 
    

#     url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
#     email_list=pd.read_csv(url)

#     all_names = email_list.loc[:,'NAME']
#     all_emails = email_list['MAIL']
#     all_messages=email_list['MESSAGE']
#     all_subject = email_list['SUBJECT']

#     for idx in range(len(all_emails)):
#     # Get each records name, email, subject and message
#         sheet_name = all_names[idx]
#         email = all_emails[idx]
#         message = all_messages[idx]
#         subject = all_subject[idx]

#         msg=f"Dear {sheet_name},\n"


#         # Create the email to send
#         full_email = ("From: {0} <{1}>\n"
#                       "To: {2} <{3}>\n"
#                       "Subject: {4}\n\n"
#                       "{5}{6}"
#                       .format(name, your_email, sheet_name, email, subject, msg, message))#name change

#         # In the email field, you can add multiple other emails if you want
#         # all of them to receive the same text
#         try:
#             server.sendmail(your_email, [email], full_email)
#             res.append(f' --> Email to {name},{email} successfully sent!')
#             time.sleep(1)
#         except Exception as e:
#             res.append('Email to {} could not be sent--------------------------------------------------------------because {}'.format(name, str(e)))
            
#     return res