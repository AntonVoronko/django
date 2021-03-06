"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from qa.views import test, question_list, popular_questions, question_detail, question_add, answer_add, signup, login_user

urlpatterns = [
    url(r'^$', question_list, name='main'),
    url(r'^popular/$', popular_questions),
    url(r'^question/(?P<id>\d+)/$', question_detail),
    url(r'^login/', login_user),
    url(r'^signup/', signup),
    url(r'^answer/$', answer_add),
    url(r'^ask/', question_add),
    url(r'^new/', test),
]
