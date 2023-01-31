from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializers

def drink_list(request):

  # get all the drinks 
  # serialize them
  # return json 

  drinks = Drink.objects.all()
  serializer = DrinkSerializers(drinks, many = True)
  return JsonResponse(serializer.data)
