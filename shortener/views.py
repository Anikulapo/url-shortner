from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import URL
import random
import string
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your views here.
class CreateShortURL(APIView):
    def post(self, request):
        long_url = request.data.get("url")
        if not long_url:
            return Response({"error": "Long URL is required."}, status=status.HTTP_400_BAD_REQUEST)
        validator = URLValidator()
        try:
            validator(long_url)
        except ValidationError:
            return Response({"error": "Invalid URL format."}, status=status.HTTP_400_BAD_REQUEST)
        existing = URL.objects.filter(original_Url=long_url).first()

        if existing:
            return Response({
                            "short_code": existing.short_code,
                            "short_url": f"http://127.0.0.1:8000/{existing.short_code}"
                            }, status=status.HTTP_200_OK)
        
        def generate_short_code():
            return ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        short_code = generate_short_code()
        while URL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()
        URL.objects.create(original_Url=long_url,short_code=short_code)

        return Response({ "short_code": short_code,
                        "short_url": f"http://127.0.0.1:8000/{short_code}"
                        }, status=status.HTTP_201_CREATED)



class RedirectURL(APIView):
    def get(self, request, code):
        url = get_object_or_404(URL, short_code=code)
        return redirect(url.original_Url)
