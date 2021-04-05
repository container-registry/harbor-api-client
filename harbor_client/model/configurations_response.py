"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from harbor_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from harbor_client.model.bool_config_item import BoolConfigItem
    from harbor_client.model.configurations_response_scan_all_policy import ConfigurationsResponseScanAllPolicy
    from harbor_client.model.integer_config_item import IntegerConfigItem
    from harbor_client.model.string_config_item import StringConfigItem
    globals()['BoolConfigItem'] = BoolConfigItem
    globals()['ConfigurationsResponseScanAllPolicy'] = ConfigurationsResponseScanAllPolicy
    globals()['IntegerConfigItem'] = IntegerConfigItem
    globals()['StringConfigItem'] = StringConfigItem


class ConfigurationsResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'oidc_verify_cert': (BoolConfigItem,),  # noqa: E501
            'email_identity': (StringConfigItem,),  # noqa: E501
            'ldap_group_search_filter': (StringConfigItem,),  # noqa: E501
            'auth_mode': (StringConfigItem,),  # noqa: E501
            'self_registration': (BoolConfigItem,),  # noqa: E501
            'oidc_scope': (StringConfigItem,),  # noqa: E501
            'ldap_search_dn': (str,),  # noqa: E501
            'storage_per_project': (IntegerConfigItem,),  # noqa: E501
            'scan_all_policy': (ConfigurationsResponseScanAllPolicy,),  # noqa: E501
            'verify_remote_cert': (BoolConfigItem,),  # noqa: E501
            'ldap_timeout': (IntegerConfigItem,),  # noqa: E501
            'ldap_base_dn': (StringConfigItem,),  # noqa: E501
            'ldap_filter': (StringConfigItem,),  # noqa: E501
            'read_only': (BoolConfigItem,),  # noqa: E501
            'quota_per_project_enable': (BoolConfigItem,),  # noqa: E501
            'ldap_url': (StringConfigItem,),  # noqa: E501
            'oidc_name': (StringConfigItem,),  # noqa: E501
            'project_creation_restriction': (StringConfigItem,),  # noqa: E501
            'ldap_uid': (StringConfigItem,),  # noqa: E501
            'oidc_client_id': (StringConfigItem,),  # noqa: E501
            'ldap_group_base_dn': (StringConfigItem,),  # noqa: E501
            'ldap_group_attribute_name': (StringConfigItem,),  # noqa: E501
            'email_insecure': (BoolConfigItem,),  # noqa: E501
            'ldap_group_admin_dn': (StringConfigItem,),  # noqa: E501
            'email_username': (StringConfigItem,),  # noqa: E501
            'oidc_endpoint': (StringConfigItem,),  # noqa: E501
            'ldap_scope': (int,),  # noqa: E501
            'count_per_project': (IntegerConfigItem,),  # noqa: E501
            'token_expiration': (IntegerConfigItem,),  # noqa: E501
            'ldap_group_search_scope': (IntegerConfigItem,),  # noqa: E501
            'email_ssl': (BoolConfigItem,),  # noqa: E501
            'email_port': (IntegerConfigItem,),  # noqa: E501
            'email_host': (StringConfigItem,),  # noqa: E501
            'email_from': (StringConfigItem,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'oidc_verify_cert': 'oidc_verify_cert',  # noqa: E501
        'email_identity': 'email_identity',  # noqa: E501
        'ldap_group_search_filter': 'ldap_group_search_filter',  # noqa: E501
        'auth_mode': 'auth_mode',  # noqa: E501
        'self_registration': 'self_registration',  # noqa: E501
        'oidc_scope': 'oidc_scope',  # noqa: E501
        'ldap_search_dn': 'ldap_search_dn',  # noqa: E501
        'storage_per_project': 'storage_per_project',  # noqa: E501
        'scan_all_policy': 'scan_all_policy',  # noqa: E501
        'verify_remote_cert': 'verify_remote_cert',  # noqa: E501
        'ldap_timeout': 'ldap_timeout',  # noqa: E501
        'ldap_base_dn': 'ldap_base_dn',  # noqa: E501
        'ldap_filter': 'ldap_filter',  # noqa: E501
        'read_only': 'read_only',  # noqa: E501
        'quota_per_project_enable': 'quota_per_project_enable',  # noqa: E501
        'ldap_url': 'ldap_url',  # noqa: E501
        'oidc_name': 'oidc_name',  # noqa: E501
        'project_creation_restriction': 'project_creation_restriction',  # noqa: E501
        'ldap_uid': 'ldap_uid',  # noqa: E501
        'oidc_client_id': 'oidc_client_id',  # noqa: E501
        'ldap_group_base_dn': 'ldap_group_base_dn',  # noqa: E501
        'ldap_group_attribute_name': 'ldap_group_attribute_name',  # noqa: E501
        'email_insecure': 'email_insecure',  # noqa: E501
        'ldap_group_admin_dn': 'ldap_group_admin_dn',  # noqa: E501
        'email_username': 'email_username',  # noqa: E501
        'oidc_endpoint': 'oidc_endpoint',  # noqa: E501
        'ldap_scope': 'ldap_scope',  # noqa: E501
        'count_per_project': 'count_per_project',  # noqa: E501
        'token_expiration': 'token_expiration',  # noqa: E501
        'ldap_group_search_scope': 'ldap_group_search_scope',  # noqa: E501
        'email_ssl': 'email_ssl',  # noqa: E501
        'email_port': 'email_port',  # noqa: E501
        'email_host': 'email_host',  # noqa: E501
        'email_from': 'email_from',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ConfigurationsResponse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            oidc_verify_cert (BoolConfigItem): [optional]  # noqa: E501
            email_identity (StringConfigItem): [optional]  # noqa: E501
            ldap_group_search_filter (StringConfigItem): [optional]  # noqa: E501
            auth_mode (StringConfigItem): [optional]  # noqa: E501
            self_registration (BoolConfigItem): [optional]  # noqa: E501
            oidc_scope (StringConfigItem): [optional]  # noqa: E501
            ldap_search_dn (str): The DN of the user to do the search.. [optional]  # noqa: E501
            storage_per_project (IntegerConfigItem): [optional]  # noqa: E501
            scan_all_policy (ConfigurationsResponseScanAllPolicy): [optional]  # noqa: E501
            verify_remote_cert (BoolConfigItem): [optional]  # noqa: E501
            ldap_timeout (IntegerConfigItem): [optional]  # noqa: E501
            ldap_base_dn (StringConfigItem): [optional]  # noqa: E501
            ldap_filter (StringConfigItem): [optional]  # noqa: E501
            read_only (BoolConfigItem): [optional]  # noqa: E501
            quota_per_project_enable (BoolConfigItem): [optional]  # noqa: E501
            ldap_url (StringConfigItem): [optional]  # noqa: E501
            oidc_name (StringConfigItem): [optional]  # noqa: E501
            project_creation_restriction (StringConfigItem): [optional]  # noqa: E501
            ldap_uid (StringConfigItem): [optional]  # noqa: E501
            oidc_client_id (StringConfigItem): [optional]  # noqa: E501
            ldap_group_base_dn (StringConfigItem): [optional]  # noqa: E501
            ldap_group_attribute_name (StringConfigItem): [optional]  # noqa: E501
            email_insecure (BoolConfigItem): [optional]  # noqa: E501
            ldap_group_admin_dn (StringConfigItem): [optional]  # noqa: E501
            email_username (StringConfigItem): [optional]  # noqa: E501
            oidc_endpoint (StringConfigItem): [optional]  # noqa: E501
            ldap_scope (int): 0-LDAP_SCOPE_BASE, 1-LDAP_SCOPE_ONELEVEL, 2-LDAP_SCOPE_SUBTREE. [optional]  # noqa: E501
            count_per_project (IntegerConfigItem): [optional]  # noqa: E501
            token_expiration (IntegerConfigItem): [optional]  # noqa: E501
            ldap_group_search_scope (IntegerConfigItem): [optional]  # noqa: E501
            email_ssl (BoolConfigItem): [optional]  # noqa: E501
            email_port (IntegerConfigItem): [optional]  # noqa: E501
            email_host (StringConfigItem): [optional]  # noqa: E501
            email_from (StringConfigItem): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)