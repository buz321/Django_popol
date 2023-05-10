from django.shortcuts import render

# Create your views here.
# ~/webpage/views.py

from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        return render(request, "index.html")