class BaseModule(object):
    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        self.hbot = hbot
        self.url = hbot.url

    @property
    def api(self):
        return self.hbot.hbot_session