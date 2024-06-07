from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentFilter(FilterSet):
    class Meta:
        model = Payment
        fields = ["course", "lesson", "payment_method"]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PaymentFilter
    ordering_fields = ["payment_date"]
    ordering = ("-payment_date",)
