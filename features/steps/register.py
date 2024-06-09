from behave import *
import requests
import json

base_url = "https://reqres.in/api/"
register_url = base_url + "register"

headers = {'Content-Type': 'application/json'}


@given('I am on the registration page')
def step_impl(context):
    context.session = requests.Session()  # Creating a session


@when('I submit registration data with email "{email}" and password "{password}"')
def step_impl(context, email, password):
    payload = json.dumps({"email": email, "password": password})
    try:
        response = context.session.post(register_url, data=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        context.response = None
        context.response_data = {}
        assert False, f"Registration failed with status code: {e.response.status_code}, Error: {e.response.text}"
    else:
        context.response = response
        context.response_data = response.json()


@then('I am registered successfully')
def step_impl(context):
    assert context.response is not None, "No response received"
    assert context.response.status_code == 200, f"Unexpected status code: {context.response.status_code}, Error: {context.response.text}"
    assert 'id' in context.response_data, f"ID not found in response: {context.response_data}"
    assert 'token' in context.response_data, f"Token not found in response: {context.response_data}"
    context.id = context.response_data['id']
    context.token = context.response_data['token']


@then('I display the user ID and token')
def step_impl(context):
    # Output ID and token for debugging purposes, be cautious with sensitive data in production
    print(f"ID: {context.id}")
    print(f"Token: {context.token}")
