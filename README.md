1. Create and activate a virtual environment
In the VS Code terminal, inside the project folder:

bash
python3 -m venv venv

Then activate it:

macOS / Linux:
source venv/bin/activate
They should now see (venv) in the terminal prompt.​

2. Install dependencies
From the same activated venv, run:

bash
pip install flask flask-cors
If you add a requirements.txt, they can instead do:

bash
pip install -r requirements.txt
4. Run the Flask app
Still in the project folder and with the venv active:

bash
python app.py
They should see “Running on http://127.0.0.1:5000/” and can then open:

http://127.0.0.1:5000/ for the backend, and

survey.html, index.html etc. from the cloned folder (via Live Server or by opening the files directly) for the frontend.​

As long as they keep the Flask server running in that terminal, your survey and popup features will work the same on their VS Code setup.
