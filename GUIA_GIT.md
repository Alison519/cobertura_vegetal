# Guía de Git por ramas

## 1. Preparar el repositorio (lo hace UNA persona, el coordinador)
    git init
    git add README.md .gitignore
    git commit -m "chore: estructura inicial del proyecto"
    git branch -M main
    git remote add origin <URL_DEL_REPO>
    git push -u origin main
    git checkout -b develop
    git push -u origin develop

El resto del equipo clona el repo y trabaja desde `develop`:
    git clone <URL_DEL_REPO>
    git checkout develop

## 2. Ramas y archivos de cada una
| Rama                          | Archivos                                                        | Historias       |
|-------------------------------|-----------------------------------------------------------------|-----------------|
| feature/tda-pilas-colas       | tda/pila.py, tda/cola.py, modelo/registro.py, modelo/historial.py | HU-04, 05, 06   |
| feature/modelo-datos          | modelo/actividad.py, modelo/cobertura.py, modelo/efecto.py      | HU-09, 10       |
| feature/recursividad          | modelo/zona.py                                                  | HU-07, 08       |
| feature/autoridad-reportes    | modelo/reporte.py, modelo/autoridad.py                          | HU-01, 02, 03   |
| feature/menu-principal        | main.py                                                         | HU-10           |
| feature/pruebas               | tests/                                                          | HU-11           |
| feature/documentacion         | README.md, informe, registro de errores                         | HU-12           |

## 3. Flujo de trabajo de cada persona
    git checkout develop
    git pull origin develop
    git checkout -b feature/tda-pilas-colas     # cambia el nombre según tu rama

    # trabajas, y haces commits pequeños:
    git add tda/pila.py
    git commit -m "feat: agrega clase Pila con apilar y desapilar"

    git push -u origin feature/tda-pilas-colas

Luego abres un Pull Request hacia `develop` y un compañero lo revisa antes de unirlo.
Nunca se hace push directo a `main` ni a `develop`.

## 4. Orden recomendado para unir las ramas a develop
1. feature/tda-pilas-colas  (Pila, Cola e historial; no dependen de nada)
2. feature/modelo-datos     (actividades, cobertura y efectos)
3. feature/recursividad     (Zona usa el historial)
4. feature/autoridad-reportes (usa la Cola)
5. feature/menu-principal   (usa todo lo anterior)
6. feature/pruebas          (prueba todo)

Después de cada unión, los demás actualizan su rama:
    git checkout feature/mi-rama
    git merge develop

## 5. Entrega final
Cuando `develop` funcione y las pruebas pasen, el coordinador lo une a `main`:
    git checkout main
    git merge develop
    git push origin main
    git tag v1.0
    git push origin v1.0

## 6. Convención de mensajes de commit
- feat: función nueva           (feat: agrega método desencolar a Cola)
- fix: corrección de un error   (fix: valida hectáreas negativas)
- test: pruebas                 (test: agrega pruebas de Zona)
- docs: documentación           (docs: actualiza README)
- chore: configuración          (chore: agrega .gitignore)

## 7. Si hay conflictos al hacer merge
Git marca los archivos con <<<<<<<, ======= y >>>>>>>. Se abre el archivo, se deja
la versión correcta, se borran las marcas y luego:
    git add <archivo>
    git commit
