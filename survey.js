// Utility to display survey data with delete button (for previous surveys)
function renderSurveyWithDelete(data, index) {
  return `<div class="survey-entry">
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
  return `<div class="survey-entry">
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

// Load previous surveys from localStorage
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
    const response = await fetch("http://127.0.0.1:5000/api/surveys", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      console.error("Backend survey submission failed.");
    }
  } catch (err) {
    console.error("Error sending survey to backend:", err);
  }
}

function showSurveys() {
  const surveys = loadSurveys();
  const previousDiv = document.getElementById("previousSurveys");

  if (!surveys.length || surveys.length === 1) {
    previousDiv.innerHTML = "<p>No previous surveys yet.</p>";
    return;
  }

  let entries = "";
  for (let i = surveys.length - 2; i >= 0; i--) {
    entries += renderSurveyWithDelete(surveys[i], i);
  }

  previousDiv.innerHTML = entries;

  const deleteButtons = previousDiv.querySelectorAll(".delete-btn");
  deleteButtons.forEach(btn => {
    btn.addEventListener("click", function () {
      const idx = parseInt(btn.getAttribute("data-delete-index"));
      deleteSurvey(idx);
    });
  });
}

function showLatestSurvey() {
  const surveys = loadSurveys();

  if (surveys.length) {
    document.getElementById("latestSurvey").style.display = "block";
    document.getElementById("latestResults").innerHTML =
      renderSurvey(surveys[surveys.length - 1]);
  } else {
    document.getElementById("latestSurvey").style.display = "none";
    document.getElementById("latestResults").innerHTML = "";
  }
}

document.getElementById("surveyForm").addEventListener("submit", async function (event) {
  event.preventDefault();

  const formData = new FormData(event.target);
  const data = {};
  for (const [key, value] of formData.entries()) {
    data[key] = value;
  }

  saveSurveyLocal(data);

  await saveSurveyBackend(data);

  document.getElementById("confirmation").style.display = "block";
  showLatestSurvey();
  showSurveys();
});

document.getElementById("newSurveyBtn").addEventListener("click", function () {
  document.getElementById("surveyForm").reset();
  document.getElementById("confirmation").style.display = "none";
  document.getElementById("latestSurvey").style.display = "none";
});

showLatestSurvey();
showSurveys();
