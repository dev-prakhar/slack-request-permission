from rest_framework import permissions

from slack_request_validator.utils import verify_slack_request


class AbstractIsSlackAppRequest(permissions.BasePermission):
    """
    Abstract Class to be inherited if a new permission needs to be created for slack app request verification
    """

    class Meta:
        abstract = True

    MANDATORY_HEADERS = ('X-Slack-Request-Timestamp', 'X-Slack-Signature')
    SLACK_APP_VERSION = None
    SLACK_APP_SIGNING_SECRET = None

    def has_permission(self, request, view):
        if not all(header in request.headers for header in self.MANDATORY_HEADERS):
            return False

        return verify_slack_request(
            request=request,
            slack_app_version=self.SLACK_APP_VERSION,
            slack_app_signing_secret=self.SLACK_APP_SIGNING_SECRET
        )
