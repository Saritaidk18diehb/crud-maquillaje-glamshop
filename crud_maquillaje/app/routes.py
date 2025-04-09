from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app.db_config import get_connection
from app.mongo_config import get_mongo_connection

app_routes = Blueprint('app_routes', __name__)

# ----------------------------
# Página de inicio con presentación
# ----------------------------
@app_routes.route('/')
def mostrar_inicio():
    return render_template('inicio.html')

# ----------------------------
# Página principal: listar productos (MySQL)
# ----------------------------
@app_routes.route('/productos')
@app_routes.route('/para-ti')
def listar_productos():
    conexion = get_connection()
    with conexion.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
    conexion.close()
    return render_template('listar.html', productos=productos)

# ----------------------------
# Crear producto (MySQL + MongoDB)
# ----------------------------
@app_routes.route('/crear', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        categoria = request.form['categoria']

        # Guardar en MySQL
        conexion = get_connection()
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO productos (nombre, descripcion, precio, stock, categoria)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, descripcion, precio, stock, categoria))
            conexion.commit()
        conexion.close()

        # Guardar en MongoDB
        mongo_db = get_mongo_connection()
        mongo_db.productos.insert_one({
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "categoria": categoria
        })

        flash('Producto creado exitosamente 💖')
        return redirect(url_for('app_routes.listar_productos'))

    return render_template('crear.html')

# ----------------------------
# Editar producto (MySQL + MongoDB)
# ----------------------------
@app_routes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    conexion = get_connection()
    mongo_db = get_mongo_connection()

    with conexion.cursor(dictionary=True) as cursor:
        if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            precio = float(request.form['precio'])
            stock = int(request.form['stock'])
            categoria = request.form['categoria']

            # Actualizar en MySQL
            cursor.execute("""
                UPDATE productos
                SET nombre = %s, descripcion = %s, precio = %s, stock = %s, categoria = %s
                WHERE id = %s
            """, (nombre, descripcion, precio, stock, categoria, id))
            conexion.commit()

            # Buscar el nombre anterior del producto
            cursor.execute("SELECT nombre FROM productos WHERE id = %s", (id,))
            producto_mysql = cursor.fetchone()

            # Actualizar en MongoDB usando el nombre
            mongo_db.productos.update_one(
                {"nombre": producto_mysql['nombre']},
                {"$set": {
                    "nombre": nombre,
                    "descripcion": descripcion,
                    "precio": precio,
                    "stock": stock,
                    "categoria": categoria
                }}
            )

            flash('Producto actualizado exitosamente ✨')
            return redirect(url_for('app_routes.listar_productos'))
        else:
            cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
            producto = cursor.fetchone()
            if producto is None:
                abort(400)

    conexion.close()
    return render_template('editar.html', producto=producto)

# ----------------------------
# Eliminar producto (MySQL + MongoDB)
# ----------------------------
@app_routes.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_producto(id):
    conexion = get_connection()
    with conexion.cursor(dictionary=True) as cursor:
        if request.method == 'POST':
            cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
            producto = cursor.fetchone()

            # Eliminar en MySQL
            cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
            conexion.commit()
            conexion.close()

            # Eliminar en MongoDB
            mongo_db = get_mongo_connection()
            mongo_db.productos.delete_one({"nombre": producto['nombre']})

            flash('Producto eliminado con éxito 💔')
            return redirect(url_for('app_routes.listar_productos'))

        cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        producto = cursor.fetchone()
    conexion.close()
    return render_template('eliminar.html', producto=producto)

# ----------------------------
# Página de categorías
# ----------------------------
@app_routes.route('/categorias')
def mostrar_categorias():
    # Aquí puedes agregar la lógica real para cargar categorías
    return render_template('categorias.html')

# ----------------------------
# Página de tiendas con links externos
# ----------------------------
@app_routes.route('/tiendas')
def mostrar_tiendas():
    marcas = [
        {"nombre": "Tintilia", "url": "https://tintilia.com"},
        {"nombre": "Atenea Beauty", "url": "https://ateneabeauty.co"},
        {"nombre": "Carmín Cosméticos", "url": "https://carmincosmeticos.com"},
        {"nombre": "Evolue Colombia", "url": "https://www.evolue.com.co"},
    ]
    return render_template('tiendas.html', marcas=marcas)
