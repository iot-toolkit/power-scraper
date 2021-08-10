import requests
import xmltodict
import json


def get_power() -> dict[str, str]:
    address = json.load(open('config.json'))['address']
    xml_response = requests.get('http://' + address + '/status1.xml').text
    response_json = json.dumps(xmltodict.parse(xml_response))
    response_dict = json.loads(response_json)
    data = dict(response_dict['response'])

    return {
        "P_L1": data['P1'],
        "P_L2": data['P2'],
        "P_L3": data['P3'],
        "P_Total": data['P4'],
        "p.f._Total": data['tpf4'],
    }


if __name__ == "__main__":
    print(get_power())
