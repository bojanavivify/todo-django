from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from core.serializers import TodoSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=True, url_name='todos', permission_classes=[IsAuthenticated])
    def todos(self, request, pk=None):
        user = User.objects.get(pk=pk)
        queryset = user.todos.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)



