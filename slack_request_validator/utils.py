import hashlib
import hmac


def generate_hmac(secret, base_string):
    """
    Helper method that returns an hmac from secret and base_string
    :param secret:
    :param base_string:
    :return:
    """
    if isinstance(secret, str):
        secret = secret.encode('UTF-8')

    if isinstance(base_string, str):
        base_string = base_string.encode('UTF-8')

    return hmac.new(secret, base_string, hashlib.sha256).hexdigest()


def verify_slack_request(request, slack_app_version, slack_app_signing_secret):
    """
    Helper method that verifies if the incoming request is from slack or not
    :param request:
    :param slack_app_version:
    :param slack_app_signing_secret:
    :return:
    """
    timestamp = request.headers['X-Slack-Request-Timestamp']
    body = request.body.decode('UTF-8')  # converting bytes to string
    base_string = f"{slack_app_version}:{timestamp}:{body}"

    generated_sign = f"{slack_app_version}={generate_hmac(slack_app_signing_secret, base_string)}"
    slack_sign = request.headers['X-Slack-Signature']

    return hmac.compare_digest(generated_sign, slack_sign)
