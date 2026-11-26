# Aruma

Aruma ejecuta un servicio de agendas con FastAPI detrás de Kong y expone HTTPS mediante Nginx. También incluye Keycloak y PostgreSQL para autenticación.

## Requisitos

- Docker
- Docker Compose
- Puertos 80 y 443 disponibles

## Configuración

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
KEYCLOAK_ADMIN=<usuario_administrador>
KEYCLOAK_ADMIN_PASSWORD=<password_administrador>
KEYCLOAK_POSTGRES_DB=<nombre_base_de_datos>
KEYCLOAK_POSTGRES_USER=<usuario_postgres>
KEYCLOAK_POSTGRES_PASSWORD=<password_postgres>
```

No usar comillas ni espacios innecesarios en los valores.

## Ejecución

Desde la raíz del proyecto, ejecutar:

```powershell
docker compose up --build -d
```

Para ver el estado de los contenedores:

```powershell
docker compose ps
```

Para ver los logs:

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

Nginx puede mostrar una advertencia de certificado al abrir el sitio porque utiliza certificados locales.

## Actualizar y reiniciar

Después de modificar el código o la configuración:

```powershell
docker compose down
docker compose up --build -d
```

## Detener

```powershell
docker compose down
```