from rest_framework.views import APIView
from .models import *
from invoice_app.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class InvoiceView(APIView):
    serializer_class = InvoiceSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class InvoiceDetail(APIView):
    serializer_class = InvoiceDetailsSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        invoices = InvoiceDetails.objects.all()
        serializer = InvoiceDetailsSerializer(invoices, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InvoiceDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
