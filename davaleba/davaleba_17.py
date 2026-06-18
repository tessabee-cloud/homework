import requests
from pydantic import BaseModel, ValidationError
import json

API_BASE_URL = "https://crudcrud.com/api/YOUR_UNIQUE_ENDPOINT/recipes"

class Recipe(BaseModel):
    name: str
    cuisine: str
    time_minutes: str

def load_recipes_from_file(filename="recipes.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def add_recipe(recipe: dict):
    try:
        rcp = Recipe(**recipe)

        response = requests.post(API_BASE_URL, json=rcp.dict(), timeout=5)
        response.raise_for_status()
        print(f"Added recipe: {rcp.name}")
    except ValidationError as e:
        print(f"Validation error: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.ConnectTimeout:
        print("Connection timed out while adding recipe.")

def get_all_recipes():
    try:
        response = requests.get(API_BASE_URL, timeout=5)
        response.raise_for_status()
        recipes = response.json()
        for r in recipes:
            print(f"Name: {r['name']}, Time: {r['time_minutes']}")
        return recipes
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.ConnectTimeout:
        print("Connection timed out while fetching recipes.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def get_recipe_by_id(recipe_id):
    try:
        response = requests.get(f"{API_BASE_URL}/{recipe_id}", timeout=5)
        response.raise_for_status()
        recipe = response.json()
        print(recipe)
        return recipe
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.ConnectTimeout:
        print("Connection timed out while fetching recipe by ID.")

def update_recipe(recipe_id, updated_data):
    try:
        recipe = Recipe(**updated_data)

        response = requests.put(f"{API_BASE_URL}/{recipe_id}", json=recipe.dict(), timeout=5)
        response.raise_for_status()
        print(f"Updated recipe ID: {recipe_id}")
    except ValidationError as e:
        print(f"Validation error: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.ConnectTimeout:
        print("Connection timed out while updating recipe.")

def delete_recipe(recipe_id):
    try:
        response = requests.delete(f"{API_BASE_URL}/{recipe_id}", timeout=5)
        response.raise_for_status()
        print(f"Deleted recipe ID: {recipe_id}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.ConnectTimeout:
        print("Connection timed out while deleting recipe.")

def main():
    recipes = load_recipes_from_file()
    for rec in recipes:
        add_recipe(rec)

    all_recipes = get_all_recipes()

    if all_recipes:
        first_recipe_id = all_recipes[0].get("_id", None)

        if first_recipe_id:
            get_recipe_by_id(first_recipe_id)

            updated_data = {
                "name": "Updated " + all_recipes[0]["name"],
                "cuisine": all_recipes[0]["cuisine"],
                "time_minutes": all_recipes[0]["time_minutes"]
            }
            update_recipe(first_recipe_id, updated_data)

            get_recipe_by_id(first_recipe_id)

        last_recipe_id = all_recipes[-1].get("_id", None)
        if last_recipe_id:
            delete_recipe(last_recipe_id)

            get_all_recipes()

if __name__ == "__main__":
    main()
