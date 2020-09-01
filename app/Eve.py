from app.libs.shared_flow import *


def main():
    """ Takes you through a local example of the OAuth 2.0 web flow."""

    access_token_file = open("access_token.txt", "r")
    character_id_file = open("character_id.txt", "r")

    token = access_token_file.read()
    character_id = character_id_file.read()

    headers = {
        "Authorization": "Bearer {}".format(token)
    }

    blueprint_path = ("https://esi.evetech.net/latest/characters/{}/blueprints/".format(character_id))
    res = requests.get(blueprint_path, headers=headers)
    print(res.content)


if __name__ == "__main__":
    main()
