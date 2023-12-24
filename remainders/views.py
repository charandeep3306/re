from django.shortcuts import render
import random

# Create your views here.
def remainders(request):
    num = random.randint(1, 100)
    for i in range(2, 10):
        remainder = num % i
        return render(request,'index.html', {'num': num,'remainder': remainder})