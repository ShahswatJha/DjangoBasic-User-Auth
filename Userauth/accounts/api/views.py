from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view,permission_classes
from accounts.api.serializers import UserRegistrationSerializer
from rest_framework.authtoken.models import Token
#from rest_framework.permission import IsAuthenticated


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Succesfully Registered."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get_ot_create(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

