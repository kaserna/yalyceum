import re
from django.http import HttpResponse
from django.utils.timezone import datetime
from django.shortcuts import render

# Create your views here.


def hi(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    # match_object = re.match("[a-zA-Z]+", name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"

    content = "Привет " + name + "! Сейчас" + formatted_now
    return HttpResponse(content)
