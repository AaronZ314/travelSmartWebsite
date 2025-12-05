
async function fetchPlaces() {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/places");
    return await response.json(); // returns array of places
  } catch (error) {
    console.error("Error fetching places:", error);
    return []; // fallback if backend fails
  }
}

function createPlaceCard(place, index) {
  const card = document.createElement("article");
  card.className = "place-card";

  const imgDiv = document.createElement("div");
  imgDiv.className = "place-image";
  imgDiv.textContent = `Image ${index + 1}`;

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

  const aiLink = document.createElement("a");
  aiLink.className = "website-btn";
  aiLink.href = place.ai_overview || place.website || "#";
  aiLink.target = "_blank";
  aiLink.rel = "noopener noreferrer";
  aiLink.textContent = "AI Overview";

  actionsDiv.appendChild(aiLink);

  contentDiv.appendChild(textDiv);
  contentDiv.appendChild(actionsDiv);

  card.appendChild(imgDiv);
  card.appendChild(contentDiv);

  return card;
}

async function renderPlaces() {
  const list = document.getElementById("placesList");

  if (!list) {
    console.error("Element with ID 'placesList' not found.");
    return;
  }

  list.innerHTML = "";

  const places = await fetchPlaces();

  places.forEach((place, idx) => {
    list.appendChild(createPlaceCard(place, idx));
  });
}

document.addEventListener("DOMContentLoaded", renderPlaces);
