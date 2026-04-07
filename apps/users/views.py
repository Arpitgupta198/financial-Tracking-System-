from rest_framework.response import Response
from .serializer import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    def post(self,request):
        permission_classes = [IsAuthenticated]
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response({
                "status":True,
                "messages":"Register succesfully",
                "data":serializer.data
            })



