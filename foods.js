// Sample static restaurant data for now
const foods = [
  {
    name: "Joe's Pizza",
    description: "Classic New York–style slices with a crispy thin crust.",
    location: "Greenwich Village, Manhattan",
    website: "https://www.joespizzanyc.com/"
  },
  {
    name: "Katz's Delicatessen",
    description: "Famous deli known for pastrami sandwiches and classic NYC vibes.",
    location: "Lower East Side, Manhattan",
    website: "https://katzsdelicatessen.com/"
  },
  {
    name: "Di Fara Pizza",
    description: "Legendary Brooklyn pizzeria with hand-crafted pies.",
    location: "Midwood, Brooklyn",
    website: "https://difarapizzany.com/"
  }
];

function createFoodCard(food, index) {
  const card = document.createElement("article");
  card.className = "food-card";

  const imgDiv = document.createElement("div");
  imgDiv.className = "food-image";
  imgDiv.textContent = `Image ${index + 1}`; // placeholder for now

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

function renderFoods() {
  const list = document.getElementById("foodsList");
  foods.forEach((food, idx) => {
    list.appendChild(createFoodCard(food, idx));
  });
}

document.addEventListener("DOMContentLoaded", renderFoods);
