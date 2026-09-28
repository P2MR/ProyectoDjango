from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario
from django.shortcuts import get_object_or_404
from .serializers import UsuarioSerializer


@api_view(['GET', 'POST'])
def lista_usuarios(request):

    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

@api_view(['GET', 'PATCH', 'DELETE'])
def detalle_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'PATCH':
        serializer = UsuarioSerializer(usuario, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        usuario.delete()
        return Response(status=204)