# Purpose

This project will be a simple implementation of Oauth between a client, authorization server, and protected API.
The goal is to gain a better understanding of how Oauth works via a concrete example. 

## Goals

- An authentication server that
  - Asks the user for consent regarding permissions for using the protected API
  - Provides the client with an access token
- A client application that
  - Redirects the user to the auth server
  - Sends an authorization grant to the auth serve 
  - Uses the access token to make a request to the protected API
- A protected API that
  - Rejects requests without a proper access token
  - Accepts requests with a proper access token
  - Handles user scopes as part of that token

## Anti-goals

- A robust frontend
  - The UI should be simple with only a few buttons/fields.
- A robust Docker environment
  - My plan for initial implementation is to have the three apps running in Docker containers. 
    While I'm sure I'll learn some useful things here, it shouldn't be my focus for this project.
- A non-trivial API
  - Again the focus should be on Oauth. Making an API that does more than some trivial functionality would run counter to that focus.

## Stretch Goals

- Authenticate with a third party service using Oauth
- User account authentication with OpenID

# Running
You will need:
 - Docker >= 20.10.11
 - Docker Compose >= 1.29.2

To start all three apps, simply run `docker-compose up` in the base directory.

Since this is using an in memory database, we will need to manually set up a few things.
1. Get a terminal into the auth server docker container. Run `docker ps`. Then run `docker exec -it <CONTAINER_ID> bash` where CONTAINER_ID is the ID of the auth server container.
2. In `auth/auth` run `python manage.py migrate`
3. Run `python manage.py createsuperuser`
4. Use the user you just created to log into the Django admin page (default localhost:800/admin)
5. Navigate to localhost:8000/applications and register the client (default localhost:8002)

# Using this Demo

I used some of the `django-oauth-toolkit` provided tools to help reduce time spent on things such as developing an interface.

0. Navigate to `http://localhost:8001/protected_api/random` and verify you get a 403
1. Navigate to http://django-oauth-toolkit.herokuapp.com/consumer/. Enter the client ID from the Running section of this README and the auth url (default `http://localhost:8000/oauth/authorize`)
2. Follow the redirect URL
3. Click `authorize` and copy the token received
4. Navigate to http://django-oauth-toolkit.herokuapp.com/consumer/client/. Enter the API url (default `http://localhost:8001/protected_api/random`) and the token from the previous step. Click GET and verify that you are able to access the API with the token.
