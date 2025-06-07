from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms

from . import util

class newForm(forms.Form):
    title = forms.CharField(label="Page_Title", max_length=150)
    content = forms.CharField(label="Content", max_length=5000, widget=forms.Textarea(attrs={'rows': 10, 'cols':60}))


def index(request):
    if request.method == 'POST':
        searchValue = request.POST['q'].strip()
        for iten in util.list_entries():
            if searchValue.lower() == iten.lower():
                return HttpResponseRedirect(reverse('encyclopedia:view', args = [iten]))
            
        entries =[]
        for iten in util.list_entries():
            if searchValue.lower() in iten.lower():
                entries += [iten]

        return render(request, "encyclopedia/results.html",{
            'entries':entries,
            'searchValue': searchValue
        })

        
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def view(request, name):
    view = util.get_entry(f"{name}")

    if view == None:
        origin = 'view'
        return render(request, "encyclopedia/error.html", {
            "title":name,
            'origin':origin
        })
    return render(request, "encyclopedia/view.html", {
        "title":name,
        "view":view
    })

def add(request):

    if request.method == 'POST':
        form = newForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            addResult = util.save_entry(title, content)
            if addResult == None:
                origin = 'add'
                return render(request, 'encyclopedia/error.html', {
                    'origin':origin
                })

            else:
                return HttpResponseRedirect(reverse("encyclopedia:view", args = [title]))
    else:
        form = newForm()
        return render(request, "encyclopedia/add.html", {
            "form":form
        })
