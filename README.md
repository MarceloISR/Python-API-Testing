
# SETUP

From the root directory execute

### Save requirements
```bash
  python -m pip freeze > requirements.txt
```

### Install requirements
```bash
  python -m pip install -r requirements.txt
```


### CONFIGURE SO ENVIRONMENT VARIABLES

| VARIABLE     | VALUE     |
| :--------    | :-------  | 
| `API_KEY`    | ABC123    |
| `API_SECRET` | DEF456    |
| `API_URL`    | URL123    |


# RUN TESTS

## Run all the tests within the test folder
```bash
  pytest tests
```

## Run tests by marker
```bash
  pytest tests\test.py -m pagination
```

## Run tests by markers
```bash
  pytest tests\test.py -m "pagination or authorization"
```

## Run an specific test file
```bash
  pytest tests\test.py
```

## Generate Reporter
To run tests, generating a report, run the following command

```bash
  pytest tests\test.py --template=html1/index.html --report=report.html
```
