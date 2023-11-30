import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import event
import parse

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def connect():
	"""Shows basic usage of the Google Calendar API.
	Prints the start and name of the next 10 events on the user's calendar.
	"""
	creds = None
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists("token.json"):
		print('x')
		creds = Credentials.from_authorized_user_file("token.json", SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
			"credentials.json", SCOPES
			)
			creds = flow.run_local_server(port=0)
			# Save the credentials for the next run
			with open("token.json", "w") as token:
				token.write(creds.to_json())

	try:
		service = build("calendar", "v3", credentials=creds)

	# Call the Calendar API
		now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
		return service

	except HttpError as error:
		print(f"An error occurred: {error}")
  
  
def get_calendars(service):
	cal_list = service.calendarList().list().execute()
	id_dict = {}
	
	# gets calendar : calendar_id of writable calendars
	for calendar in cal_list["items"]:
		if(calendar["accessRole"] == "owner" or calendar["accessRole"] == "writer"):
			id_dict[calendar["summary"]] = calendar["id"]
	
	return id_dict
  
	
def main():
	filepath = '../files/schedule.pdf'
	
	service = connect()
	courses = parse.parse_pdf(filepath)
	cal_dict = get_calendars(service)

	e_list = []

	for c in courses:
		e_list.append(event.course_to_event(c))
  
	for e in e_list:
		if e != None:
			e = service.events().insert(calendarId=cal_dict["API test"], body=e).execute()
			print('Event created: %s' % (e.get('htmlLink')))
	


if __name__ == "__main__":
	main()

