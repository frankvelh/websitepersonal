```markdown
## Creamos Links website


Este proyecto es una aplicación web que muestra enlaces a redes sociales. Utiliza una arquitectura **Frontend + Backend**, ambos ejecutados en contenedores Docker mediante `docker-compose`.

---

## Estructura del Proyecto
```bash
LinksWebsite/
│
├── frontend/
│ ├── sitio
│ ├─── linktree.html
│ ├─── requests.js
│ ├── Dockerfile
│ └── 
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── docker-compose.yml
|── README.md



## En frontend 
- dockerfile para creación de la imagen  frontend 
creamos el sitio:
- lintree con la estructra html
- requests.js

## Creamos el backend
- Dentro  tenemos el appi llamdo app.py el cual tiene un metodo : def getMyInfo() --> el método tiene un json que almacena los vínculos de las redes sociales el cual se verá reflejado en el frontend gracias a un script llamado requestd.js el cual está obteniendo con una operación get la información y mandándole al html para que pueda ser desplegada 
- tendremos al dockerfile para creación de la imagen backend

y en el proyecto creamos el docker-compose para crear el contenedor.

## Ejecutamos: 
1- docker compose build  --> se ejecuta segun la secuencia y se crean las dos imagenes
2- docker compose up --> se crea el contenedor 
3- docker compose up p --> se crea el contenedor permanente