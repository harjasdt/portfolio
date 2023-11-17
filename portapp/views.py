from django.shortcuts import render,redirect

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import AllowAny


import smtplib
import time
import pandas as pd
from datetime import datetime
from csv import writer
from portapp.models import QUESTION,HISTORY,DOOR,DOORFAIL,ACTIVE,TEMP
from django.http import JsonResponse


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import numpy as np
model_filename = "naive_bayes_model.sav"
model = joblib.load(model_filename)

dict={0: 'apple',
 1: 'banana',
 2: 'blackgram',
 3: 'chickpea',
 4: 'coconut',
 5: 'coffee',
 6: 'cotton',
 7: 'grapes',
 8: 'jute',
 9: 'kidneybeans',
 10: 'lentil',
 11: 'maize',
 12: 'mango',
 13: 'mothbeans',
 14: 'mungbean',
 15: 'muskmelon',
 16: 'orange',
 17: ' papaya',
 18: 'pigeonpeas',
 19: 'pomegranate',
 20: 'rice',
 21: 'watermelon'}


def help():
    data=QUESTION.objects.last()
    x=np.array([[data.temp, data.ph, data.mos, data.n, data.p, data.k]])
    ans=model.predict(x)
    currentDateAndTime = datetime.now()
    time = currentDateAndTime.strftime("%h:%m")
    data=HISTORY(time=currentDateAndTime,crop=dict[int(ans)])
    data.save()

def history(request):
    # help()
    data=HISTORY.objects.all().order_by('-time').values()
    context={
        "data":data
    }
    return render(request,'final/history.html',context)

def predhistory(request):
    help()
    data=HISTORY.objects.all().order_by('-time').values()
    context={
        "data":data
    }
    return render(request,'final/history.html',context)

def home(request):
    data=QUESTION.objects.last()
    print(data)
    context={"data":data}

    return render(request,'final/home.html',context)

def clear(request):
    QUESTION.objects.all().delete()

    return redirect('/')



import math
@api_view(['GET'])
def getting(request):
    data=QUESTION.objects.last()
    context={
        "temp":data.temp,
        "ph":data.ph,
        "mos":data.mos,
        "n":data.n,
        "p":data.p,
        "k":data.k
    }

    return Response(context)

import math
@api_view(['GET'])
def test(request):
    # time=request.query_params['time']
    temp=request.query_params['temp']
    ph=request.query_params['ph']
    mos=request.query_params['mos']
    n=request.query_params['n']
    p=request.query_params['p']
    k=request.query_params['k']
    currentDateAndTime = datetime.now()

    time = int(currentDateAndTime.strftime("%M%S"))

    data=QUESTION(time=time,temp=temp,ph=ph,mos=mos,n=n,p=p,k=k)
    data.save()
    # with open('event.csv', 'a') as f:
    #     f.write(f'last update at {datetime.datetime.now()} ans {x} \n')

    return Response("temp received")



# ----------------------------------------------------------------------------------------------------------------------

def securehome(request):
    data=DOOR.objects.last()
    

    context={"data":data,
             }

    return render(request,'safe.html',context)

@api_view(['GET'])
def doorstatus(request):
    temp=TEMP.objects.last()
    data=DOOR.objects.last()
    currentDateAndTime = datetime.now()
    now = str(currentDateAndTime.strftime("%H:%M:%S"))
    start = datetime.strptime(data.time, "%H:%M:%S") 
    end = datetime.strptime(now, "%H:%M:%S") 
    difference = end - start 

    state = difference.total_seconds()
    print(state)
    active=ACTIVE.objects.last()
    if(state>10):
        state=0
    else:
        state=1
    context={
        "d1":data.d1,
        "d2":data.d2,
        "time":data.time,
        "temp":temp.temp,
        "state":state,
        "active":active.active,
    }

    return Response(context)

@api_view(['GET'])
def updatestatus(request):
    # time=request.query_params['time']
    d1=int(request.query_params['d1'])
    d2=int(request.query_params['d2'])
    currentDateAndTime = datetime.now()
    time = str(currentDateAndTime.strftime("%H:%M:%S"))
    lastdata=DOOR.objects.last()

    lastdata.time=time
    lastdata.d1=d1
    lastdata.d2=d2

    lastdata.save()
    # with open('event.csv', 'a') as f:
    #     f.write(f'last update at {datetime.datetime.now()} ans {x} \n')

    return Response("Existing Status Updated")

@api_view(['GET'])
def newstatus(request):
    # time=request.query_params['time']
    d1=int(request.query_params['d1'])
    d2=int(request.query_params['d2'])
    currentDateAndTime = datetime.now()
    time = str(currentDateAndTime.strftime("%H:%M:%S"))

    data=DOORFAIL(time=time,d1=d1,d2=d2)
    

    data.save()
    # with open('event.csv', 'a') as f:
    #     f.write(f'last update at {datetime.datetime.now()} ans {x} \n')

    return Response("NEW FAIL DATA SAVED")


@api_view(['GET'])
def reqactive(request):
    data=ACTIVE.objects.last()
    # context={
    #     "active":data.active
    # }

    return Response(data.active)

def changeactive(request):
    data=ACTIVE.objects.last()
    if(data.active == 1):
        data.active=0
    else:
        data.active=1

    data.save()
    
    return redirect ("/security")

def failhistory(request):
    data=DOORFAIL.objects.all().order_by('-time').values()
    context={
        "data":data
    }
    return render(request,'failhistory.html',context)

@api_view(['GET'])
def sendtemp(request):
    # time=request.query_params['time']
    temp=request.query_params['temp']
    currentDateAndTime = datetime.now()
    time = str(currentDateAndTime.strftime("%H:%M:%S"))
    lastdata=TEMP.objects.last()

    lastdata.activatetime=time
    lastdata.temp=temp

    lastdata.save()
    return Response("Internal Temp Updated")
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