from jnpr.healthbot.swagger.models import *
from jnpr.healthbot.exception import SchemaError, NotFoundError
from jnpr.healthbot.modules.playbooks import PlayBookInstanceBuilder

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def _addMethod(verb, dict):
    """Make a get or add method and add it to dict."""
    if verb == 'add':
        fields = dict.pop('_add')
        dict[verb] = _makeAdd(fields)
    if verb == 'get':
        fields = dict.pop('_get')
        dict[verb] = _makeGet(fields)


def _makeAdd(fields):
    """Return a method that can be used to add Schema."""
    schemaClass = fields.get("schema")
    logger = fields.get("logger")
    urlfor = fields.get("url_for")
    payload_key = fields.get("payload_key")

    def add(self, schema, **kwargs):
        if schema is None:
            schema = schemaClass(**kwargs)
        else:
            if not isinstance(schema, schemaClass):
                raise SchemaError(schemaClass)
        payload = self.hbot._create_payload(schema)
        url = self.hbot.urlfor.__getattribute__(urlfor)(
            payload[payload_key])
        response = self.api.post(url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True
    return add


def _makeGet(fields):
    """Return a method that can be used to add Schema."""
    schemaClass = fields.get("schema")
    logger = fields.get("logger")
    urlfor = fields.get("url_for")
    payload_key = fields.get("payload_key")
    uncommitted = fields.get("uncommitted", True)
    return_response_json = fields.get("return_response_json", False)

    def get(self, name: str = None, uncommitted: bool = uncommitted):
        if name is not None:
            url = self.hbot.urlfor.__getattribute__(urlfor)(
                name)
            if uncommitted:
                url += self.hbot.apiopt_candidate
            response = self.api.get(url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(response, schemaClass)
        else:
            url = self.hbot.urlfor.__getattribute__(urlfor)()
            if uncommitted:
                url += self.hbot.apiopt_candidate
            response = self.api.get(url)
            if response.status_code == 404:
                return []
            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            response.raise_for_status()
            return_list = []
            if return_response_json:
                return response_json
            items = response_json[payload_key]
            for item in items:
                obj = self.hbot._create_schema(
                    item, schemaClass)
                return_list.append(obj)
            return return_list
    return get


class AutoGenClass(type):
    """Adds add/get methods to the class."""

    def __new__(cls, name, bases, dict):
        if '_add' in dict:
            _addMethod('add', dict)
        if '_get' in dict:
            _addMethod('get', dict)
        return type.__new__(cls, name, bases, dict)

from jnpr.healthbot.healthbot import HealthBotClient
