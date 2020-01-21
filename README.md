# Members Count Service

Service returning actual Pirate party members count.

Has one endpoint `/members` returning JSON response like:

```
{"members": 1234}
```

## Contribution

### Files

`app.py` - main app
`tests.py` - tests

### Local setup

Create and activate virtual environment.

Instal requirements and test requirements:

`$ pip install -r requirements.txt`
`$ pip install -r test-requirements.txt`

Run local server:

`$ gunicorn app:api`

### Running tests

Tests are using `pytest` framework.

Run tests: `$ pytest`

### Updating requirements

Use `pip-compile` from pip tools (`$ pip install pip-tools`):

Update requirements: `$ pip-compile -U requirements.in`
Update test requirements: `$ pip-compile -U test-requirements.in`
