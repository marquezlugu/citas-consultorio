# Citas del Consultorio

Sistema para que los pacientes agenden sus citas médicas desde el teléfono, sin tener que llamar al consultorio.

> **Proyecto ficticio.** Es el ejemplo de la exposición «GitHub y GitLab como herramientas de gestión de proyectos» (Ingeniería de Software, Maestría en Informática Gerencial, UDO Monagas). No es un sistema real.

## Equipo (ficticio)

| Persona | Rol |
|---|---|
| Laura | Líder del proyecto |
| Carlos | Programador |
| Ana | Programadora |
| Pedro | Pruebas |

## Cómo trabajamos

- Cada cosa por hacer es un **issue**, con etiquetas y el hito **Versión 1.0**.
- Trabajamos en **ciclos de 2 semanas** (Ciclo 1 y Ciclo 2) en el tablero del proyecto.
- Nada entra a `main` sin un **pull request** revisado por otra persona.
- Las pruebas corren solas en cada pull request.

## Correr las pruebas

```
python -m unittest discover -s tests
```
