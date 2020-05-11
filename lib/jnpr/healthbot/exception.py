class SchemaError(Exception):

    """
    Generated in response to a invalid Schema type
    """

    def __init__(self, schema):
        self._schema = schema

    def __repr__(self):
        return "Schema provided is not of {} type".format(self._schema)

    __str__ = __repr__


class NotFoundError(Exception):

    """
    Generated in response to a invalid Schema type
    """

    def __init__(self, detail):
        self.detail = detail.get('detail')
        self.status = detail.get('status')

    def __repr__(self):
        return "{}, {}".format(self.status, self.detail)

    __str__ = __repr__


class ConnectAuthError(Exception):

    """
    Generated if the user-name, password is invalid
    """
    def __init__(self, hbot, msg=None):
        self.hbot = hbot
        self._orig = msg

    def __repr__(self):
        if self._orig:
            return "{}(host: {}, msg: {})".format(self.__class__.__name__,
                                                     self.hbot.server,
                                                     self._orig)
        else:
            return "{}({})".format(self.__class__.__name__,
                                     self.hbot.server)

    __str__ = __repr__
