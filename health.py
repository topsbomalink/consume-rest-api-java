import requests

try:
    app_status = requests.get("http://"+ env.EC2_IP + "/api/test/all")
#     app_status = requests.get("http://localhost:8000/api/test/all")

    if app_status.status_code == 200:
        print("App is up and running. API calls can be made.")
    else:
        print("Something went wrong. App not reachable")

except ConnectionError:
    print("Something went wrong. We could")
