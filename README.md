# GitHub MCP Test Repository

A deliberately small Flask application used for testing
a GitHub MCP server.

This repository contains several intentional bugs and
technical issues so that the GitHub Issues API can be tested.

## Known Problems

- Login crashes when username is missing
- Database connections are not closed
- Passwords use MD5
- Flask runs with debug mode enabled
- No rate limiting exists on login
- User profile endpoint has no authentication
