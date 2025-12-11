async function fetchPlaces() {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/places");
    if (!response.ok) {
      throw new Error("Failed to fetch /api/places");
    }
    return await response.json(); // array of 3 places from backend
  } catch (error) {
    console.error("Error loading places:", error);
    return [];
  }
}

function createPlaceCard(place, index) {
  const card = document.createElement("article");
  card.className = "place-card";

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
  websiteLink.href = place.website || "#";
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

async function renderPlaces() {
  const list = document.getElementById("placesList");
  list.innerHTML = "";

  const places = await fetchPlaces();
  places.forEach((place, idx) => {
    list.appendChild(createPlaceCard(place, idx));
  });
}

document.addEventListener("DOMContentLoaded", renderPlaces);
