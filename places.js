// Sample static data for now (can be replaced with fetch from Flask later)
const places = [
  {
    name: "Central Park",
    description: "Large urban park with walking paths, lakes, and open fields.",
    location: "Manhattan, NYC",
    website: "https://www.centralparknyc.org/"
  },
  {
    name: "Brooklyn Museum",
    description: "One of the largest and oldest art museums in the United States.",
    location: "Brooklyn, NYC",
    website: "https://www.brooklynmuseum.org/"
  },
  {
    name: "Flushing Meadows–Corona Park",
    description: "Historic park known for the Unisphere and wide open spaces.",
    location: "Queens, NYC",
    website: "https://www.nycgovparks.org/parks/flushing-meadows-corona-park"
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
  const list = document.getElementById("placesList");
  places.forEach((place, idx) => {
    list.appendChild(createPlaceCard(place, idx));
  });
}

document.addEventListener("DOMContentLoaded", renderPlaces);
