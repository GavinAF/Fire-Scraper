from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Link

# Create views here.

@login_required(login_url="/")
def dashboard(response):

    if response.user.is_authenticated:
        user = response.user
        username = response.user.username

    link_count = Link.objects.all().filter(owner=user).count()

    return render(response, "dashboard/dashboard.html", {"username":username, "link_count":link_count})

@login_required(login_url="/")
def profile(response):
    return render(response, "dashboard/user.html", {})

@login_required(login_url="/")
def view_links(response):

    if response.user.is_authenticated:
        user = response.user
        username = response.user.username

    links = Link.objects.all().filter(owner=user)

    return render(response, "dashboard/view.html", {"username":username, "links":links})

@login_required(login_url="/")
def create(response):

    if response.user.is_authenticated:
        user = response.user

    if response.method == "POST":
        if "add_link" in response.POST:
            new_company = response.POST.get("company", "")
            new_product = response.POST.get("product_name", "")
            new_url = response.POST.get("url", "")
            new_threshold = response.POST.get("threshold", "")

            link_add = Link(url=new_url, store=new_company, threshold=new_threshold, active="True", title=new_product, owner=user)
            link_add.save()

            return HttpResponse("")

@login_required(login_url="/")
def delete(response):

    if response.user.is_authenticated:
        user = response.user

    if response.method == "POST":
        if "delete_link" in response.POST:

            linkid = response.POST.get("linkid", "")

            Link.objects.all().filter(owner=user).get(pk=linkid).delete()

    return HttpResponse("")

@login_required(login_url="/")
def modal(response, linkid):

    if response.user.is_authenticated:
        user = response.user

    
    instance = get_object_or_404(Link.objects.all().filter(owner=user), pk=linkid)
    context={
        'instance':instance
    }
    
    return render(response, "dashboard/modal.html", context)

@login_required(login_url="/")
def update(response):

    if response.user.is_authenticated:
        user = response.user

    if response.method == "POST":
        if "update_link" in response.POST:
            id_link = response.POST.get("linkid", "")
            new_company = response.POST.get("company", "")
            new_product = response.POST.get("product_name", "")
            new_url = response.POST.get("url", "")
            new_threshold = response.POST.get("threshold", "")

            link_modify = Link.objects.all().filter(owner=user).get(pk=id_link)

            link_modify.store = new_company
            link_modify.title = new_product
            link_modify.url = new_url
            link_modify.threshold = new_threshold

            link_modify.save()
    
    return HttpResponse("")

@login_required(login_url="/")
def update_table(response):

    if response.user.is_authenticated:
        user = response.user

    links = Link.objects.all().filter(owner=user)

    return render(response, "dashboard/update_table.html", {"links":links})