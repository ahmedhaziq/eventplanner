import React from "react";

function MealCalendar({ mealPlan }) {
  const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
  
  const plan = mealPlan.split("\n").filter(line => line.trim() !== ""); // Parse ChatGPT's response

  return (
    <div className="calendar">
      <h2>Weekly Meal Plan</h2>
      <div className="calendar-grid">
        {days.map((day, index) => (
          <div key={index} className="calendar-day">
            <h3>{day}</h3>
            <p>{plan[index]}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MealCalendar;
