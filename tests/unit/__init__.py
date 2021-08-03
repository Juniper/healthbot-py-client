from jnpr.healthbot.swagger.models.inline_response2002 import InlineResponse2002


def _mock_user_login():
    return InlineResponse2002(access_token='xxxx', refresh_token='yyyy',
                              refresh_token_expires=1, token_expires=1)
