# eventos

Django app 

## Tablas

eventos:
- organizador
- descripcion
- fecha_hora
- direccion
- valor
- cantidad_boletos
- typo_evento
- afiche
- user_id
- fecha_creacion
- stado

Tipo:
- id
- nombre
- descripción
- estado
- fecha_registro

## Ejecutar Celery
```
python -m celery -A taskapp worker
```