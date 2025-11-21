    // Utility to display survey data
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
    function showSurveys() {
      const surveys = loadSurveys();
      const previousDiv = document.getElementById("previousSurveys");
      if (!surveys.length) {
        previousDiv.innerHTML = "<p>No previous surveys yet.</p>";
      } else {
        previousDiv.innerHTML = surveys.slice(0,-1).reverse().map(renderSurvey).join("");
      }
    }

    // Show latest survey results
    function showLatestSurvey() {
      const surveys = loadSurveys();
      if (surveys.length) {
        document.getElementById("latestSurvey").style.display = "block";
        document.getElementById("latestResults").innerHTML = renderSurvey(surveys[surveys.length-1]);
      } else {
        document.getElementById("latestSurvey").style.display = "none";
        document.getElementById("latestResults").innerHTML = "";
      }
    }

    // Reset to allow new survey
    function startNewSurvey() {
      document.getElementById('surveyForm').reset();
      document.getElementById('confirmation').style.display = 'none';
      document.getElementById('latestSurvey').style.display = 'none';
    }

    // Survey submit handler
    document.getElementById('surveyForm').addEventListener('submit', function(event) {
      event.preventDefault();
      const formData = new FormData(event.target);
      const data = {};
      for (const [key, value] of formData.entries()) { data[key] = value; }
      saveSurvey(data);
      document.getElementById('confirmation').style.display = 'block';
      showLatestSurvey();
      showSurveys();
    });

    // Handle "New Survey" button
    document.getElementById('newSurveyBtn').addEventListener('click', startNewSurvey);

    // Show surveys on load
    showLatestSurvey();
    showSurveys();