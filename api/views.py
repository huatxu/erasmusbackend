from django.shortcuts import render


from api.models import Comida, Cerveza, Titulo, TipoComida
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
import csv
import os

class CervezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cerveza
        fields = ['id', 'nombre', 'estilo', 'pais', 'pais_ingles', 'alcohol', 'color', 'amargor', 'descripcion', 'descripcion_ingles', 'disponible', 'imagen', 'artesanal', 'tipo', 'recomendada', 'formato', 'precio', 'formato_2', 'precio_2', 'formato_3', 'precio_3', 'sin_gluten', 'aparece', 'barril']


class ComidaList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        comidas = Comida.objects.filter(disponible=True, tipo__aparece=True).order_by('tipo__orden', 'orden', 'nombre')
        serializer = ComidaSerializer(comidas, many=True)
        return Response(serializer.data)


class ComidaSerializer(serializers.ModelSerializer):
    tipo = serializers.SerializerMethodField('get_tipo')

    def get_tipo(self, obj):
        return obj.tipo.nombre + '-' + obj.tipo.nombre_ingles

    class Meta:
        model = Comida
        fields = ('id', 'nombre', 'nombre_ingles', 'descripcion', 'descripcion_ingles', 'tipo', 'precio', 'precio_2', 'altramuces', 'apio', 'cacahuete', 'crustaceo', 'gluten', 'huevo', 'lacteos', 'moluscos', 'mostaza', 'nueces', 'pescado', 'sesamo', 'soja', 'sulfitos', 'disponible')

class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = ['titulo_1', 'titulo_1_ingles', 'titulo_2', 'titulo_2_ingles']


class CervezaList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        cervezas = Cerveza.objects.all()
        serializer = CervezaSerializer(cervezas, many=True)
        titulos = Titulo.objects.first()
        titulosSerializer = TituloSerializer(titulos)
        return Response({"titulos": titulosSerializer.data, "cervezas": serializer.data})


import csv
import os

def cast_bool(entry):
    try:
        if not entry:
            return False
        trues = ['sí', 'si']
        return entry.lower() in trues
    except Exception:
        return False

def cast_price(entry):
    result = entry
    result = result.replace('€', '')
    result = result.replace(',', '.')
    result = result.strip()
    if result:
        return float(result)
    return 0.0

def load_csv():

    with open(f'{os.path.dirname(os.path.abspath(__file__))}/carta-cervezas.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                cerveza = Cerveza.objects.create(
                    nombre=row['Nombre'],
                    estilo = row['Estilo'],
                    pais = row['País'],
                    pais_ingles = row['País Ingles'],
                    alcohol	 = row['Alcohol'],
                    color = row['Color'],
                    amargor	 = row['Amargor'],
                    descripcion = row['Descripcion'],
                    descripcion_ingles = row['Descripcion ingles'],
                    disponible = cast_bool(row['Disponible']),
                    imagen = row['Imagen'],
                    artesanal = cast_bool(row['Artesanal']),
                    tipo = row['Tipo'],
                    recomendada	 = cast_bool(row['Recomendada']),
                    formato	 = row['Formato'],
                    precio = cast_price(row['Precio']),
                    formato_2 = row['formato 2'],
                    precio_2 = cast_price(row['precio 2']),
                    formato_3 = row['formato 3'],
                    precio_3 = cast_price(row['precio 3']),
                    sin_gluten = cast_bool(row['Sin gluten']),
                    aparece	= cast_bool(row['Aparece']),
                    barril = cast_bool(row['Barril'])
                )
                cerveza.save()
            except Exception:
                pass

    with open(f'{os.path.dirname(os.path.abspath(__file__))}/carta-comida.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                comida = Comida.objects.create(
                    nombre=row['Nombre'],
                    nombre_ingles=row['Nombre ingles'],
                    descripcion=row['Descripcion'],
                    descripcion_ingles=row['Descripcion ingles'],
                    tipo=row['Tipo'],
                    precio=cast_price(row['Precio']),
                    precio_2=cast_price(row['precio 2']),
                    altramuces=cast_bool(row['Altramuces']),
                    apio=cast_bool(row['Apio']),
                    cacahuete=cast_bool(row['Cacahuete']),
                    crustaceo=cast_bool(row['Crustaceo']),
                    gluten=cast_bool(row['Gluten']),
                    huevo=cast_bool(row['Huevo']),
                    lacteos=cast_bool(row['Lacteos']),
                    moluscos=cast_bool(row['Moluscos']),
                    mostaza=cast_bool(row['Mostaza']),
                    nueces=cast_bool(row['Nueces']),
                    pescado=cast_bool(row['Pescado']),
                    sesamo=cast_bool(row['Sesamo']),
                    soja=cast_bool(row['Soja']),
                    sulfitos=cast_bool(row['Sulfitos']),
                    disponible=cast_bool(row['Disponible'])
                )
                comida.save()
            except Exception as exc:
                pass