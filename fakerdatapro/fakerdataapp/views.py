from django.http import HttpResponse
from django.shortcuts import render
from .models import FakerData
import faker
fake = faker.Faker()
def mainPage(request):
    if request.method == "GET":
            return render(request, 'mainpage.html')
    else:
        hall=request.POST.get("hall_ticket")
        print(hall)
        data = FakerData.objects.get(hall_ticket = hall)
        return render(request, 'resultspage.html',{'data':data})

def resultsPage(request):
    for i in range(10):
        fname1 = fake.first_name()
        lname1 = fake.last_name()
        telugu1 = fake.random_int(min=0, max=100)
        hindi1 = fake.random_int(min=0, max=100)
        english1 = fake.random_int(min=0, max=100)
        maths1 = fake.random_int(min=0, max=100)
        science1 = fake.random_int(min=0, max=100)
        social1 = fake.random_int(min=0, max=100)
        hall_ticket1 = fake.unique.random_int(min=1000, max=2000)
        FakerData(
                    first_name = fname1,
                    last_name = lname1,
                    telugu = telugu1,
                    hindi = hindi1,
                    english = english1,
                    maths = maths1,
                    science = science1,
                    social = social1,
                    hall_ticket = hall_ticket1
                ).save()
    return HttpResponse('Data Saved!!!')
