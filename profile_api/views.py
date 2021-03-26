from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from profile_api import serializers
from profile_api import models
from profile_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """Return a hello msg"""
        a_viewset = [
            'Uses action (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'msg': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello msg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hello {name}!'
            return Response({'msg': msg})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        """Handle object by its id"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PTACH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)