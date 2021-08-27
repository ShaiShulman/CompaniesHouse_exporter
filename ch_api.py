# ch_api.py
""" Companies House API calls for companies_house_viewer.py


"""
from requests.auth import HTTPBasicAuth
from datetime import datetime
import json
import requests

URL_PROFILE = "https://api.companieshouse.gov.uk/company/"
URL_OFFICERS = "/officers"
COMPANY_NUM_LEN = 8  # number of digits in compan


def fill_company_number(num):
    """ Add leading zeros to a company number
    """
    return ("0" * (COMPANY_NUM_LEN - len(str(num)))) + str(num)


def get_resource(url, company_num, key):
    """

    Args:
        url: base method API utl
        company_num: comapnies number
        key: API key

    Returns:

    """
    return get_resource_fullurl(url + company_num, key)


def get_resource_fullurl(url, key, params={}):
    """ Get specific type of resource (query) from a specific API URL

    Args:
        url: API urls
        key: Companies House API key
        params: paraneters to use in HTTP request


    Returns:
        json response

    """
    response = requests.get(url, auth=HTTPBasicAuth(key, ''), params=params)
    if response.status_code == 404:
        return None
    return json.loads(response.text)


def get_profile(company_num, key):
    """ Get basic information for a company

    Args:
        company_num:  company number as string
        key: Companies House API key

    Returns:
        dictionary with the information received, None if company number could not be found

    """
    profile = {}
    response = get_resource(URL_PROFILE, fill_company_number(company_num), key)
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
                                            ['address_line_1', 'address_line_2', 'care_of', 'locality', 'postal_code',
                                             'country', 'premises']
                                            if addr.get(x, None)
                                            ])
    return profile


def get_officers(company_num, key, filter_directors=True):
    """ Get list of current officers and directors in a company

    Args:
        company_num: number of a company
        key: Companies House API key
        filter_directors: True if list should return only directors

    Returns:
        multi-line string with full names of the directors / officers, None if not found

    """
    response = get_resource_fullurl(URL_PROFILE + fill_company_number(company_num) + URL_OFFICERS, key)
    if response:
        return '\n'.join([(' '.join([k.strip().title() for k in reversed(i['name'].split(','))]))
                          for i in response["items"] if "resigned_on" not in i and (
                                  (filter_directors and i["officer_role"] == "director") or (
                                  not filter_directors and i["officer_role"] != "director"))])
