from django.shortcuts import render, render_to_response


# Create your views here.
from hw_app.models import FantasyStat


def index_view(request):
    return render_to_response("index.html", {})


def about_me_view(request):
    return render_to_response("about_me.html", {})


def detailed_info_view(request):
    players = FantasyStat.objects.all()
    return render_to_response("detailed_info.html", {"stats": players})
