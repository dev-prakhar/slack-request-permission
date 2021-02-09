from django.conf import settings

from slack_request_validator.abstract_permission import AbstractIsSlackAppRequest


class IsSlackAppRequest(AbstractIsSlackAppRequest):
    """
    Permission class to verify if the incoming request is coming from slack
    """
    SLACK_APP_VERSION = getattr(settings, 'SLACK_VERSION', 'v0')
    SLACK_APP_SIGNING_SECRET = getattr(settings, 'SLACK_APP_SIGNING_SECRET', '')
