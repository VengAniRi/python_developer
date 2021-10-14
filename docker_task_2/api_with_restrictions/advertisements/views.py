from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from django_filters import rest_framework as filters
from advertisements.filters import AdvertisementFilter
from rest_framework.serializers import ValidationError
from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.select_related('creator').all()
    serializer_class = AdvertisementSerializer

    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [permissions.IsAuthenticated()]
        if self.action in ["destroy", "update", "partial_update"]:
            return [permissions.IsAuthenticated(), IsOwner()]
        return []
