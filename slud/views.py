from slud.serializers import SpeakerSerializer
from rest_framework import viewsets #conjunto de vistas
from slud.models import Speaker
from rest_framework import permissions

class SpeakerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        else:
            return (permissions.IsAuthenticatedOrReadOnly(),)