from requests import get
import pandas as pd


def get_data(url):
    response = get(endpoint, timeout=10)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: {response.text}')

    return response.json()


if __name__ == '__main__':
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=utla;areaCode=E08000021&'
        'structure={"date":"date","areaName":"areaName","newCasesBySpecimenDate":"newCasesBySpecimenDate",'
        '"newDeathsByDeathDate":"newDeathsByDeathDate"} '
    )


json_data = get_data(endpoint)

localauth_data = []

for day in json_data['data']:
    localauth_data.append([day['date'],day['newCasesBySpecimenDate'],day['newDeathsByDeathDate']])

localauth_df = pd.DataFrame(data=localauth_data, columns=['Date', 'Daily Cases', 'Daily Deaths'])




