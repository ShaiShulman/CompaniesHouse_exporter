# api.py

from requests.auth import HTTPBasicAuth
from urllib.parse import quote_plus
import pprint
import json
import requests

KEY = "HCAM36mMUItP0w3Rs16EKvaiiVN1QJucgJdbeG13"
URL_PROFILE = "https://api.companieshouse.gov.uk/company/"
URL_OFFICERS = "/officers"
COMPANY_NUM_LEN = 8


def fill_company_number(num):
    return ("0" * (COMPANY_NUM_LEN - len(num))) + num


def get_resource(url, company_num):
    return get_resource_fullurl(url + company_num)


def get_resource_fullurl(url, params={}):
    response = requests.get(url, auth=HTTPBasicAuth(KEY, ''), params=params)
    if response.status_code == 404:
        return None
    return json.loads(response.text)


def get_next_confirmation_date(company_numbers):
    results = {}
    for num in company_numbers:
        response = get_resource(URL_PROFILE, fill_company_number(num))
        if response:
            try:
                results[num] = response["confirmation_statement"]["next_due"]
            except IndexError:
                results[num] = None
        else:
            results[num] = None
    return results


def get_officers(company_numbers, filter_directors=True):
    results = {}
    for num in company_numbers:
        response = get_resource_fullurl(URL_PROFILE + fill_company_number(num) + URL_OFFICERS)
        if response:
            results[num] = [(' '.join([k.strip().title() for k in reversed(i['name'].split(','))]))
                            for i in response["items"] if not "resigned_on" in i and (
                                        (filter_directors and i["officer_role"] == "director") or (
                                            not filter_directors and i["officer_role"] != "director"))]
        else:
            results[num] = None
    return results
