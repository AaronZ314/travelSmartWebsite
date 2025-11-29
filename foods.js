// Sample static data for now (can be replaced with fetch from Flask later)
const foods = [
  {
    name: "Food place 1",
    description: "Someone replace this please!",
    location: "Manhattan, NYC",
    website: ""
  },
  {
    name: "Food place 2",
    description: "Someone replace this please!",
    location: "Brooklyn, NYC",
    website: ""
  },
  {
    name: "Food place 3",
    description: "Someone replace this please!",
    location: "Queens, NYC",
    website: ""
  }
];

function createPlaceCard(place, index) {
  const card = document.createElement("article");
  card.className = "place-card";

  const imgDiv = document.createElement("div");
  imgDiv.className = "place-image";
  imgDiv.textContent = `Image ${index + 1}`; // placeholder text for now

  const contentDiv = document.createElement("div");
  contentDiv.className = "place-content";

  const textDiv = document.createElement("div");
  textDiv.className = "place-text";
  textDiv.innerHTML = `
    <h3>${place.name}</h3>
    <p>${place.description}</p>
    <p><strong>Location:</strong> ${place.location}</p>
  `;

  const actionsDiv = document.createElement("div");
  actionsDiv.className = "place-actions";

  const websiteLink = document.createElement("a");
  websiteLink.className = "website-btn";
  websiteLink.href = place.website;
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

function renderPlaces() {
  const list = document.getElementById("foodsList");
  foods.forEach((food, idx) => {
    list.appendChild(createPlaceCard(food, idx));
  });
}

document.addEventListener("DOMContentLoaded", renderPlaces);
