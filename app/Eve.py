from app.libs.shared_flow import *


def _get_type_id(type_id):
    return requests.get(f"https://esi.evetech.net/latest/universe/types/{type_id}/").json()


def main():
    """ Takes you through a local example of the OAuth 2.0 web flow."""

    access_token_file = open("access_token.txt", "r")
    character_id_file = open("character_id.txt", "r")

    token = access_token_file.read()
    character_id = character_id_file.read()

    headers = {
        "Authorization": "Bearer {}".format(token)
    }

    blueprint_path = ("https://esi.evetech.net/latest/characters/{}/assets/".format(character_id))
    res = requests.get(blueprint_path, headers=headers)
    json = res.json()
    for item in json:
        if item['location_flag'] == "Cargo":
            print("CARGO: " + _get_type_id(item['type_id'])['name'])
        else:
            print(item)


if __name__ == "__main__":
    main()
