import sys

import requests
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import os


# Create your views here.
from django_amazon.settings import BASE_DIR


def get_course_data(course_sku):
    if course_sku == "course-v1:OXF+FIN+03-2021":
        return ["Register", "Oxford Fintech", "31 March 2021"]
    elif course_sku == "course-v1:OXF+FIN+06-2021":
        return ["Register", "Oxford Fintech", "9 June 2021"]
    elif course_sku == "course-v1:OXF+FIN+10-2021":
        return ["Register", "Oxford Fintech", "13 Oct 2021"]
    elif course_sku == "course-v1:OXF+FIN+01-2022":
        return ["Register", "Oxford Fintech", "19 January 2022"]
    elif course_sku == "course-v1:OXF+CYB+03-2021":
        return ["Register", "Oxford Cyber Security", "31 March 2021"]
    elif course_sku == "course-v1:OXF+CYB+06-2021":
        return ["Register", "Oxford Cyber Security", "16 June 2021"]
    elif course_sku == "course-v1:OXF+CYB+10-2021":
        return ["Register", "Oxford Cyber Security", "13 Oct 2021"]
    elif course_sku == "course-v1:OXF+CYB+01-2022":
        return ["Register", "Oxford Cyber Security", "12 January 2022"]
    elif course_sku == "course-v1:OXF+AIF+03-2021":
        return ["Register", "Oxford AI in Finance", "26 May 2021"]
    elif course_sku == "course-v1:OXF+AIF+10-2021":
        return ["Register", "Oxford AI in Finance", "13 Oct 2021"]
    elif course_sku == "course-v1:OXF+AIF+01-2022":
        return ["Register", "Oxford AI in Finance", "19 January 2022"]
    elif course_sku == "course-v1:MIT+HVN+06-2021":
        return ["Register", "MIT Leading Health Tech Innovation", "16 June 2021"]
    elif course_sku == "course-v1:MIT+HVN+10-2021":
        return ["Register", "MIT Leading Health Tech Innovation", "29 September 2021"]
    elif course_sku == "course-v1:MIT+AIL+07-2021":
        return ["Register", "MIT AI Leadership", "7 July 2021"]
    elif course_sku == "course-v1:MIT+AIL+10-2021":
        return ["Register", "MIT AI Leadership", "6 October 2021"]
    elif course_sku == "TEST+TST101+2021_T1":
        return ["Register", "Test Product", "22 September 2021"]
    elif course_sku == "course-v1:OXF+BCH+09-2021":
        return ["Register", "Oxford Blockchain Strategy", "22 September 2021"]
    elif course_sku == "course-v1:OXF+PLT+10-2021":
        return ["Register", "Oxford Platforms and Digital Disruption Programme", "6 October 2021"]
    elif course_sku == "course-v1:OXF+PLT+01-2022":
        return ["Register", "Oxford Platforms and Digital Disruption Programme", "19 January 2022"]
    elif course_sku == "course-v1:CAM+STF+10-2021":
        return ["Register", "Cambridge Startup Funding Pre-seed to Exit Programme", "13 October 2021"]
    elif course_sku == "course-v1:CAM+REG+10-2021":
        return ["Register", "Cambridge RegTech", "20 October 2021"]
    elif course_sku == "course-v1:MIT+AIS+10-2021":
        return ["Register", "MIT AI + Data Strategy", "20 October 2021"]
    else:
        return ["Register", "Registered directly", "No date"]

@method_decorator(csrf_exempt, name="dispatch")
class KlaviyoData(View):

    def post(self, request):

        print(request.META['HTTP_HOST'])

        # begin: get the user data from request
        data = json.loads(request.body.decode("utf-8"))
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        http_request = requests.post("http://django-env.eba-pqmphmpr.us-west-2.elasticbeanstalk.com/send-data-klaviyo/", data=json.dumps(data), headers=headers);
        print(http_request.text);
        if http_request.text.__contains__("true"):
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=400)

