from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializers
    ##serializer_class = serializers.HelloSerializers
    
    def get(self, request, format=None):
        """Return a list APIview Feature"""
        an_apiview = [
            'Uses HTTP methods as function (get, psot, patch, put, delete)',
            'Is similer to a Django view',
            'Gives  you the most control over you application',
            'Is mapped manually to URLs'
        ]

        return Response({'Msg': 'Hello', 'an_apiview': an_apiview})


    def post(self, request):
        
        """Create a hello msg with our name"""
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'hello {name}'
            return Response({'msg': msg})
        else:
            return Response(
                serializer.errors, 
                status= status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handle upadte an object"""
        return Response({'MSg': 'Put request method'})

    def patch(self, request, pk=None):
        """Handle upadte an object"""
        return Response({'MSg': 'Patch request method'})

    def delete(self, request, pk=None):
        """Handle delte request"""
        return Response({'Msg': "Delete request method"})