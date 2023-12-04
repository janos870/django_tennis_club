from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MemberForm
from django.template import loader
from .models import Member
from django.utils import timezone


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        "mymembers": mymembers
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        "mymember": mymember
    }
    return HttpResponse(template.render(context, request))


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.joined_date = timezone.now()
            member.save()
            return redirect('members')
    else:
        form = MemberForm()

    template = loader.get_template('add_member.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))
