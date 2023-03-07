from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


from rest_framework import viewsets

#from video 45
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters

#from video 55
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

#from video 59
from rest_framework.permissions import IsAuthenticatedOrReadOnly



# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,  post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',

        ]
        return Response({'message':'hello', 'an_apiview':an_apiview})


    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})



    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})



#===============================================================================
class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """return hello mesage"""
        a_viewset = [
            "uses actions (list, create, retrieve, update, partial_update)",
            "automatically maps to urls using routers",
            "provides more functionally with less code",
        ]
        return Response({'message': 'hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return  Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handle update an object """
        return  Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part of an object"""
        return  Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing an object by its ID"""
        return  Response({'http_method': 'DELETE'})


#===============================================================================
#from video 45
class UserProfileViewSet(viewsets.ModelViewSet):
    """handel creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    #search options
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


#===============================================================================
#from video 55

class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

#===============================================================================
#from video 59
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    #from permissions
    permission_classes = {
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    }



    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
