import urllib.parse
from datetime import datetime, timedelta

def generate_google_calendar_link(candidate_name, interview_date, interview_time, location):
    base_url = "https://www.google.com/calendar/render?action=TEMPLATE"
    title = f"Interview with {candidate_name}"

    # Parse date and time into a datetime object
    start_dt = datetime.strptime(f"{interview_date} {interview_time}", "%Y-%m-%d %H:%M")
    end_dt = start_dt + timedelta(hours=1)  # Assuming a 1-hour interview

    # Format the start and end dates in Google Calendar's required format
    datetime_start = start_dt.strftime("%Y%m%dT%H%M%SZ")
    datetime_end = end_dt.strftime("%Y%m%dT%H%M%SZ")

    # Event details and parameters
    details = f"Interview with {candidate_name}"
    params = {
        "text": title,
        "dates": f"{datetime_start}/{datetime_end}",
        "details": details,
        "location": location,
    }

    # Construct and return the full URL
    return base_url + "&" + urllib.parse.urlencode(params)
