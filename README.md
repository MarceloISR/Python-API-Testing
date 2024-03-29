
# SETUP

From the root directory execute
### Install requirements
```bash
  python -m pip install -r requirements.txt
```


### Save requirements
if some changes are made, new libraries were installed, then run the command
```bash
  python -m pip freeze > requirements.txt
```




### CONFIGURE OS ENVIRONMENT VARIABLES
In order to run the tests suite 3 environment variables must be set
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
