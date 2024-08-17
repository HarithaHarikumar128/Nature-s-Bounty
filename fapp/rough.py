# In mycaert1:
c=re
      sum=[]
      l=0
      d=addproduct.objects.all()
      t=0

      sub={}
      su=re
      for i in su:
        sub[i.cartitm]=[i.count,i.cartitm.price*i.count,i.tprice]
      print(sub)
      for i in c:
        t=t+(i.cartitm.price*i.count)
      for i in sub:
        sum.append(sub[i])
      print(sum)
    #   print(r.session['user']['name'])
      return render(r,'mycart1.html',{'st':re ,'total':t,'sub':sub,'cl':sub,'d':d})

 # btn=request.POST.get('cod',0)
            # if btn=='Procced':
            #     location=request.POST.get('location')
            #     pincode=request.POST.get('pincode')
            #     rpamount = int(request.POST['amount'])  # Razorpay amount in paisa
            #     pdctid=int(request.POST['pdctid'])
            #     print(pdctid)                
            #     request.session['payment']={'amount':rpamount,'location':location,'pincode':pincode,'pdctid':pdctid}
            #     return render(request, 'cod.html',{'amount': amount})
            # else:




def replymaill(request,d):
    datas=Feedback.objects.filter(pk=d)
    return render(request,'replymail.html',{'datas':datas})
def repl(request):
    if request.method == 'POST':
        email=request.POST['email']
        z='ekartqwe@gmail.com'
        re=request.POST['message']
        send_mail('Ekart Message', f'{email},{re}','settings.EMAIL_HOST_USER',[z],fail_silently=False)
    return redirect(admin)


def plusbuy(r,id):
    if 'user' in r.session:
        p=buy.objects.get(pk=id)
        print(p)
        p.qty = p.qty + 1
        p.totprice=p.buyitm.price*p.qty
        p.save()
    return redirect(buynow)




# bootsnav.css-523line

  # nav.navbar.bootsnav ul.nav > li.dropdown > a.dropdown-toggle:after{
  #       font-family: 'FontAwesome';
  #       content: "\f0d7";
  #       margin-left: 5px;
  #       margin-top: 2px;
  #   }









    <!DOCTYPE html>
<html>
<head>
    <title>Payment</title>
</head>
<body>
    <h1>Scan the QR Code to Pay</h1>
    <img src="data:image/png;base64,{{ qr_image|b64encode }}" alt="QR Code">
</body>
</html>