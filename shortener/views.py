from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import URL
from .serializers import URLSerializer
import random
import string
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.
class CreateShortURL(APIView):

    def generate_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=7))

    @swagger_auto_schema(request_body=URLSerializer)
    def post(self, request):
        long_url = request.data.get("url")

        if not long_url:
            return Response(
                {"error": "URL is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if URL already exists
        existing = URL.objects.filter(original_Url=long_url).first()

        if existing:
            return Response({
                "short_code": existing.short_code,
                "short_url": f"https://url-shortner-dbau.onrender.com/{existing.short_code}"
            }, status=status.HTTP_200_OK)

        # Generate unique short code
        short_code = self.generate_code()

        while URL.objects.filter(short_code=short_code).exists():
            short_code = self.generate_code()

        # Save using serializer
        serializer = URLSerializer(
            data={"url": long_url},
            context={"short_code": short_code}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "short_code": short_code,
            "short_url": f"https://url-shortner-dbau.onrender.com/{short_code}"
        }, status=status.HTTP_201_CREATED)

class RedirectURL(APIView):
    def get(self, request, code):
        url = get_object_or_404(URL, short_code=code)
        return redirect(url.original_Url)

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)