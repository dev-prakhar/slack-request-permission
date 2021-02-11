## Slack Request Permission

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Django](https://img.shields.io/badge/Django-3.1.6-green.svg)](https://shields.io/)

### Installation
* Compatibility
```
Python Version > 3.5
Django Version > 2.0
```
* Install using
```bash
pip install slack-request-permission
```

### Introduction

Every slack app that needs to interact with any server needs to be verified (verify if the sender is actually slack).

This package offers you:

* [Out-of-the-box `Django` permission class that can be used to authenticate slack requests](#out-of-the-box)
* [Framework for creating your own permission class for any slack app](#framework)
* [A standalone method to verify slack request](#standalone-method)

### Out-of-the-box

To use out of the box permission class, all you have to do is add the class into permission classes of
[Django Rest Framework](https://www.django-rest-framework.org/tutorial/3-class-based-views/).

```python
class RandomSlackRequestView(APIView):
    permission_classes = (IsSlackAppRequest,)
```

`In settings.py`

```python
SLACK_APP_VERSION = 'v0'
SLACK_APP_SIGNING_SECRET = {YOUR_SLACK_APP_SIGNING_SECRET}
```

The view will verify that the incoming request is from slack before running anything.

### Framework

There might come a use case where you have different slack apps with different `signing_secrets` interacting with your
backend. In that case, you can create your own custom permission class

```python
from slack_request_validator.abstract_permission import AbstractIsSlackAppRequest

class MySlackApp1Permission(AbstractIsSlackAppRequest):
    SLACK_APP_VERSION = 'v0'
    SLACK_APP_SIGNING_SECRET = {MySlackApp1_SIGNING_SECRET}


class MySlackApp2Permission(AbstractIsSlackAppRequest):
    SLACK_APP_VERSION = 'v0'
    SLACK_APP_SIGNING_SECRET = {MySlackApp2_SIGNING_SECRET}
```

These permissions can be then used inside any Django Rest Framework's View


```python
class MySlackApp1View(APIView):
    permission_classes = (MySlackApp1Permission,)


class MySlackApp2View(APIView):
    permission_classes = (MySlackApp2Permission,)
```

### Standalone-Method
There might be cases when you don't want to use permission classes.
You can directly use the method that verifies slack request

This method `returns` either `True` or `False`
```python
True # If slack request is correct
False # If slack request is incorrect
```

```python
from slack_request_validator.utils import verify_slack_request

slack_version = 'v0'
slack_app_signing_secret = {YOUR_SLACK_APP_SIGNING_SECRET}
verify_slack_request(request=request, slack_app_version=slack_version, slack_app_signing_secret=slack_app_signing_secret)
```
***
