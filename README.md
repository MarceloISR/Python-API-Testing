
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

| VARIABLE     | VALUE        |
| :--------    | :-------     | 
| `API_KEY`    | key value    |
| `API_SECRET` | secret value |
| `API_URL`    | url value    |


# RUN TESTS

## Run an specific file
```bash
  pytest tests\test.py
```

## Generate Reporter
To run tests, generating a report, run the following command

```bash
  pytest tests\test.py --template=html1/index.html --report=report.html
```
