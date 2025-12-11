async function fetchFoods() {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/foods");
    if (!response.ok) {
      throw new Error("Failed to fetch /api/foods");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching foods:", error);
    return [];
  }
}

function createFoodCard(food, index) {
  const card = document.createElement("article");
  card.className = "food-card";

  const contentDiv = document.createElement("div");
  contentDiv.className = "food-content";

  const textDiv = document.createElement("div");
  textDiv.className = "food-text";
  textDiv.innerHTML = `
    <h3>${food.name}</h3>
    <p>${food.description}</p>
    <p><strong>Location:</strong> ${food.location}</p>
  `;

  const actionsDiv = document.createElement("div");
  actionsDiv.className = "food-actions";

  const websiteLink = document.createElement("a");
  websiteLink.className = "website-btn";
  websiteLink.href = food.website || "#";
  websiteLink.target = "_blank";
  websiteLink.rel = "noopener noreferrer";
  websiteLink.textContent = "Website";

  actionsDiv.appendChild(websiteLink);

  contentDiv.appendChild(textDiv);
  contentDiv.appendChild(actionsDiv);

  card.appendChild(contentDiv);

  return card;
}

async function renderFoods() {
  const list = document.getElementById("foodsList");
  list.innerHTML = "";

  const foods = await fetchFoods();
  foods.forEach((food, idx) => {
    list.appendChild(createFoodCard(food, idx));
  });
}

document.addEventListener("DOMContentLoaded", renderFoods);
