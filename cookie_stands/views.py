from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandSerializer
from .forms import CreateAPIForm


class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer

    # custom form that dont have owner field
    form_class= CreateAPIForm
    # save the ouner automatically
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
