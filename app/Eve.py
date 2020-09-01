import requests
import base64

from app.libs.shared_flow import *


def main():
    """ Takes you through a local example of the OAuth 2.0 web flow."""

    client_id = "25de483df3304d9ca17b5adb5d16946a"

    #print_auth_url(client_id)

    #auth_code = input("Copy the \"code\" query parameter and enter it here: ")
    auth_code = "1"
    app_secret = "M3mdEGcoBEfr1SH9ElIeAJbW8lV7pZqfSqDVIJ4A"

    # Basic auth can be taken care of by the requests library by passing in
    # the kwarg "auth=(client_id, app_secret)" but it's best to show how it's
    # done without it for this example.
    user_pass = "{}:{}".format(client_id, app_secret)
    basic_auth = base64.urlsafe_b64encode(user_pass.encode('utf-8')).decode()
    auth_header = "Basic {}".format(basic_auth)

    form_values = {
        "grant_type": "authorization_code",
        "code": auth_code,
    }

    headers = {"Authorization": auth_header}

    print("\nThe following request uses basic authentication, as a web based "
          "app you should do the same.")

    #res = send_token_request(form_values, add_headers=headers)
    #data = res.json()
    #access_token = data["access_token"]
    #print(access_token)

    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IkpXVC1TaWduYXR1cmUtS2V5IiwidHlwIjoiSldUIn0.eyJzY3AiOlsiZXNpLWNoYXJhY3RlcnMucmVhZF9ibHVlcHJpbnRzLnYxIiwiZXNpLXNraWxscy5yZWFkX3NraWxscy52MSJdLCJqdGkiOiI0YjgzMTYwZi04MjA2LTRjMjQtYjJmOC1mNTZmNmFlNjUwNTAiLCJraWQiOiJKV1QtU2lnbmF0dXJlLUtleSIsInN1YiI6IkNIQVJBQ1RFUjpFVkU6MjExMjUzOTY1NyIsImF6cCI6IjI1ZGU0ODNkZjMzMDRkOWNhMTdiNWFkYjVkMTY5NDZhIiwibmFtZSI6IlZhc3RoIiwib3duZXIiOiJWNFBFcldGOEJxcG9XQmx2WXZKdWhYSTAydWc9IiwiZXhwIjoxNTk4OTc2MDA5LCJpc3MiOiJsb2dpbi5ldmVvbmxpbmUuY29tIn0.jmOp25UgRV9G88jP9yD4QugU1uxSXDvpVPB5HrI328BKfuouihYI0EnLdslxTON75ydovR7r3C0RqvTw2XaVu2qkHlwrYZfX2I7kcV0nFSDCmUNhLOmg4fNaoeMJCJvmGMPV4AmmDuZaEY5zZ6GxE_s_MswXt457W1ddtXhIzYTUoNGT1bSiXA05KjyN3cTE3PaONCR2V1_xUXi-UadqyWrziaeJRjnXHcGEw1lIWf3ILjYyWk1KlnRBGwjeP3zG7SYHigKU_FER21Y_pVFDyUujDcoOqaHnwz8puXSAtfiVfazQh5Q5ddRjSuoO4rWpCoIkoUiLfVVJ7Wvnfo-P7g"
    #token = access_token

    headers = {
        "Authorization": "Bearer {}".format(token)
    }

    blueprint_path = ("https://esi.evetech.net/latest/characters/{}/blueprints/".format(2112539657))
    res = requests.get(blueprint_path, headers=headers)
    print(res.content)


if __name__ == "__main__":
    main()
