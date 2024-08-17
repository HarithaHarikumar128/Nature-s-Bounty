"""
URL configuration for fruits project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.base),
    path('BASEE',views.BASEE),
    path('search',views.search),

    path('adbase',views.adbase),
    path('',views.index1),
    path('frreg',views.frreg),
    path('usrreg',views.usrreg),
    path('contact',views.contact),
    path('aboutus',views.aboutus,name='aboutus'),
    path('adlog',views.adlog),
    path('adlogout',views.adlogout),
    path('farmlog',views.farmlog,name='farmlog'),
    path('forgotfarm',views.forgotfarm),
    path('resetfarm/<token>',views.reset_passwordfarm,name='reset_passwordfarm'),
    path('usrlog',views.usrlog),
    path('forgotusr',views.forgotusr),
    path('resetuser/<token>',views.reset_passworduser,name='reset_passworduser'),
    path('index',views.index),
    path('adindex',views.adindex),
    path('gallery',views.gallery),
    path('account',views.account),
    path('checkout',views.checkout),
    path('delivery/<int:id>',views.delivery,name='delivery'),
    path('deliveries/<int:id>',views.deliveries,name='deliveries'),



    path('msg',views.msg,name='msg'),

    path('frbase',views.frbase),
    path('frindex',views.frindex),
    path('addpro',views.addpro),
    path('mngpro',views.mngpro,name='mngpro'),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete),
    path('fpay',views.fpay),
    path('farmlogout',views.farmlogout),
    path('usrbase',views.usrbase),
    path('usrindex',views.usrindex,name='usrindex'),
    path('usrlogout',views.usrlogout),
    path('usrdisplay',views.usrdisplay,name='usrdisplay'),
    path('usrdisplay2/<int:id>',views.usrdisplay2,name='usrdisplay2'),
    path('empty',views.empty,name='empty'),
    path('myacc',views.myacc,name='myacc'),
    path('order',views.order,name='order'),
    path('uedit/<int:id>',views.uedit,name='uedit'),

    path('addtocart/<int:id>',views.addtocart),
    path('buynow',views.buynow),
    # path('mycart',views.mycart,name='mycart'),
    path('mycart1',views.mycart1,name='mycart1'),

    path('pluscart/<int:id>',views.pluscart),
    path('minuscart/<int:id>',views.minuscart),
    path('delete_c/<int:id>',views.delete_c),
    path('buynow/<int:id>',views.buynow,name='buynow'),
    path('mybuy/<int:id>',views.mybuy,name='mybuy'),
    path('plusbuy/<int:id>',views.plusbuy,name='plusbuy'),
    path('minusbuy/<int:id>',views.minusbuy,name='minusbuy'),
    path('create/',views.create_payment,name='create_payment'),
    # path('callback/',views.payment_callback,name='payment_callback'),
    path('success',views.success,name='success'),
    path('cart_payment/',views.cart_payment,name='cart_payment'),
    path('csuccess',views.csuccess,name='csuccess'),

    path('fmsg',views.fmsg,name='fmsg'),
    path('admsg',views.admsg),
    path('cmsg',views.cmsg),
    path('usrply/<int:id>',views.usrply,name='usrply'),
    path('adshare/<int:id>',views.adshare,name='adshare'),



    path('usrview',views.usrview),
    path('frview',views.frview),
    path('approve/<int:id>',views.approve),
    path('reject/<int:id>',views.reject),
    path('prodisp',views.prodisp),
    path('adpay',views.adpay),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
