from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import C_details,C_history

from django.contrib import messages
import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')

def customers(request):
    allcustomers= C_details.objects.all()
    
    context= {'allcustomers': allcustomers}
    if request.method=="POST":
        #a = request.method
        try:
            # Fetching data from customer table from the user 
            cname = request.POST['cname']
            cid = request.POST['cid']
            context['fetched_name'] = cname
            context['fetched_id'] = cid
        except:
            #fetching details from t_money 
            senderId = int(request.POST['senderId'])
            senderName = request.POST['senderName']

            context['fetched_name'] = senderName
            context['fetched_id'] = senderId

            receiverName = request.POST['receiverName']
            receiverId = int(request.POST['receiverId'])

            credits = int(request.POST['credits'])

            print(receiverName,receiverId,credits,senderId,senderName)

            r = C_details.objects.filter(c_id=receiverId)
            print(r.values_list())
            if (list(r.values_list())[0][2]) == receiverName:
                #updating transaction in the database
                balr = list(r.values_list())[0][4] + credits
                bals = list(r.values_list())[0][4] - credits
                C_details.objects.filter(c_id=senderId).update(c_balance=bals)
                C_details.objects.filter(c_id=receiverId).update(c_balance=balr)

                #adding histories 
                c_history= C_history(s_id=senderId,s_name=senderName,r_id=receiverId,r_name=receiverName,t_date=datetime.datetime.now(),transaction=credits)
                c_history.save()


            else:
                messages.info(request, 'No Receiver on the given Receiver ID, Please Enter correct information.')
                return render(request,'t_money.html',context)
            messages.info(request, 'Last Transaction was successful , You can start next transaction now.')
            return render(request,'customers.html',context)

        #C_details.objects.filter(c_name='hii').update(c_balance=11000)
        #print(context['allcustomers'].values_list())


        #rendering t_money after choosing the sender
        #return t_money(request,context) #this way can be done
        return render(request,'t_money.html',context)
    else:
        return render(request,'customers.html',context)


def t_money(request,context):
    return render(request,'t_money.html',context)

def history(request):
    c_history= C_history.objects.all().order_by('t_date').reverse()
    context= {'c_history': c_history}
    return render(request,'history.html',context)

def about(request):
    return render(request,'about.html')

