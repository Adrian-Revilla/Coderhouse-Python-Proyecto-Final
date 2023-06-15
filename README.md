Coderhouse comisión #40445,
Adrian Felipe Revilla Martinez.
---------------

#### Configuración del entorno de desarrollo
Estos son los pasos a seguir muy resumidamente:

- **Situarse en la raíz del proyecto**
	- Crear e inicializar un entorno virtual
	- Instalar paquetes de pip descritos en requirements.txt
	- Preparar la base de datos 
	- ejecutar manage.py situado en src/

---

#### Comandos de terminal a ejecutar en orden 
#### (Probado en una maquina Ubuntu 22.04.1 LTS x86_64):
---------------
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd src
python manage.py createsuperuser # admin y passwd 1234
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
