from flask import Blueprint, request, jsonify

recipes_bp = Blueprint('recipes', __name__)

# Simple demo recipes endpoint
@recipes_bp.route('/suggest', methods=['POST'])
def suggest_recipes():
    data = request.json
    ingredients = data.get('ingredients')  # list or string

    # Dummy recipe suggestion logic
    recipes = [
        {'name': 'Tomato Pasta', 'ingredients': ['tomato', 'pasta', 'olive oil']},
        {'name': 'Chicken Salad', 'ingredients': ['chicken', 'lettuce', 'olive oil']},
    ]

    # Filter recipes that match at least one ingredient
    matched = []
    if isinstance(ingredients, str):
        ingredients = [i.strip().lower() for i in ingredients.split(',')]
    elif not isinstance(ingredients, list):
        ingredients = []

    for recipe in recipes:
        if any(ing in ingredients for ing in recipe['ingredients']):
            matched.append(recipe)

    return jsonify({'recipes': matched})
