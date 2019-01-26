from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
user_list = [
    {"user": "jack", "pwd": "abc"},
    {"user": "tom", "pwd": "ABC"},
]


def index(request):
    # request.POST
    # request.Get
    # return HttpResponse("hello world!")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        tmp = {"user": username, "pwd": password}
        user_list.append(tmp)
    return render(request, "index.html", {"data": user_list})
