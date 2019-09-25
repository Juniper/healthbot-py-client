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
