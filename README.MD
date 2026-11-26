# Aruma

Aruma ejecuta una API de agendas con FastAPI detrás de Kong y expone el acceso mediante Nginx. Incluye Keycloak, PostgreSQL y volúmenes persistentes.

## Requisitos

- Docker
- Docker Compose
- Puertos 80 y 443 disponibles
- Certificados en `nginx/certs/fullchain.pem` y `nginx/certs/privkey.pem`

## Configuración

Crear el archivo `.env` en la raíz del proyecto:

```env
KEYCLOAK_ADMIN=<usuario_administrador>
KEYCLOAK_ADMIN_PASSWORD=<password_administrador>
KEYCLOAK_POSTGRES_DB=<nombre_base_de_datos>
KEYCLOAK_POSTGRES_USER=<usuario_postgres>
KEYCLOAK_POSTGRES_PASSWORD=<password_postgres>
```

Crear el archivo `ms-agendas/.env`:

```env
DB_URL=postgresql+psycopg://<usuario_postgres>:<password_postgres>@agendas-db:5432/<nombre_base_de_datos>
POSTGRES_DB=<nombre_base_de_datos>
POSTGRES_USER=<usuario_postgres>
POSTGRES_PASSWORD=<password_postgres>
```

`DB_URL`, `POSTGRES_DB`, `POSTGRES_USER` y `POSTGRES_PASSWORD` deben usar los mismos valores.

## Ejecución

Entorno de producción:

```powershell
docker compose up --build -d
```

Entorno de desarrollo con recarga automática:

```powershell
docker compose -f docker-compose.dev.yml up --build -d
```

Para comprobar los contenedores:

```powershell
docker compose ps
```

Para seguir los logs:

```powershell
docker compose logs -f
```

## Acceso

Servicio de agendas:

```text
https://localhost/api/agendas
```

Keycloak:

```text
https://localhost/auth
```

Nginx puede mostrar una advertencia si los certificados son locales o autofirmados.

## Reiniciar

Producción:

```powershell
docker compose down
docker compose up --build -d
```

Desarrollo:

```powershell
docker compose -f docker-compose.dev.yml down
docker compose -f docker-compose.dev.yml up --build -d
```

## Detener

```powershell
docker compose down
```

Para detener el entorno de desarrollo:

```powershell
docker compose -f docker-compose.dev.yml down
```