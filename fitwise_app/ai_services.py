
from google import genai

api_key = "Ab8RN6KsMRLS47XZBOulHqqjnwOSvSf0vvwrmcLkrBSKs5znRA"

client = genai.Client(api_key=api_key)

def get_diet_plan(response_data):

    monthly_total_calorie = response_data.get("monthly_total_calorie")
    category_total_calorie = response_data.get("category_total_calorie")

    category_total_calorie_text = ""

    for di in category_total_calorie:

        category_total_calorie_text += f". {di.get("meal_type")} : {di.get("total")}\n"

    print(category_total_calorie_text)