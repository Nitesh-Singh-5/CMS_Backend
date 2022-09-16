from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from base.models import VerificationModel
from base.serializers import RoomSerializer,verificationSerializer


class verificationProfile(viewsets.ModelViewSet):
    queryset = VerificationModel.objects.all()
    serializer_class = verificationSerializer


