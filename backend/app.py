
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="")

# 静态文件托管
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

# 示例 API 路由
@app.route("/test", methods=["GET"])
def test():
    return []

@app.route("/generate_meal_plan", methods=["POST"])
def generate_meal_plan():
    data = request.json
    dishes = data.get("dishes", [])
    meal_plan = {
        "Monday": {"Breakfast": "Pancakes", "Lunch": "Salad", "Dinner": "Pizza"},
        "Tuesday": {"Breakfast": "Oatmeal", "Lunch": "Sandwich", "Dinner": "Soup"}
    }
    return jsonify({"meal_plan": meal_plan})

if __name__ == "__main__":
    app.run(debug=True)
