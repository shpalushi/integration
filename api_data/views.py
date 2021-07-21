import sys

import requests
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import os
import dotenv


# Create your views here.
from klaviyo_integration.settings import BASE_DIR


@method_decorator(csrf_exempt, name="dispatch")
class KlaviyoData(View):

    def post(self, request):

        print(request.META['HTTP_HOST'])

        # begin: get the user data from request
        data = json.loads(request.body.decode("utf-8"))
        customer_title = data.get("customer_title")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        phone = data.get("phone")
        email = data.get("email")
        date_of_birth = data.get("date_of_birth")
        country = data.get("country")
        way_of_contact = data.get("way_of_contact")
        education = data.get("education")
        institution = data.get("institution")
        work_experience = data.get("work_experience")
        pay_type = data.get("pay_type")
        course_sku = data.get("course_name")
        course_name = ""
        lead_type = ""
        course_start_date = '01-01-2020'

        if course_sku == "course-v1:MIT+AIL+10-2021":
            course_name = "MIT AI Leadership"
            lead_type = "Register"
            course_start_date = '01-07-2020'
        # end: get the user data from request

        # get api key from secrets file
        dotenv_file = os.path.join(BASE_DIR, ".env")
        if os.path.isfile(dotenv_file):
            dotenv.load_dotenv(dotenv_file)
        api_key = os.environ['API_KEY']

        # prepare json body
        json_data_send = {
            "token": api_key,
            "event": "Account creation",
            "customer_properties": {
                "salutation": customer_title,
                "date_of_birth": date_of_birth,
                "education": education,
                "$email": email,
                "$first_name": first_name,
                "institution": institution,
                "$last_name": last_name,
                "pay_type": pay_type,
                "$phone_number": phone,
                "way_of_contact": way_of_contact,
                "experience": work_experience,
                "$country": country,
                "course_sku": course_sku,
                "course_name": course_name,
                "lead_type": lead_type,
                "course_start_date": course_start_date
            }
        }

        # prepare and send the request
        url = "https://a.klaviyo.com/api/track"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        http_request = requests.post(url, data=json.dumps(json_data_send), headers=headers);

        # check the status of the response
        if http_request.text == '1':
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=400)

