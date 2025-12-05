async function fetchFoods() {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/foods");
    return await response.json(); // returns array of foods
  } catch (error) {
    console.error("Error fetching foods:", error);
    return []; // return empty list on error
  }
}

function createFoodCard(food, index) {
  const card = document.createElement("article");
  card.className = "food-card";

  const imgDiv = document.createElement("div");
  imgDiv.className = "food-image";
  imgDiv.textContent = `Image ${index + 1}`;

  const contentDiv = document.createElement("div");
  contentDiv.className = "food-content";

  const textDiv = document.createElement("div");
  textDiv.className = "food-text";
  textDiv.innerHTML = `
    <h3>${food.name}</h3>
    <p>${food.description}</p>
    <p><strong>Cuisine:</strong> ${food.cuisine}</p>
    <p><strong>Location:</strong> ${food.location}</p>
  `;

  const actionsDiv = document.createElement("div");
  actionsDiv.className = "food-actions";

  const websiteLink = document.createElement("a");
  websiteLink.className = "website-btn";
  websiteLink.href = food.website;
  websiteLink.target = "_blank";
  websiteLink.rel = "noopener noreferrer";
  websiteLink.textContent = "Website";

  actionsDiv.appendChild(websiteLink);

  contentDiv.appendChild(textDiv);
  contentDiv.appendChild(actionsDiv);
  card.appendChild(imgDiv);
  card.appendChild(contentDiv);

  return card;
}

async function renderFoods() {
  const foodsList = document.getElementById("foodsList");

  if (!foodsList) {
    console.error("Element with ID 'foodsList' not found.");
    return;
  }

  foodsList.innerHTML = "";

  const foods = await fetchFoods();

  foods.forEach((food, idx) => {
    foodsList.appendChild(createFoodCard(food, idx));
  });
}

document.addEventListener("DOMContentLoaded", renderFoods);
