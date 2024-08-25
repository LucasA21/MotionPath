# MotionPath app

## Dependencias

- Docker

> [!WARNING]
> Si no lo usamos como un submodulo hay que usar el servicio dev del compose.

## Configuración

Copiar el archivo .env.sample en la misma carpeta con el nombre .env y completar los datos con los requeridos pra la app y la bases de datos.

```bash
cp .env.sample .env
nano .env
```

## Iniciar

```bash
docker compose up -d dev
```

_Quitando la opción _-d_ se ven los logs del contenedor._

## Detener

```bash
# Si estan corriendo con logs visibles
#     detener con Ctr+C
docker compose down
```

## Debug

```bash
docker composer exec -it dev bash
```

## Manage Django

Para hacer las migraciones hay que hacerlas desde dentro del conteedor, la mayoria de los comando puede seguir el mismo formato

```bash
docker composer exec dev python manage.py makemigrations
```

Para aplicarlas es lo mismo

```bash
docker composer exec dev python manage.py migrate
```