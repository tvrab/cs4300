# Movie Theater Booking Application

## Live Deployment
* **Render URL:** https://cs4300-movie-booking-app.onrender.com

---

## Setup Instructions

1. **Navigate to the project directory:**
   ```bash
   cd homework2
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

---

## How to Run

### Local Development Server
```bash
python manage.py runserver
```

### Running Tests & Coverage
```bash
python manage.py test
coverage run --source=bookings manage.py test
coverage report
```

---

## Project Structure

```text
homework2/
├── manage.py
├── requirements.txt
├── movie_theater_booking/      # Project configuration (settings, wsgi, urls)
└── bookings/                   # Application folder
    ├── models.py               # Database schemas (Movie, Seat, Booking)
    ├── views.py                # Web & REST API view handlers
    ├── urls.py                 # App routing
    ├── serializers.py          # DRF API serializers
    ├── tests.py                # Automated unit & integration tests
    └── templates/              # HTML templates (base, list, booking, history)
```

---

## AI Usage Citation

* **Tool Used:** Gemini 

* **Areas of Usage:** 
1. **Documentation:** Drafted a project `README.md` file. 
2. **Conceptual Learning:** Acted as an interactive tutor explaining Django architecture, Model-View-Template (MVT) design, URL routing, and `settings.py` configuration. 
3. **Testing & Deployment:** Provided initial html templates and assisted with Gunicorn, WSGI configuration, and Render cloud deployment troubleshooting.

 * **Human Incorporation & Verification:** All AI-generated code snippets and documentation templates were reviewed, manually verified, and refactored to align with project requirements and local environment settings.
