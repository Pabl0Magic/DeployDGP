# DGP Digital Twin Team 2
## Inicio
### Prerrequisitos
1. Node.js
	- Descarga e instala Node.js desde la página oficial: [https://nodejs.org/](https://nodejs.org/)
2. npm
	- npm viene incluido con la instalación de Node.js.
3. Python
	- Descarga e instala Python 3.10 desde la página oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Instalación
1. Navega al directorio del proyecto:
  ```bash
  cd teaching-dgp23-digitaltwin-team2
  ```
2. (Opcional) Usa un entorno virtual:
  - Genera un entorno virtual:
    ```bash
    python -m venv .venv
    ```
  - En el IDE, selecciona este entorno virtual
3. Instala las dependencias del servidor:
  - Navega al subdirectorio del servidor:
    ```bash
    cd backend/heroku-django-template-master
    ```
  - Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```
4. Instala las dependencias del cliente:
  - Navega hacia el subdirectorio del cliente:
    ```bash
    cd frontend
    ```
  - Instala las dependencias necesarias:
    ```bash
    npm install
    ```

### Uso
1. Inicia el servidor Django:
  ```bash
  cd backend/heroku-django-template-master
  python manage.py runserver
  ```
2. Inicia el servidor Angular:
  ```bash
  ng serve
  ```
3. Accede a la aplicación a través de un navegador:
  - Abre el navegador y accede a `http://localhost:4200/` (o la dirección que se especifique en el terminal)