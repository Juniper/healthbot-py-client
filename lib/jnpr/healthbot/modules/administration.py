from jnpr.healthbot.modules import BaseModule
from jnpr.healthbot.swagger.api.administration_api import AdministrationApi
from jnpr.healthbot.swagger.rest import ApiException
from jnpr.healthbot.swagger.models.user_schema import UserSchema
from jnpr.healthbot.swagger.models.groups import Groups
from jnpr.healthbot.swagger.models.role_schema_inner import RoleSchemaInner
from jnpr.healthbot.exception import SchemaError, NotFoundError

from jnpr.healthbot.swagger.models import user
from jnpr.healthbot.swagger.models import groups

import logging
logger = logging.getLogger(__file__)


class Administration(object):
    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        self._hbot = hbot
        self.user = User(hbot)
        self.group = Group(hbot)
        self.role = Role(hbot)


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
        if userid is not None and user_name is not None:
            raise Exception("userid & user_name are mutually exclusive")

        if user_name is not None:
            userid=self.get_userid_from_user_name(user_name)
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

    def delete(self, userid: str = None, user_name: str = None):
        """
        Remove give user id

        :param userid: ID of user
        :param user_name: Can pass user name if user id is not known

        Example:
        ::
            hb.administration.user.delete(userid ='425453652efwfer')
            hb.administration.user.delete(user_name='dummy')

        :returns: True when OK
        """
        if userid is not None and user_name is not None:
            raise Exception("userid & user_name are mutually exclusive")

        if user_name is not None:
            userid = self.get_userid_from_user_name(user_name)
        if userid is not None:
            try:
                self._admin_api.delete_user(authorization=self.authorization,
                                            userid=userid)
                return True
            except ApiException as ex:
                raise ex
        return False

    def get_userid_from_user_name(self, user_name: str):
        """
        Get user ID from given user name

        :param user_name: user name

        """
        try:
            responses = self._admin_api.retrieve_users(
                authorization=self.authorization)
        except ApiException as ex:
            raise ex
        for response in responses:
            if user_name == response.user_name:
                return response.user_id
        raise NotFoundError('Not able to find userid for given user_name: "{}"'.format(
            user_name))

    def update(self, schema: UserSchema = None, **kwargs):
        """
        Update `UserSchema <jnpr.healthbot.swagger.models.html#UserSchema>`_ for
        given UserSchema schema

        Only support `post` and not `put`

        :param obj schema: `UserSchema <jnpr.healthbot.swagger.models.html#UserSchema>`_
        :param object kwargs: key values, which can be used to create
            UserSchema
            Check `UserSchema <jnpr.healthbot.swagger.models.html#UserSchema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.administration.user.get(user_name="test")
                schemaObj.last_name = 'Kumar'
                schemaObj = hb.administration.user.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = user.User(**kwargs)
        else:
            if not isinstance(schema, UserSchema):
                raise SchemaError(UserSchema)
        userid = self.get_userid_from_user_name(schema.user_name)
        try:
            payload = self.hbot._create_payload(schema)
            self._admin_api.update_user_profile(self.authorization,
                                                userid=userid, user=payload)
        except ApiException as ex:
            raise ex
        return True


class Group(BaseModule):
    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        super().__init__(hbot)
        self._admin_api = AdministrationApi(self.api_client)

    def get(self, groupid: str = None, group_name: str = None):
        """
        Get `Groups(s) <jnpr.healthbot.swagger.models.html#Groups>`_ for
        given group id or list for all. Can also get for given group name.

        :param groupid: ID of group
        :param group_name: Can pass group name if group id is not known

        Example:
            ::
                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.administration.group.get(groupid='425453652efwfer')
                    print(hb.administration.group.get(group_name='hboperator')

        :return: `Groups(s) <jnpr.healthbot.swagger.models.html#Groups>`_
        """
        if groupid is not None and group_name is not None:
            raise Exception("groupid & group_name are mutually exclusive")

        if group_name is not None:
            groupid = self.get_groupid_from_group_name(group_name)
        if groupid is not None:
            try:
                response = self._admin_api.get_group_details(
                    authorization=self.authorization, groupid=groupid)
            except ApiException as ex:
                raise ex
            return self.hbot._create_schema(response, Groups)
        else:
            try:
                responses = self._admin_api.retrieve_groups(
                    authorization=self.authorization)
            except ApiException as ex:
                raise ex
            groups_list = []
            for response in responses:
                groups_list.append(self.hbot._create_schema(response, Groups))
            return groups_list

    def add(self, schema: Groups = None, **kwargs):
        """
        Add group to HealthBot administration

        :param object schema: `Groups <jnpr.healthbot.swagger.models.html#Groups>`_
        :param object kwargs: key values, which can be used to create
            Groups
            Check `Groups <jnpr.healthbot.swagger.models.html#Groups>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import Groups
            from jnpr.healthbot import GroupgroupidRoles
            from jnpr.healthbot import AssociatedUserSchemaInner

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                userid = hb.administration.user.get_userid_from_user_name(user_name="alpha")

                schema = Groups(group_name='test', group_description="testing HbEZ",
                                roles=[GroupgroupidRoles(role_id='fa52374b-7852-4fb1-a697-b924b642e89f',
                                                         role_name='token:write')],
                                users=[AssociatedUserSchemaInner(user_id=userid, user_name="alpha"),
                                       AssociatedUserSchemaInner(user_id=
                                       hb.administration.user.get_userid_from_user_name(
                                           user_name="mc"), user_name="mc")])
                print(hb.administration.group.add(schema))

        :returns: True when OK

        """
        if schema is None:
            schema = Groups(**kwargs)
        if not isinstance(schema, list):
            schema = [schema]
        payload = [self.hbot._create_payload(item) for item in schema]
        try:
            self._admin_api.create_groups(authorization=self.authorization,
                                         groups=payload)
        except ApiException as ex:
            raise ex
        return True

    def delete(self, groupid: str = None, group_name: str = None):
        """
        Remove give group id

        :param groupid: ID of group
        :param group_name: Can pass group name if group id is not known

        Example:
        ::
            hb.administration.group.delete(groupid ='425453652efwfer')
            hb.administration.group.delete(group_name='test')

        :returns: True when OK
        """
        if groupid is not None and group_name is not None:
            raise Exception("groupid & group_name are mutually exclusive")

        if group_name is not None:
            groupid = self.get_groupid_from_group_name(group_name)
        if groupid is not None:
            try:
                self._admin_api.delete_group(authorization=self.authorization,
                                            groupid=groupid)
                return True
            except ApiException as ex:
                raise ex
        return False

    def get_groupid_from_group_name(self, group_name: str):
        """
        Get Group ID from given group name

        :param group_name: group name

        """
        try:
            responses = self._admin_api.retrieve_groups(
                authorization=self.authorization)
        except ApiException as ex:
            raise ex
        for response in responses:
            if group_name == response.group_name:
                return response.group_id
        raise NotFoundError('Not able to find groupid for given group_name: "{}"'.format(
            group_name))

    def update(self, schema: Groups = None, **kwargs):
        """
        Update `Groups <jnpr.healthbot.swagger.models.html#Groups>`_ for
        given Groups schema

        Only support `post` and not `put`

        :param obj schema: `Groups <jnpr.healthbot.swagger.models.html#Groups>`_
        :param object kwargs: key values, which can be used to create
            Groups
            Check `Groups <jnpr.healthbot.swagger.models.html#Groups>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schema = hb.administration.group.get(group_name="test")
                schema.users.append(AssociatedUserSchemaInner(user_id=
                                       hb.administration.user.get_userid_from_user_name(
                                           user_name="mc"), user_name="mc"))
                print(hb.administration.group.update(schema=schema))

        :returns: True when OK
        """
        if schema is None:
            schema = groups.Groups(**kwargs)
        else:
            if not isinstance(schema, Groups):
                raise SchemaError(Groups)
        groupid = self.get_groupid_from_group_name(schema.group_name)
        try:
            payload = self.hbot._create_payload(schema)
            self._admin_api.update_group(self.authorization,
                                                groupid=groupid, group=payload)
        except ApiException as ex:
            raise ex
        return True


class Role(BaseModule):
    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        super().__init__(hbot)
        self._admin_api = AdministrationApi(self.api_client)

    def get(self, role_id: str = None, role_name: str = None):
        """
        Get `RoleSchemaInner(s) <jnpr.healthbot.swagger.models.html#RoleSchemaInner>`_ for
        given role id or list for all. Can also get for given role name.

        :param role_id: ID of role
        :param role_name: Can pass role name if role id is not known

        Example:
            ::
                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    # to get all roles data
                    hb.administration.role.get()

                    # to get individual role
                    print(hb.administration.role.get(role_id='425453652efwfer')
                    print(hb.administration.role.get(role_name="token:write")

        :return: `RoleSchemaInner(s) <jnpr.healthbot.swagger.models.html#RoleSchemaInner>`_
        """
        if role_id is not None and role_name is not None:
            raise Exception("role_id & role_name are mutually exclusive")

        try:
            responses = self._admin_api.retrieve_roles(
                authorization=self.authorization)
        except ApiException as ex:
            raise ex
        roles_list = []
        for response in responses:
            role = self.hbot._create_schema(response, RoleSchemaInner)
            if role_id and response.get('roleId') == role_id:
                return role
            if role_name and response.get('roleName') == role_name:
                return role
            roles_list.append(role)
        return roles_list
