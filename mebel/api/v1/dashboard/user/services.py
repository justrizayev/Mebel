import requests


def ctg_list_by_api():

    url = "http://127.0.0.1:8000/api/v1/ctg/list/"

    payload = {}
    headers = {
        'Authorization': 'Bearer 5a164f5784358089a725e0a7a945cfb06961ad39',
        'Cookie': 'csrftoken=5JZIarHU2AldHdCneutFgAkjQpmFf4B9'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()























