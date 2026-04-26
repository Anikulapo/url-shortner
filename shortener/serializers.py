from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    url = serializers.URLField(write_only=True)

    class Meta:
        model = URL
        fields = ['url', 'short_code']
        read_only_fields = ['short_code']

    def create(self, validated_data):
        return URL.objects.create(
            original_Url=validated_data['url'],
            short_code=self.context['short_code']
        )