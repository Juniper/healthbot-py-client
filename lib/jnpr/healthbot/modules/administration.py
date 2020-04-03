from jnpr.healthbot.modules import BaseModule
from jnpr.healthbot.swagger.api.administration_api import AdministrationApi
from jnpr.healthbot.swagger.rest import ApiException
from jnpr.healthbot.swagger.models.user_schema import UserSchema

import logging
logger = logging.getLogger(__file__)


class Administration(object):
    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        self._hbot = hbot
        self.user = User(hbot)
        # self.group = Group(hbot)
        # self.role = Role(hbot)


class User(BaseModule):
    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        super().__init__(hbot)
        self._admin_api = AdministrationApi(self.api_client)

    def get(self, userid: str = None, user_name: str = None):
        """
        Get `UserSchema(s) <jnpr.healthbot.swagger.models.html#UserSchema>`_ for
        given user id or list for all. Can also get for given user name.

        :param userid: ID of user
        :param user_name: Can pass user name if user id is not known

        Example:
            ::
                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.administration.user.get('425453652efwfer')

        :return: `UserSchema(s) <jnpr.healthbot.swagger.models.html#UserSchema>`_
        """
        if user_name is not None:
            try:
                responses = self._admin_api.retrieve_users(
                    authorization=self.authorization)
            except ApiException as ex:
                raise ex
            for response in responses:
                if user_name == response.user_name:
                    return self.hbot._create_schema(response, UserSchema)
            return False
        if userid is not None:
            try:
                response = self._admin_api.get_user_details(
                    authorization=self.authorization, userid=userid)
            except ApiException as ex:
                raise ex
            return self.hbot._create_schema(response, UserSchema)
        else:
            try:
                responses = self._admin_api.retrieve_users(
                    authorization=self.authorization)
            except ApiException as ex:
                raise ex
            users_list = []
            for response in responses:
                users_list.append(self.hbot._create_schema(response, UserSchema))
            return users_list

    def add(self, schema: UserSchema = None, **kwargs):
        """
        Add user to HealthBot administration

        :param object schema: `UserSchema <jnpr.healthbot.swagger.models.html#UserSchema>`_
        :param object kwargs: key values, which can be used to create
            UserSchema
            Check `UserSchema <jnpr.healthbot.swagger.models.html#notificationschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import UserSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                user = UserSchema(user_name="test", first_name="xyz", last_name="kr",
                        password="xxxx", email="xyz.kr@gmail.com", active=True,
                        groups=[UserSchemaGroups(group_id="xx-bc26bc4419d2",
                        group_name="hboperator")])
                hb.administration.user.add(user)

        :returns: True when OK

        """
        if schema is None:
            schema = UserSchema(**kwargs)
        if not isinstance(schema, list):
            schema = [schema]
        payload = [self.hbot._create_payload(item) for item in schema]
        try:
            self._admin_api.create_users(authorization=self.authorization,
                                         users=payload)
        except ApiException as ex:
            raise ex
        return True

    def delete(self, userid: str):
        """
        Remove give user id

        :param userid: ID of user

        Example:
        ::
            hb.administration.user.delete('425453652efwfer')

        :returns: True when OK
        """

        try:
            self._admin_api.delete_user(authorization=self.authorization,
                                        userid=userid)
        except ApiException as ex:
            raise ex
        return True
    #
    # def update(self, schema: NotificationSchema = None, **kwargs):
    #     """
    #     Update `NotificationSchema <jnpr.healthbot.swagger.models.html#notificationschema>`_ for
    #     given NotificationSchema schema
    #
    #     Passing Schema invoke `put` and kwargs `post`
    #
    #     :param obj schema: `NotificationSchema <jnpr.healthbot.swagger.models.html#notificationschema>`_
    #     :param object kwargs: key values, which can be used to create
    #         RetentionPolicySchema
    #         Check `NotificationSchema <jnpr.healthbot.swagger.models.html#notificationschema>`_
    #         for details about which all keys can be used
    #
    #     Example:
    #     ::
    #
    #         from jnpr.healthbot import HealthBotClient
    #         with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
    #             schemaObj = hb.settings.notification.get('xyz')
    #             schemaObj.description = 'changed description'
    #             hb.settings.notification.update(schemaObj)
    #
    #     :returns: True when OK
    #     """
    #     if schema is None:
    #         schema = NotificationSchema(**kwargs)
    #         call = self.api.post
    #     else:
    #         if not isinstance(schema, NotificationSchema):
    #             raise SchemaError(NotificationSchema)
    #         call = self.api.put
    #     payload = self.hbot._create_payload(schema)
    #     name = schema.notification_name
    #     notification_url = self.hbot.urlfor.notification(name)
    #     response = call(notification_url, json=payload)
    #     if response.status_code != 200:
    #         logger.error(response.text)
    #     response.raise_for_status()
    #     return True
    #
