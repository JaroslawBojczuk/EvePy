import requests
import base64

from app.libs.shared_flow import *


def main():
    """ Takes you through a local example of the OAuth 2.0 web flow."""

    client_id = "25de483df3304d9ca17b5adb5d16946a"

    print_auth_url(client_id)

    auth_code = input("Copy the \"code\" query parameter and enter it here: ")
    app_secret = "M3mdEGcoBEfr1SH9ElIeAJbW8lV7pZqfSqDVIJ4A"

    user_pass = "{}:{}".format(client_id, app_secret)
    basic_auth = base64.urlsafe_b64encode(user_pass.encode('utf-8')).decode()
    auth_header = "Basic {}".format(basic_auth)

    form_values = {
        "grant_type": "authorization_code",
        "code": auth_code,
    }

    headers = {"Authorization": auth_header}

    res = send_token_request(form_values, add_headers=headers)
    access_token = res.json()["access_token"]

    jwt = validate_eve_jwt(access_token)
    character_id = jwt["sub"].split(":")[2]
    
    print("Access token: " + access_token)
    print("Character ID: " + character_id)

    access_token_file = open("access_token.txt", "w")
    access_token_file.write(access_token)
    access_token_file.close()

    character_id_file = open("character_id.txt", "w")
    character_id_file.write(character_id)
    character_id_file.close()


if __name__ == "__main__":
    main()
