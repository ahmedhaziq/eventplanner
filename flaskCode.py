from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store food and quantity data
food_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global food_data
    
    if request.method == 'POST':
        # Get the input values from the form
        food = request.form['food']
        quantity = request.form['quantity']
        
        # Append the data to the food_data list
        food_data.append((food, quantity))
        
        # Redirect to the same page to update the table
        return redirect(url_for('index'))
    
    # Render the calendar and pass the food data
    return render_template('index.html', food_data=food_data)

if __name__ == '__main__':
    app.run(debug=True)
