from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer

@api_view(['POST'])
def upload_document(request):

    serializer = DocumentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Document Uploaded"})

    return Response(serializer.errors)


@api_view(['GET'])
def document_list(request):

    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)

    return Response(serializer.data)


@api_view(['PUT'])
def verify_document(request, id):

    document = Document.objects.get(id=id)

    document.status = request.data.get('status')
    document.save()

    return Response({"message": "Document Verified"})