from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 设置 OpenAI API 密钥
openai.api_key = "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"

@app.route('/api/meals', methods=['POST'])
def generate_meal_plan():
    try:
        data = request.json
        user_meals = data.get('meals', [])

        if not user_meals:
            return jsonify({'error': 'No meals provided'}), 400

        # open ai
        prompt = f"用户提供的餐点：{', '.join(user_meals)}。请为用户生成未来一周早、中、晚饭的完整计划。"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个擅长制定营养餐计划的助手。"},
                {"role": "user", "content": prompt}
            ]
        )

        meal_plan = response['choices'][0]['message']['content']

        # 返回生成的 meal plan
        return jsonify({'meal_plan': meal_plan})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)