# Notas de seguridad del laboratorio

## Propósito

Este laboratorio existe para enseñar cómo funciona la inyección SQL y por qué las
consultas parametrizadas son la defensa correcta. **No es una herramienta de ataque.**

## Reglas de uso

1. Ejecutar únicamente en local (`127.0.0.1`) o en una red aislada.
2. No apuntar a sistemas, sitios web o servicios de terceros.
3. No desplegar en Internet ni exponer el puerto 8080 públicamente.
4. Usar exclusivamente los datos ficticios incluidos en `database/seed.sql`.

## Vulnerabilidades inclucidas (intencionadas)

| Escenario | Ruta | Técnica |
| --- | --- | --- |
| Login bypass | `/login` | Concatenación de cadenas en la consulta |
| Error-based | `/search?q='` | Error SQL expuesto en la respuesta |
| Boolean-based | `/product?id=1' AND '1'='1` | Inferencia por diferencia de respuesta |
| Time-based | `/product?id=1' AND SLEEP(5) -- -` | Retardo medido en la respuesta |

## Defensas demostradas

- `/secure-login` usa `cursor.execute(sql, params)` con marcadores `%s`.
- Validación de que el payload de bypass no autentica en la versión segura.

## Manejo de datos

Las contraseñas se almacenan en texto plano **únicamente** para que el laboratorio
sea reproducible. En cualquier sistema real deben usarse algoritmos de hash
(`bcrypt`, `argon2`, ...) y nunca texto plano.
