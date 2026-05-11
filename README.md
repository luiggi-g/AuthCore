# AuthCore

Backend de autenticación desarrollado con Python y FastAPI, enfocado en comprender e implementar desde cero los fundamentos de seguridad y autenticación moderna utilizando JWT, bcrypt y PostgreSQL.

## Objetivo del proyecto

El propósito de este proyecto fue construir un sistema de autenticación profesional sin utilizar ORMs ni librerías que abstraigan completamente el funcionamiento interno de JWT.

La idea principal fue entender a profundidad:

* Arquitectura backend por capas
* Hashing de contraseñas
* Generación y validación manual de JWT
* Flujo Access Token + Refresh Token
* Protección de endpoints
* Validación de credenciales
* Manejo de sesiones modernas

---

# Tecnologías utilizadas

* Python
* FastAPI
* PostgreSQL
* psycopg2
* Pydantic
* bcrypt
* JWT (implementación manual)
* Uvicorn

---

# Características implementadas

## Autenticación

* Registro de usuarios
* Login de usuarios
* Verificación segura de contraseñas
* Hashing con bcrypt
* Access Tokens
* Refresh Tokens
* Renovación de sesión
* Endpoints protegidos
* Validación de expiración de tokens
* Validación de firma HMAC SHA256
* Validación de tipo de token (`access` / `refresh`)

---

# Arquitectura del proyecto

```bash
app/
├── main.py
├── core/
│   ├── config.py
│   ├── security.py
│   └── dependencies.py
├── db/
│   └── connection.py
├── models/
│   └── user_model.py
├── schemas/
│   └── user_schema.py
├── services/
│   └── user_service.py
├── routers/
│   └── auth_router.py
└── utils/
```

---

# Arquitectura utilizada

El proyecto utiliza una arquitectura por capas para separar responsabilidades:

| Capa     | Responsabilidad           |
| -------- | ------------------------- |
| routers  | Endpoints HTTP            |
| services | Lógica de negocio         |
| models   | Acceso a base de datos    |
| schemas  | Validación de datos       |
| core     | Seguridad y configuración |

---

# Flujo de autenticación

## Login

```text
Usuario envía credenciales
↓
Verificación de contraseña con bcrypt
↓
Generación de Access Token
↓
Generación de Refresh Token
↓
Respuesta al cliente
```

## Protección de endpoints

```text
Cliente envía Bearer Token
↓
Validación JWT
↓
Validación de expiración
↓
Acceso permitido
```

## Renovación de sesión

```text
Cliente envía Refresh Token
↓
Validación del token
↓
Generación de nuevo Access Token
```

---

# Instalación

## Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/AuthCore.git
```

## Entrar al proyecto

```bash
cd AuthCore
```

## Crear entorno virtual

```bash
python -m venv venv
```

## Activar entorno virtual

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Variables de entorno

Crear archivo:

```bash
app/.env
```

Ejemplo:

```env
SECRET_KEY=tu_secret_key
ACCESS_TOKEN_EXPIRE_SECONDS=3600
```

---

# Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

---

# Endpoints principales

| Método | Endpoint       | Descripción          |
| ------ | -------------- | -------------------- |
| POST   | /auth/register | Registro de usuarios |
| POST   | /auth/login    | Inicio de sesión     |
| POST   | /auth/refresh  | Renovar access token |
| GET    | /auth/profile  | Endpoint protegido   |

---

# Aprendizajes principales

Durante el desarrollo de este proyecto se trabajó en:

* Implementación manual de JWT
* Seguridad backend
* Manejo de autenticación moderna
* Arquitectura escalable
* SQL puro con PostgreSQL
* Diseño limpio de APIs REST
* Separación de responsabilidades

---

# Mejoras futuras

* Revocación de refresh tokens
* Logout real
* Roles y permisos (RBAC)
* Rate limiting
* Dockerización
* Tests automatizados
* Auditoría de sesiones
* Integración CI/CD

---

# Autor

Desarrollado como proyecto de aprendizaje avanzado en backend, autenticación y seguridad utilizando FastAPI y PostgreSQL.
