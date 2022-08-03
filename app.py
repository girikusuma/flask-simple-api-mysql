from flask import Flask, jsonify, make_response, request
from database import connection

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    data = [{
        'categories': 'http://127.0.0.1:5000/categories',
        'products': 'http://127.0.0.1:5000/products',
    }]
    return make_response(jsonify({'data': data}), 200)

@app.route('/categories', methods=['GET', 'POST'])
def categories_list():
    try:
        if request.method == 'GET':
            conn = connection()
            cursor = conn.cursor()

            query = "SELECT * FROM categories;"
            cursor.execute(query)
            row = [x[0] for x in cursor.description]
            result = cursor.fetchall()
            
            data = []
            for item in result:
                data.append(dict(zip(row, item)))
            return make_response(jsonify({'data': data}), 200)
        elif request.method == 'POST':
            req = request.json
            name = req['name']
            description = req['description']

            conn = connection()
            cursor = conn.cursor()

            query = "INSERT INTO categories (name, description) VALUES (%s, %s);"
            values =  (name, description)
            cursor.execute(query, values)
            conn.commit()

            data = [{
                'message': 'Category created'
            }]
            return make_response(jsonify({'data': data}), 201)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)

@app.route('/categories/<id>', methods=['GET', 'PUT', 'DELETE'])
def categories_detail(id):
    try:
        if request.method == 'GET':
            conn = connection()
            cursor = conn.cursor()

            query = "SELECT * FROM categories WHERE id = %s;"
            values = (id,)
            cursor.execute(query, values)
            row = [x[0] for x in cursor.description]
            result = cursor.fetchall()
            
            data = []
            for item in result:
                data.append(dict(zip(row, item)))
            return make_response(jsonify({'data': data}), 200)
        elif request.method == 'PUT':
            req = request.json
            name = req['name']
            description = req['description']

            conn = connection()
            cursor = conn.cursor()

            query = "UPDATE categories SET name = %s, description = %s WHERE id = %s;"
            values =  (name, description, id)
            cursor.execute(query, values)
            conn.commit()

            data = [{
                'message': 'Category updated'
            }]
            return make_response(jsonify({'data': data}), 200)
        else:
            conn = connection()
            cursor = conn.cursor()

            query = "DELETE FROM categories WHERE id = %s;"
            values =  (id,)
            cursor.execute(query, values)
            conn.commit()

            data = [{
                'message': 'Category deleted'
            }]
            return make_response(jsonify({'data': data}), 204)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)

@app.route('/products', methods=['GET', 'POST'])
def product_list():
    try:
        if request.method == 'GET':
            conn = connection()
            cursor = conn.cursor()

            query = "SELECT * FROM products;"
            cursor.execute(query)
            row = [x[0] for x in cursor.description]
            result = cursor.fetchall()
            
            data = []
            for item in result:
                data.append(dict(zip(row, item)))
            return make_response(jsonify({'data': data}), 200)
        elif request.method == 'POST':
            req = request.json
            category_id = req['category_id']
            code = req['code']
            name = req['name']
            description = req['description']

            conn = connection()
            cursor = conn.cursor()

            query = "INSERT INTO products (category_id, code, name, description) VALUES (%s, %s, %s, %s);"
            values =  (category_id, code, name, description)
            cursor.execute(query, values)
            conn.commit()

            data = [{
                'message': 'Product created'
            }]
            return make_response(jsonify({'data': data}), 201)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)

@app.route('/products/<id>', methods=['GET', 'PUT', 'DELETE'])
def products_detail(id):
    try:
        if request.method == 'GET':
            conn = connection()
            cursor = conn.cursor()

            query = "SELECT * FROM products WHERE id = %s;"
            values = (id,)
            cursor.execute(query, values)
            row = [x[0] for x in cursor.description]
            result = cursor.fetchall()
            
            data = []
            for item in result:
                data.append(dict(zip(row, item)))
            return make_response(jsonify({'data': data}), 200)
        elif request.method == 'PUT':
            req = request.json
            category_id = req['category_id']
            code = req['code']
            name = req['name']
            description = req['description']

            conn = connection()
            cursor = conn.cursor()

            query = "UPDATE categories SET category_id = %s, code = %s, name = %s, description = %s WHERE id = %s;"
            values =  (category_id, code, name, description, id)
            cursor.execute(query, values)
            conn.commit()

            data = [{
                'message': 'Product updated'
            }]
            return make_response(jsonify({'data': data}), 200)
        else:
            conn = connection()
            cursor = conn.cursor()

            query = "DELETE FROM products WHERE id = %s;"
            values =  (id,)
            cursor.execute(query, values)
            conn.commit()
            
            data = [{
                'message': 'Product deleted'
            }]
            return make_response(jsonify({'data': data}), 204)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)

app.run()