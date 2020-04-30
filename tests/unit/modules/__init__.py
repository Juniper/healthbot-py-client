from jnpr.healthbot.swagger.models.inline_response2006 import InlineResponse2006


def _mock_user_login():
    return InlineResponse2006(access_token='xxxx', refresh_token='yyyy',
                              first_login=None, refresh_token_expires=1,
                              token_expires=1)