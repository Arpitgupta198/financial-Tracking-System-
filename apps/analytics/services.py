from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.transcations.services import calculate_summary

class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = calculate_summary(request.user)
        return Response(data)