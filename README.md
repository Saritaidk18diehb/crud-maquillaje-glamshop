# 💖 GlamShop CRUD: Gestor de Productos de Maquillaje

¡Bienvenid@ a **GlamShop**!  
Un proyecto web visualmente atractivo y funcional, diseñado para ayudar a principiantes del maquillaje a conocer y crear productos nuevos. Este CRUD conecta simultáneamente con **MongoDB Atlas** y **MySQL (HeidiSQL)**, todo con una interfaz dulce, pastel y fácil de usar.
-
## 🌈 Vista Previa
> Inspirado en el diseño y la estética de [maquillajetrendyshop.com](https://www.maquillajetrendyshop.com/)

![Vista del CRUD](https://i.imgur.com/7jGNsPT.png)  
*(Agrega aquí tus propias capturas de pantalla reales desde Visual Studio Code o navegador)*
---

## ⚙️ Tecnologías Utilizadas

| Categoría     | Herramienta                      |
|--------------|----------------------------------|
| Backend      | Python + Flask                   |
| Frontend     | HTML, CSS (pastel)               |
| DB NoSQL     | MongoDB Atlas                    |
| DB SQL       | MySQL (gestionado con HeidiSQL)  |
| IDE          | Visual Studio Code               |
| Control de versiones | Git + GitHub             |
---

## 🧠 Funcionalidades

✔️ Crear productos nuevos  
✔️ Listar todos los productos  
✔️ Editar productos existentes  
✔️ Eliminar productos  
✔️ Categorías visibles  
✔️ Enlace a tiendas externas  
✔️ Diseño pastel y navegación fluida  
✔️ Sincronización con **MongoDB Atlas** y **MySQL (HeidiSQL)** en tiempo real

---

## 🗂️ ESTRUCTURA FINAL DEL PROYECTO GLAMSHOP CRUD
![image](https://github.com/user-attachments/assets/8dfc284c-9f1d-45da-8e22-da06fd3e7c7e)


🚀 ¿Cómo ejecutar GlamShop CRUD?
Sigue estos pasos para levantar el proyecto de manera local desde Visual Studio Code. Puedes trabajar con MongoDB Atlas o con MySQL (HeidiSQL), dependiendo de la rama en la que estés (mongo-atlas o heidi).

🔧 1. Clona el repositorio: 
git clone https://github.com/tu-usuario/GlamShopCRUD.git
cd GlamShopCRUD

🐍 2. Crea y activa un entorno virtual
Importante: Haz todo desde Visual Studio Code. Abre el proyecto y ejecuta estos comandos en el terminal integrado.

Windows:
python -m venv .venv
.venv\Scripts\activate

SI ESTAS EN macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

📦 3. Instala las dependencias
pip install -r requirements.txt

⚙️ 4. Configura tu base de datos

🔀 Ramas del Repositorio
El proyecto se divide en dos ramas con funcionalidades completas e independientes:
Rama	                   Contenido
mongo-atlas	               CRUD completo conectado a MongoDB Atlas
heidi	                   CRUD completo conectado a MySQL con HeidiSQL


📌 Si estás en la rama heidi:
Asegúrate de tener un servidor MySQL activo (con HeidiSQL).
Edita tu archivo db_config.py con las credenciales correctas.
Usa el archivo Exportaciones/export_mysql.sql para crear y poblar la tabla productos.

📌 Si estás en la rama mongo-atlas:
Asegúrate de tener acceso a tu clúster de MongoDB Atlas.
Edita mongo_config.py con tu URI personal.
Usa el archivo Exportaciones/export_mongo.json para importar los datos en tu colección productos.

🧪 5. Ejecuta la aplicación
python run.py
La aplicación estará disponible en:
📍 http://127.0.0.1:5000/


🧭 Navegación de la App
Inicio → Presentación del sitio
Categorías → Lista de categorías
Tiendas → Enlaces externos de tiendas colombianas
Para ti → CRUD de productos con edición en tiempo real

🧩 Diagrama de Clases
+---------------------+
|      Producto       |
+---------------------+
| - nombre            |
| - descripcion       |
| - precio            |
| - stock             |
| - categoria         |
+---------------------+

![image](https://github.com/user-attachments/assets/69dbe082-60bb-4863-a8ea-4d153a9119e3)


     Sincroniza con ambas bases:

     ↓                 ↓
+----------------+  +-----------------+
|  MySQL (SQL)   |  | MongoDB (NoSQL) |
+----------------+  +-----------------+


🧠 Comentarios del Código
Cada archivo contiene comentarios detallados explicando la lógica, propósitos y detalles técnicos del desarrollo. Se han agregado más de 20 comentarios extensos y excepcionales para facilitar la lectura del código por parte de cualquier desarrollador o revisor técnico.


🔗 Rutas Web Principales
URL	                            Vista
/	                           Página de inicio
/productos	                   Listado de productos (CRUD)
/crear                      	Crear producto
/editar/<id>	                Editar producto
/eliminar/<id>               	Eliminar producto
/categorias	                    Mostrar categorías
/tiendas	                    Mostrar tiendas externas

✨ Inspiración Visual
El diseño pastel y la estructura amigable están inspirados en sitios de maquillaje modernos y delicados, especialmente maquillajetrendyshop.com, buscando siempre mantener una estética coherente con el mundo del maquillaje.

🧑‍💻 Autor
Desarrollado con 💅 por [Sofia Romero]
📧 Contacto: sr6584459@gmail.com
🌐 GitHub: Saritaidk18diehb

