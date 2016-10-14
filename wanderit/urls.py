"""wanderit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls import url, include
from django.contrib import admin

import main
from main.views import HomeView, ComingSoonView
from searchreports.views import ReportDetailView, SearchReportDetailView
from travelrequests.views import UserDestinationRequestCreateView, UserDatesRequestCreateView

urlpatterns = [
    url(r'^$', ComingSoonView.as_view()),
    url(r'^home/$', HomeView.as_view()),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^report/(?P<pk>\d+)/$', ReportDetailView.as_view()),
    url(r'^searchreport/(?P<pk>\d+)/$', SearchReportDetailView.as_view()),
    url(r'^destination/add/$', UserDestinationRequestCreateView.as_view(), name='destination-add'),
    url(r'^dates/add/$', UserDatesRequestCreateView.as_view(), name='dates-add'),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
