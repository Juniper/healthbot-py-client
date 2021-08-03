class BaseModule(object):
    def __init__(self, hbot, url=None):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        :param str url: either hb.url or hb.config_url. default is hb.url
        """

        self.hbot = hbot
        if url is None:
            self.url = hbot.url
        else:
            self.url = url

    @property
    def api(self):
        return self.hbot.hbot_session

    @property
    def api_client(self):
        return self.hbot.api_client

    @property
    def authorization(self):
        return 'x-iam-token ' + self.hbot.user_token.access_token
