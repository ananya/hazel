from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView
from .views import (
    repo_create,
	code_list,
	submit_model,
	test_model,
	)
app_name = "nucleus"

urlpatterns = [
	url(r'^create/$',repo_create,name="create"),
	url(r'^(?P<id>\d+)', code_list,name="list"),
	url(r'submit/$', submit_model,name="submit"),
	url(r'test/$', test_model,name="test"),
	]
