from django.db import models

from wagtail.models import Page


class HomePage(Page):
    template = "home/home_page.html"