from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from openai import OpenAI
from django.conf import settings
from .serializers.common import CoverLetterRequestSerializer, CoverLetterResponseSerializer
import logging

logger = logging.getLogger(__name__)
client = OpenAI(api_key=settings.OPENAI_API_KEY)

#openai.api_key = settings.OPENAI_API_KEY

class GenerateCoverLetterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request_serializer = CoverLetterRequestSerializer(data=request.data)
        if request_serializer.is_valid():
            data = request_serializer.validated_data
            job_title = data['job_title']
            company = data['company']
            jd_url = data['jd_url']
            professional_bio = data['professional_bio']

            prompt = f"""
            Generate a cover letter for a {job_title} position at {company}.
            Job Description URL: {jd_url}
            Candidate's Professional Bio: {professional_bio}

            The cover letter should be professional, engaging, and tailored to the specific job and company.
            Highlight relevant skills and experiences from the professional bio that match the job requirements.
            """

            try:
                client = OpenAI(api_key=settings.OPENAI_API_KEY)
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that generates cover letters."},
                        {"role": "user", "content": prompt}
                    ]
                )

                cover_letter = response.choices[0].message.content.strip()
                
                response_serializer = CoverLetterResponseSerializer(data={'cover_letter': cover_letter})
                if response_serializer.is_valid():
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                else:
                    logger.error(f"Response serializer errors: {response_serializer.errors}")
                    return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as e:
                logger.error(f"Error generating cover letter: {str(e)}")
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            logger.error(f"Request serializer errors: {request_serializer.errors}")
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

generate_cover_letter = GenerateCoverLetterView.as_view()