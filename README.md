# tpi-gimnasio

## Dependencias

- Docker

## Iniciar submodulos

Este repositorio es el contenedor de otros 2 repositorios que conforman esta app. Para inicarlos hay que ejecutar los siguientes comandos en la terminal:

```bash
git submodule init
git submodule update
```

## Configuración

Copiar el archivo .env.sample en la misma carpeta con el nombre .env y completar los datos con los requeridos pra la app y la bases de datos.

```bash
cp .env.sample .env
nano .env
```

## Iniciar

```bash
docker compose up -d database
docker compose up -d app
```

> [!NOTE]
> Tuvimos problemas a la hora de iniciar sin especificar el orden de los permisos porque no estaba respetando bien el orden del compose.

_Quitando la opción _-d_ se ven los logs del contenedor._

## Detener

```bash
# Si estan corriendo con logs visibles
#     detener con Ctr+C
docker compose down
```

## Debug

Para la app de Django

```bash
docker composer exec -it app bash
```

Para la base de datos

```bash
docker composer exec -it database bash
```

## Manage Django

Para hacer las migraciones hay que hacerlas desde dentro del conteedor, la mayoria de los comando puede seguir el mismo formato

```bash
docker composer exec app python manage.py makemigrations
```

Para aplicarlas es lo mismo

```bash
docker composer exec app python manage.py migrate
```

## Información

Para mas información consulte los ***README*** de cada submodulo.

- [APP](./app/README.md)
- [DB](./database/README.md)