import requests
import xmltodict
import json


def get_current_and_voltage() -> dict[str, str]:
    address = json.load(open('config.json'))['address']
    xml_response = requests.get('http://' + address + '/status.xml').text
    response_json = json.dumps(xmltodict.parse(xml_response))
    response_dict = json.loads(response_json)
    data = dict(response_dict['response'])

    return {
        "V_L1-L2": data['Ud1'],
        "V_L2-L3": data['Ud2'],
        "V_L3-L1": data['Ud3'],
        "V_L1": data['Us1'],
        "V_L2": data['Us2'],
        "V_L3": data['Us3'],
        "A_L1": data['I1'],
        "A_L2": data['I2'],
        "A_L3": data['I3'],
        "A_N": data['I4'],
    }


if __name__ == "__main__":
    print(get_current_and_voltage())
