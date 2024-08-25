# Postgres

## Instalamos Docker

### Para Debian/Ubuntu

#### Referencia

[Instalación de docker para ubuntu](https://docs.docker.com/engine/install/ubuntu).

```bash
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

## Configuración

Hay 2 instancias, una para iniciar en bloque con los demas servicios (*database*) y otro que inicia individualmente este servicio (*dev*).

1. Copiamos el archivo de ejemplo "**.env.sample**", le cambiamos el nombre a "**.env**" y le agregamos los valores a las variables de entorno que correspondan para la instancia requerida y borramos las innecesarias.

## Iniciar contenedor database

Este servicio no se inica directamente desde este proyecto.

## Iniciar contenedor dev

La opción "**-d**" se puede sacar si se quiere ver los logs al crear el contenedor.

```bash
docker compose up -d dev
```

## Detener contenedor

Si esta corriendo sin la opción "**-d**" simplemente apretar Ctrl+C.

```bash
docker compose down
```

## Base de Datos

Toda la base de datos se guardara en "**/docker/data**"

Para conectarse a una terminal del contenedor (sólo para debug).
Usar los datos configurados previamente en "**.env**".

**POSTGRES_USER**: está en el archivo "**.env**"

**POSTGRES_DB**: está en el archivo "**.env**"

### Debug para database

```bash
docker compose exec -it database bash

# dentro del contenedor (root)
psql -U ${POSTGRES_USER} ${POSTGRES_DB}
```

### Debug para dev

```bash
docker compose exec -it dev bash

# dentro del contenedor (root)
psql -U ${POSTGRES_USER} ${POSTGRES_DB}
```

## Backups

Se creó un volumen para guardar los **backups** en "**/docker/backups**".

### Realizar backup

Para hacer el backup tenemos que entrar a una shell del contenedor y generar el archivo de backup en la carpeta donde esta montado el volumen.
Usar los datos configurados previamente en "**.env**"

**POSTGRES_USER**: está en el archivo "**.env**"

**POSTGRES_DB**: está en el archivo "**.env**"

#### Realizar backups para database

```bash
docker compose exec -it database bash

# dentro del contenedor
pg_dump -U ${POSTGRES_USER} ${POSTGRES_DB} > backups/${POSTGRES_DB}$(date "+%Y%m%d-%H_%M").sql
exit
```

#### Realizar backups para dev

```bash
docker compose exec -it dev bash

# dentro del contenedor
pg_dump -U ${POSTGRES_USER} ${POSTGRES_DB} > backups/${POSTGRES_DB}$(date "+%Y%m%d-%H_%M").sql
exit
```

### Restaurar backup

Para restaurar el backup tenemos que entrar a una shell del contenedor y restaurar el backup que se encuentra en el volumen montado.

**Hay que asegurarse de tener el backup en la carpeta **/backups**.**

**POSTGRES_USER**: está en el archivo "**.env**"

**POSTGRES_DB**: está en el archivo "**.env**"

### Restaurar backup para database

```bash
# Descomprimo el backup
cd backups
sudo gunzip NOMBRE_BACKUP.sql.gz
cd ..

# Elimino la base datos que existe actualmente
docker compose -f compose.dev.yml down
sudo rm -rf docker/data
docker compose -f compose.dev.yml up -d development

# Levanto el backup
docker compose exec -it database bash

# dentro del contenedor
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f backups/NOMBRE_BACKUP.sql
exit
```

### Restaurar backup para dev

```bash
# Descomprimo el backup
cd backups
sudo gunzip NOMBRE_BACKUP.sql.gz
cd ..

# Elimino la base datos que existe actualmente
docker compose -f compose.dev.yml down
sudo rm -rf docker data
docker compose -f compose.dev.yml up -d development

# Levanto el backup
docker compose exec -it dev bash

# dentro del contenedor
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f backups/NOMBRE_BACKUP.sql
exit
```

## Programar backups automáticos (CRON)

### Prerrequisitos

En el servidor de destino tiene que estar configurado ssh para aceptar autenticación con Public Keys.

```bash
$ # En el servidor de destino
$ sudo nano /etc/ssh/sshd_config
$ # Descomentar la linea que tiene: PubkeyAuthentication yes
$ sudo systemctl restart sshd.service
$ #------------------------------------------------------------------------------
$ # En el servidor de origen del backup (USUARIO ROOT)
root$ # Generar las claves del usuario que va a ejecutar el script en este equipo
root$ ssh-keygen
root$ ssh-copy-id USUARIO@SERVIDOR_DESTINO
```

### Programar tarea

```bash
$ # En el servidor de origen del backup
$ cp backup_cron.sh.example backup_cron.sh
$ # Configurar el destino. Editar la linea #DEST=usuaro@host:/path
$ nano backup_cron.sh
$ # Programar la tarea con cron (USUARIO ROOT)
root$ crontab -e
root$ # En cron:
   # Para probar un backup cada 5 minutos
   */5 * * * * /ruta_al_script/backup_cron.sh

   # Para dejar el backup 1 vez por dia
   0 0 * * * /ruta_al_script/backup_cron.sh
```
