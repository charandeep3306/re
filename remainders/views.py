from django.shortcuts import render 
import random

def remainders_view(request):

  # Generate random number
  num = random.randint(1, 2500)
  
  remainders = []

  # Calculate remainders 
  for divisor in range(2, 10):
    remainder = num % divisor
    remainders.append(remainder)

  context = {
    'num': num,
    'remainders': remainders,
  }

  return render(request, 'index.html', context)
