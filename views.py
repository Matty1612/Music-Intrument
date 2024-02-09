from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.method == 'POST':
        instrument = request.POST["instrument"]
        if 'real' in request.POST:
            return HttpResponseRedirect(reverse(f"real-{instrument}"))
        if 'upload' in request.POST:
            return HttpResponseRedirect(reverse(f"upload-{instrument}"))
    return render(request, "airstrument/index.html")


def instruments(request):
    return render(request, "airstrument/instruments.html")


def real_drums(request):
    return render(request, "airstrument/real_drums.html")


def real_trumpet(request):
    return render(request, "airstrument/real_trumpet.html")


def real_trombone(request):
    return render(request, "airstrument/real_trombone.html")


def real_xylophone(request):
    return render(request, "airstrument/real_xylophone.html")


def real_cymbal(request):
    return render(request, "airstrument/real_cymbal.html")


def real_piano(request):
    return render(request, "airstrument/real_piano.html")


def real_guitar(request):
    return render(request, "airstrument/real_guitar.html")


def skeleton(request):
    return render(request, "airstrument/skeleton.html")


def about(request):
    return render(request, "airstrument/about.html")


def team(request):
    return render(request, "airstrument/team.html")
