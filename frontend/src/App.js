import React, {useState} from "react";
import MealCalendar from "./MealCalendar";
import "./styles.css";

function App() {
  const axios = require('axios').default;
  const instance = axios.create({baseURL: 'http://127.0.0.1:5000'});
  const [dishes, setDishes] = useState("");
  const [mealPlan, setMealPlan] = useState(null);

  const handleSubmit = async (e) => {
    
    e.preventDefault();
    instance.post('/generate_meal_plan', {
      "Content-Type": "application/json"
    }).then(function(response){
      console.log(response)
    });
      
    const data = await response.json();
    if (response.ok) {
      setMealPlan(data.meal_plan);
    } else {
      console.error(data.error);
    }
  
  };

  return (
    <div className="App">
      <h1>Weekly Meal Planner</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Enter Dishes (comma-separated):
          <input
            type="text"
            value={dishes}
            onChange={(e) => setDishes(e.target.value)}
            placeholder="e.g., Pizza, Salad, Soup"
          />
        </label>
        <button type="submit">Generate Meal Plan</button>
      </form>
      {mealPlan && <MealCalendar mealPlan={mealPlan} />}
    </div>
  );
}

export default App;
