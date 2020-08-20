# TCGPlayer

[![Generic badge](https://img.shields.io/badge/Python-3.7-COLOR.svg)](https://shields.io/)

**TCGPlayer** is a Python library to interact with the TCGPlayer (Trading Card Game Player) API.

## Installation

`tcgplayer` requires at least Python 3.7, because it  uses f-strings (a lot).

1. Fork and clone the project repo: `git clone https://github.com/rsfxiii/TCGPlayer`
2. Add `PUB_KEY`, `PRIV_KEY`, `API_VERSION`, and `APP_ID` values to the `.env` file provided in the repo.
3. Run tests to make sure the setup works and credentials can be located: `python -m unittest`

## Usage

```python
# Import the resource endpoint you want to use
from api.endpoints import Category

# Refresh your access token for the session
access_token = Client.refresh_access_token()

# Make an API call to TCGPlayer
all_categories = Client.handle_request('GET', Category.list(), {}, access_token)

# Make a call with path params
specific_category = Client.handle_request('get', Category.get_details(1), {}, access_token)

# Make a call with both path and query params
category_groups = Client.handle_request('get', Category.get_groups(1), {'limit': 10}, access_token)
```

> NOTE: Endpoint methods, like `Category.get_details` will accept *path* params, while `Client.handle_request` will accept *query* params.

## Project Goals

0. Write a maintainable, clean, and tested Python library:
    * Adhere to [PEP8 Style Guide for Python](https://www.python.org/dev/peps/pep-0008/)
    * Pair features with reasonable, effective unit tests
    * Lint, document, and distribute the package

1. Retrieve data from the [TCGPlayer API](https://docs.tcgplayer.com/docs):
    * Implement Class-based representation of the TCG Player API structure
      * Top-Level Endpoints: **App**, **Catalog**, **Inventory**, **Prices**

