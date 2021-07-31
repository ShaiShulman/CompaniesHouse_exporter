# api.py

from requests.auth import HTTPBasicAuth
from datetime import datetime
import json
import requests

KEY = "HCAM36mMUItP0w3Rs16EKvaiiVN1QJucgJdbeG13"
URL_PROFILE = "https://api.companieshouse.gov.uk/company/"
URL_OFFICERS = "/officers"
COMPANY_NUM_LEN = 8


def fill_company_number(num):
    return ("0" * (COMPANY_NUM_LEN - len(str(num)))) + str(num)


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


def get_profile(company_num):
    profile = {}
    response = get_resource(URL_PROFILE, fill_company_number(company_num))
    if response:
        try:
            profile['company_name'] = response['company_name'] = response["company_name"]
        except KeyError:
            pass
        try:
            profile['next_confirmation'] = response["confirmation_statement"]["next_due"]
        except KeyError:
            pass
        else:
            profile['next_confirmation'] = datetime.strptime(profile['next_confirmation'], "%Y-%m-%d").date()
        try:
            profile['next_accounts'] = response['accounts']['next_due']
        except KeyError:
            pass
        else:
            profile['next_accounts'] = datetime.strptime(profile['next_accounts'], "%Y-%m-%d").date()
        try:
            addr = response['registered_office_address']
        except KeyError:
            pass
        else:
            profile['address'] = ', '.join([addr.get(x, None) for x in
                       ['address_line_1', 'address_line_2', 'care_of', 'locality', 'postal_code', 'country', 'premises']
                       if addr.get(x, None)
                       ])
    return profile


def get_officers(company_num, filter_directors=True):
    response = get_resource_fullurl(URL_PROFILE + fill_company_number(company_num) + URL_OFFICERS)
    if response:
        return '\n'.join([(' '.join([k.strip().title() for k in reversed(i['name'].split(','))]))
                for i in response["items"] if "resigned_on" not in i and (
                        (filter_directors and i["officer_role"] == "director") or (
                        not filter_directors and i["officer_role"] != "director"))])
