// Utility for previous surveys (with delete button)
function renderSurveyWithDelete(data, index) {
  return `
    <div class="survey-entry">
      <button class="delete-btn" data-delete-index="${index}">Delete</button>
      <strong>Attractions:</strong> ${data.attractions}<br>
      <strong>Climate:</strong> ${data.climate}<br>
      <strong>Distance:</strong> ${data.distance}<br>
      <strong>Cuisine:</strong> ${data.cuisine}<br>
      <strong>Restrictions:</strong> ${data.restrictions}<br>
      <strong>Dining Style:</strong> ${data.diningStyle}<br>
      <strong>Trip Budget:</strong> ${data.tripBudget}<br>
      <strong>Meal Budget:</strong> ${data.mealBudget}<br>
      <strong>Budget Strictness:</strong> ${data.strictBudget}
    </div>`;
}

// Utility for the latest survey (no delete button)
function renderSurvey(data) {
  return `
    <div class="survey-entry">
      <strong>Attractions:</strong> ${data.attractions}<br>
      <strong>Climate:</strong> ${data.climate}<br>
      <strong>Distance:</strong> ${data.distance}<br>
      <strong>Cuisine:</strong> ${data.cuisine}<br>
      <strong>Restrictions:</strong> ${data.restrictions}<br>
      <strong>Dining Style:</strong> ${data.diningStyle}<br>
      <strong>Trip Budget:</strong> ${data.tripBudget}<br>
      <strong>Meal Budget:</strong> ${data.mealBudget}<br>
      <strong>Budget Strictness:</strong> ${data.strictBudget}
    </div>`;
}

function loadSurveys() {
  const saved = localStorage.getItem("travelSmartSurveys");
  return saved ? JSON.parse(saved) : [];
}

function saveSurvey(newSurvey) {
  const surveys = loadSurveys();
  surveys.push(newSurvey);
  localStorage.setItem("travelSmartSurveys", JSON.stringify(surveys));
}

function deleteSurvey(index) {
  const surveys = loadSurveys();
  surveys.splice(index, 1);
  localStorage.setItem("travelSmartSurveys", JSON.stringify(surveys));
  showLatestSurvey();
  showSurveys();
}

async function saveSurveyBackend(data) {
  try {
    const res = await fetch("http://127.0.0.1:5000/api/surveys", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    if (!res.ok) {
      console.error("Backend did NOT accept the survey.");
    }
  } catch (err) {
    console.error("Error connecting to backend:", err);
  }
}

function showSurveys() {
  const surveys = loadSurveys();
  const previousDiv = document.getElementById("previousSurveys");

  if (surveys.length <= 1) {
    previousDiv.innerHTML = "<p>No previous surveys yet.</p>";
    return;
  }

  let entries = "";
  for (let i = surveys.length - 2; i >= 0; i--) {
    entries += renderSurveyWithDelete(surveys[i], i);
  }

  previousDiv.innerHTML = entries;

  const deleteButtons = previousDiv.querySelectorAll(".delete-btn");
  deleteButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const idx = parseInt(btn.getAttribute("data-delete-index"), 10);
      deleteSurvey(idx);
    });
  });
}

function showLatestSurvey() {
  const surveys = loadSurveys();
  const latestDiv = document.getElementById("latestSurvey");
  const resultsDiv = document.getElementById("latestResults");

  if (!surveys.length) {
    latestDiv.style.display = "none";
    resultsDiv.innerHTML = "";
    return;
  }

  latestDiv.style.display = "block";
  resultsDiv.innerHTML = renderSurvey(surveys[surveys.length - 1]);
}

document.getElementById("surveyForm").addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);
  const data = {};
  for (const [key, value] of formData.entries()) {
    data[key] = value;
  }

  // Save locally + backend
  saveSurvey(data);
  await saveSurveyBackend(data);

  document.getElementById("confirmation").style.display = "block";
  showLatestSurvey();
  showSurveys();

  // Fetch recommendation summary for popup
  try {
    const res = await fetch("http://127.0.0.1:5000/api/recommend-summary");
    const summary = await res.json();
    showRecommendationModal(summary);
  } catch (err) {
    console.error("Error fetching recommendation summary:", err);
  }
});

function showRecommendationModal(rec) {
  const modal = document.getElementById("resultModal");
  const foodDiv = document.getElementById("modalFood");
  const placeDiv = document.getElementById("modalPlace");

  if (!modal || !foodDiv || !placeDiv) {
    console.warn("Modal elements missing in HTML.");
    return;
  }

  if (rec.error) {
    foodDiv.innerHTML = "<p>No survey found — complete one first!</p>";
    placeDiv.innerHTML = "";
  } else {
    const food = rec.food || {};
    const place = rec.place || {};

    foodDiv.innerHTML = `
      <h3>Recommended Food: ${food.name || "N/A"}</h3>
      <p>${food.description || ""}</p>
      <p><strong>Location:</strong> ${food.location || ""}</p>
    `;

    placeDiv.innerHTML = `
      <h3>Recommended Place: ${place.name || "N/A"}</h3>
      <p>${place.description || ""}</p>
      <p><strong>Location:</strong> ${place.location || place.borough || ""}</p>
    `;
  }

  modal.style.display = "flex";
}

const closeBtn = document.getElementById("closeModalBtn");
if (closeBtn) {
  closeBtn.addEventListener("click", () => {
    document.getElementById("resultModal").style.display = "none";
  });
}

const modalRoot = document.getElementById("resultModal");
if (modalRoot) {
  modalRoot.addEventListener("click", (e) => {
    if (e.target.id === "resultModal") {
      modalRoot.style.display = "none";
    }
  });
}

// Initial render when page loads
showLatestSurvey();
showSurveys();
