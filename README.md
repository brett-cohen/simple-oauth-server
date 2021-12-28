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

To start all three apps, simply run `docker-compose up` in the base directory.