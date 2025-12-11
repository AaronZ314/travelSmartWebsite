1. Create and activate a virtual environment
Mac/Linux:

python3 -m venv venv

source venv/bin/activate​

Windows (cmd or PowerShell):

python -m venv venv

venv\Scripts\activate​

2. Install required packages
With the venv active (you should see (venv) in the prompt):

Install Flask:

pip install flask​

Install Flask-CORS (fixes the No module named flask_cors error):

pip install Flask-Cors​

3. Set the Flask app and run it
Assuming your main file is app.py and contains the Flask app object:

Mac/Linux:

export FLASK_APP=app.py

Windows (cmd/PowerShell):

set FLASK_APP=app.py​

Then start the server:

flask run​

Flask will show a URL like http://127.0.0.1:5000/; open that in a browser, or point your frontend to it as the backend API.​
