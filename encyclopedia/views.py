from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util


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
        return render(request, "encyclopedia/error.html", {
            "title":name
        })
    return render(request, "encyclopedia/view.html", {
        "title":name,
        "view":view
    })
