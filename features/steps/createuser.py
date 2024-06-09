from behave import *
import requests
import json

base_url = "https://reqres.in/api/"
create_user_url = base_url + "users"

headers = {'Content-Type': 'application/json'}


@given('I am on the user creation page')
def step_impl(context):
    context.session = requests.Session()  # Creating a session


@when('I submit user data with name "{name}" and job "{job}"')
def step_impl(context, name, job):
    payload = json.dumps({"name": name, "job": job})
    try:
        response = context.session.post(create_user_url, data=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        context.response = None
        context.response_data = {}
        assert False, f"User creation failed with status code: {e.response.status_code}, Error: {e.response.text}"
    else:
        context.response = response
        context.response_data = response.json()


@then('The user is created successfully')
def step_impl(context):
    assert context.response is not None, "No response received"
    assert context.response.status_code == 201, f"Unexpected status code: {context.response.status_code}, Error: {context.response.text}"
    assert 'id' in context.response_data, f"ID not found in response: {context.response_data}"
    assert 'name' in context.response_data, f"Name not found in response: {context.response_data}"
    assert 'job' in context.response_data, f"Job not found in response: {context.response_data}"
    assert 'createdAt' in context.response_data, f"Creation timestamp not found in response: {context.response_data}"
    context.user_id = context.response_data['id']
    context.name = context.response_data['name']
    context.job = context.response_data['job']


@then('I display the user ID, name, and job')
def step_impl(context):
    # Output ID, name, and job for debugging purposes, be cautious with sensitive data in production
    print(f"ID: {context.user_id}")
    print(f"Name: {context.name}")
    print(f"Job: {context.job}")
