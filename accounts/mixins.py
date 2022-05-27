from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

class LoginMixin():  
    @action(detail=False, methods=["post"])
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': { 'email': user.email,
                        'first_name': user.first_name, 
                        'last_name': user.last_name },
        })