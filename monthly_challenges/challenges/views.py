from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    "january":"Eat no meat for the entire month!",
    "february": "Walk at least 10,000 steps every day!",
    "march": "Read one book this month!",
    "april": "Drink 2 liters of water daily!",
    "may": "Wake up before 6:30 AM every day!",
    "june": "Avoid sugar for the entire month!",
    "july": "Do a random act of kindness each week!",
    "august": "Spend 30 minutes learning something new daily!",
    "september": "No social media during weekdays!",
    "october": "Write a journal entry every day!",
    "november": "Meditate for 10 minutes daily!",
    "december": "Reflect on your year and plan your goals!"
}
# Create your views here.

def index_fun(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)



def challenges_fun_num(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    forward_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)



def challenges_fun(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html",{
            "text" : challenge_text,
            "month" : month
        })
        # response_data = render_to_string("challenges/challenges.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    