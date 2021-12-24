import requests
import datetime
import os

# --------------------------nutritionix API--------------------------------------#
site_url = 'https://developer.nutritionix.com/docs/v2'
NUTRITIONIX_USER_EMAIL = os.environ['NUTRITIONIX_USER_EMAIL']
NUTRITIONIX_PASSWORD = os.environ['NUTRITIONIX_PASSWORD']
NUTRITIONIX_APP_ID = os.environ['NUTRITIONIX_APP_ID']
NUTRITIONIX_API_KEY = os.environ['NUTRITIONIX_API_KEY']
HEIGHT_CM = 170
AGE = 37
WEIGHT_KG = 90
GENDER = 'male'
excercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise' #POST

headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    'x-remote-user-id': '0',
}

params = {
 "query":"ran 3 miles",
 "gender": GENDER ,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE,
}

user_input = input('What have you done today? ').lower()
params['query'] = user_input

r = requests.post(url=excercise_endpoint, json=params, headers=headers)
r.raise_for_status()
calories = r.json()['exercises'][0]['nf_calories']
activity = r.json()['exercises'][0]['name']
duration = r.json()['exercises'][0]['duration_min']


# --------------------------Sheety API------------------------------------------#
SHEETY_USER_NAME = os.environ['SHEETY_USER_NAME']
PROJECT_NAME = 'Workouts Tracker'
SHEET_NAME = 'workouts'
TOKEN = os.environ['TOKEN']
sheety_endpoint = f'https://api.sheety.co/{SHEETY_USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}'
KEY = os.environ['KEY']
sheety_get = f'https://api.sheety.co/{KEY}/workoutsTracker/workouts'
sheety_post = f'https://api.sheety.co/{KEY}/workoutsTracker/workouts'
# Authorization header
sheety_headers = {
    'Authorization': TOKEN,
}

today = datetime.datetime.now().strftime('%d/%m/%Y')
time = datetime.datetime.now().strftime('%H:%M:%S')
sheety_params = {
    'workout': {
    'date': today,
    'time': time,
    'exercise': activity.title(),
    'duration': duration,
    'calories': calories},
}
r_sheety = requests.post(url=sheety_post, json=sheety_params, headers=sheety_headers)
sheety_results = r_sheety.json() 
