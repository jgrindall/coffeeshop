from flask import request, jsonify, abort
from .database.models import db_drop_and_create_all, Drink
from .auth.auth import requires_auth, auth_logout
import json

def api(app):

    @app.route('/reset', methods=['GET'])
    def reset():
        db_drop_and_create_all()
        return jsonify({
            'success': True
        })

    @app.route('/logout')
    def logout():
        auth_logout()

    @app.route('/drinks')
    def get_drinks():
        drinks = Drink.query.all()
        return jsonify({
            'success': True,
            'drinks': [drink.short() for drink in drinks]
        })

    
    @app.route('/drinksdetail')
    @requires_auth('get:drinksdetail')
    def get_drinks_detail(payload):
        drinks = Drink.query.all()
        return jsonify({
            'success': True,
            'drinks': [drink.long() for drink in drinks]
        })

    
    @app.route('/drinks', methods=['POST'])
    @requires_auth('create:drinks')
    def create_drink(payload):
        data = request.get_json()
        title = data.get('title', None)
        recipe = data.get('recipe', None)

        if title is None or recipe is None or not isinstance(recipe, list) or len(recipe) == 0 or title.strip() == '':
            abort(422)

        drink = Drink(title=title, recipe=json.dumps(recipe))
        drink.insert()

        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        })

    @app.route('/drinks/<int:id>', methods=['PATCH'])
    @requires_auth('update:drinks')
    def update_drink(payload, id):
        drink = Drink.query.get(id)

        if drink is None:
            abort(404)

        data = request.get_json()
        title = data.get('title', None)
        recipe = data.get('recipe', None)

        if title is not None and len(title.strip()) >= 1:
            drink.title = title

        if recipe is not None and isinstance(recipe, list) and len(recipe) >= 1:
            drink.recipe = json.dumps(recipe)

        drink.update()

        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        })

    @app.route('/drinks/<int:id>', methods=['DELETE'])
    @requires_auth('delete:drinks')
    def delete_drink(payload, id):
        drink = Drink.query.get(id)

        if drink is None:
            abort(404)

        drink.delete()

        return jsonify({
            'success': True,
            'delete': id
        })
