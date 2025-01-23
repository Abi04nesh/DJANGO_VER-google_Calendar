#  Django Google Calendar 

This project, **Django Google Calendar**, is a Django-based application that integrates with Google Calendar to manage events. It includes functionalities for scheduling, notifying, and handling event-related workflows.


## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd abi04nesh-django_ver-google_calendar
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up Google Calendar API credentials:
   - Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google Calendar API.
   - Download the credentials JSON file and place it in the project directory.
   - Update the path to the credentials in `utils.py`.

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Usage
1. **Homepage**:
   - Visit the homepage (`home.html`) to manage events.
2. **Create Events**:
   - Use the event creation form to add events to Google Calendar.
3. **Email Notifications**:
   - Automated emails are sent for event confirmations and HR notifications using the templates in `emails/`.

## Dependencies
- Python 3.x
- Django
- Google Calendar API
- Any additional dependencies listed in `requirements.txt`

To install dependencies, run:
```bash
pip install -r requirements.txt
```

## suggestion

- Ensure the `credentials.json` file is correctly configured for Google Calendar API access.
- Email settings in `settings.py` must be configured for sending notifications.
