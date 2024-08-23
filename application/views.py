from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Application
from .serializers.common import ApplicationSerializer
from aipplicant.utils.decorators import handle_exceptions

# Create your views here.
class ApplicationListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @handle_exceptions
    def get(self, request): #working tested on postman
        application = Application.objects.filter(owner=request.user)
        serialized_application = ApplicationSerializer(application, many=True)
        return Response(serialized_application.data)
    
    @handle_exceptions
    def post(self, request): #working test on postman
        request.data['owner'] = request.user.id
        create_application = ApplicationSerializer(data=request.data)
        if create_application.is_valid():
            create_application.save()
            return Response(create_application.data, 201)
        print('Validation Error', create_application.errors)
        return Response(create_application.errors, 400)
    

class ApplicationRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsAuthenticated]

    def get_application(self, id, user):
        try:
            application = Application.objects.get(pk=id, owner=user)
        except Application.DoesNotExist:
            raise NotFound('Application not found')
        return application
    
    @handle_exceptions
    def get(self, request, id): #working tested on postman
        application = self.get_application(id, request.user)
        serialized_application = ApplicationSerializer(application)
        return Response(serialized_application.data)
    

    @handle_exceptions
    def put(self, request, id): #working tested on postman
        application = self.get_application(id, request.user)
        serialized_application = ApplicationSerializer(application, data=request.data, partial=True)
        if serialized_application.is_valid():
            serialized_application.save()
            return Response(serialized_application.data)
        return Response(serialized_application.errors, 400)
    

    @handle_exceptions
    def delete(self, request, id): #working tested on postman
        application = self.get_application(id, request.user)
        application.delete()
        return Response(status=204)