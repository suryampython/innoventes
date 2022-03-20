"""innoventes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from inncomapp import views
from inncomapp.views import Company_all,CompanySinglecud,CompanyPagenation

urlpatterns = [
    #path('company_list/', views.company_list),
    #path('company/<int:pk>/', views.update_detail),
    path('company/', Company_all.as_view()),
    path('company/<int:id>/', CompanySinglecud.as_view()),
    path('companypagenation/', CompanyPagenation.as_view()),

]
