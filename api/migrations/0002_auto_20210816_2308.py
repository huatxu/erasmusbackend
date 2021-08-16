from django.db import migrations
import csv
import os

def cast_bool(entry):
    if not entry:
        return False
    trues = ['sí', 'si']
    return entry.lower() in trues

def cast_price(entry):
    result = entry
    result = result.replace('€', '')
    result = result.replace(',', '.')
    result = result.strip()
    if result:
        return float(result)
    return 0.0

def reverse(test, test2):
    pass

def load_csv(apps, schema_editor):
    Cerveza = apps.get_model('api', 'Cerveza')
    Comida = apps.get_model("api", 'Comida')
    db_alias = schema_editor.connection.alias

    with open(f'{os.path.dirname(os.path.abspath(__file__))}/carta-cervezas.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                cerveza = Cerveza.objects.using(db_alias).create(
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
                print(cast_bool(row['Sin gluten']))
                cerveza.save()
            except Exception:
                pass

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_csv, reverse)
    ]
