from rest_framework import serializers

class CoverLetterRequestSerializer(serializers.Serializer):
    job_title = serializers.CharField(max_length=200)
    company = serializers.CharField(max_length=200)
    jd_url = serializers.URLField()
    professional_bio = serializers.CharField()

class CoverLetterResponseSerializer(serializers.Serializer):
    cover_letter = serializers.CharField()