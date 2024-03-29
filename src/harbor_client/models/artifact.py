# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from harbor_client.configuration import Configuration


class Artifact(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "id": "int",
        "type": "str",
        "media_type": "str",
        "manifest_media_type": "str",
        "project_id": "int",
        "repository_id": "int",
        "digest": "str",
        "size": "int",
        "icon": "str",
        "push_time": "datetime",
        "pull_time": "datetime",
        "extra_attrs": "ExtraAttrs",
        "annotations": "Annotations",
        "references": "list[Reference]",
        "tags": "list[Tag]",
        "addition_links": "AdditionLinks",
        "labels": "list[Label]",
        "scan_overview": "ScanOverview",
        "accessories": "list[Accessory]",
    }

    attribute_map = {
        "id": "id",
        "type": "type",
        "media_type": "media_type",
        "manifest_media_type": "manifest_media_type",
        "project_id": "project_id",
        "repository_id": "repository_id",
        "digest": "digest",
        "size": "size",
        "icon": "icon",
        "push_time": "push_time",
        "pull_time": "pull_time",
        "extra_attrs": "extra_attrs",
        "annotations": "annotations",
        "references": "references",
        "tags": "tags",
        "addition_links": "addition_links",
        "labels": "labels",
        "scan_overview": "scan_overview",
        "accessories": "accessories",
    }

    def __init__(
        self,
        id=None,
        type=None,
        media_type=None,
        manifest_media_type=None,
        project_id=None,
        repository_id=None,
        digest=None,
        size=None,
        icon=None,
        push_time=None,
        pull_time=None,
        extra_attrs=None,
        annotations=None,
        references=None,
        tags=None,
        addition_links=None,
        labels=None,
        scan_overview=None,
        accessories=None,
        _configuration=None,
    ):  # noqa: E501
        """Artifact - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._type = None
        self._media_type = None
        self._manifest_media_type = None
        self._project_id = None
        self._repository_id = None
        self._digest = None
        self._size = None
        self._icon = None
        self._push_time = None
        self._pull_time = None
        self._extra_attrs = None
        self._annotations = None
        self._references = None
        self._tags = None
        self._addition_links = None
        self._labels = None
        self._scan_overview = None
        self._accessories = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if media_type is not None:
            self.media_type = media_type
        if manifest_media_type is not None:
            self.manifest_media_type = manifest_media_type
        if project_id is not None:
            self.project_id = project_id
        if repository_id is not None:
            self.repository_id = repository_id
        if digest is not None:
            self.digest = digest
        if size is not None:
            self.size = size
        if icon is not None:
            self.icon = icon
        if push_time is not None:
            self.push_time = push_time
        if pull_time is not None:
            self.pull_time = pull_time
        if extra_attrs is not None:
            self.extra_attrs = extra_attrs
        if annotations is not None:
            self.annotations = annotations
        if references is not None:
            self.references = references
        if tags is not None:
            self.tags = tags
        if addition_links is not None:
            self.addition_links = addition_links
        if labels is not None:
            self.labels = labels
        if scan_overview is not None:
            self.scan_overview = scan_overview
        if accessories is not None:
            self.accessories = accessories

    @property
    def id(self):
        """Gets the id of this Artifact.  # noqa: E501

        The ID of the artifact  # noqa: E501

        :return: The id of this Artifact.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Artifact.

        The ID of the artifact  # noqa: E501

        :param id: The id of this Artifact.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Artifact.  # noqa: E501

        The type of the artifact, e.g. image, chart, etc  # noqa: E501

        :return: The type of this Artifact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Artifact.

        The type of the artifact, e.g. image, chart, etc  # noqa: E501

        :param type: The type of this Artifact.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def media_type(self):
        """Gets the media_type of this Artifact.  # noqa: E501

        The media type of the artifact  # noqa: E501

        :return: The media_type of this Artifact.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this Artifact.

        The media type of the artifact  # noqa: E501

        :param media_type: The media_type of this Artifact.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def manifest_media_type(self):
        """Gets the manifest_media_type of this Artifact.  # noqa: E501

        The manifest media type of the artifact  # noqa: E501

        :return: The manifest_media_type of this Artifact.  # noqa: E501
        :rtype: str
        """
        return self._manifest_media_type

    @manifest_media_type.setter
    def manifest_media_type(self, manifest_media_type):
        """Sets the manifest_media_type of this Artifact.

        The manifest media type of the artifact  # noqa: E501

        :param manifest_media_type: The manifest_media_type of this Artifact.  # noqa: E501
        :type: str
        """

        self._manifest_media_type = manifest_media_type

    @property
    def project_id(self):
        """Gets the project_id of this Artifact.  # noqa: E501

        The ID of the project that the artifact belongs to  # noqa: E501

        :return: The project_id of this Artifact.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Artifact.

        The ID of the project that the artifact belongs to  # noqa: E501

        :param project_id: The project_id of this Artifact.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def repository_id(self):
        """Gets the repository_id of this Artifact.  # noqa: E501

        The ID of the repository that the artifact belongs to  # noqa: E501

        :return: The repository_id of this Artifact.  # noqa: E501
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this Artifact.

        The ID of the repository that the artifact belongs to  # noqa: E501

        :param repository_id: The repository_id of this Artifact.  # noqa: E501
        :type: int
        """

        self._repository_id = repository_id

    @property
    def digest(self):
        """Gets the digest of this Artifact.  # noqa: E501

        The digest of the artifact  # noqa: E501

        :return: The digest of this Artifact.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this Artifact.

        The digest of the artifact  # noqa: E501

        :param digest: The digest of this Artifact.  # noqa: E501
        :type: str
        """

        self._digest = digest

    @property
    def size(self):
        """Gets the size of this Artifact.  # noqa: E501

        The size of the artifact  # noqa: E501

        :return: The size of this Artifact.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Artifact.

        The size of the artifact  # noqa: E501

        :param size: The size of this Artifact.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def icon(self):
        """Gets the icon of this Artifact.  # noqa: E501

        The digest of the icon  # noqa: E501

        :return: The icon of this Artifact.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Artifact.

        The digest of the icon  # noqa: E501

        :param icon: The icon of this Artifact.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def push_time(self):
        """Gets the push_time of this Artifact.  # noqa: E501

        The push time of the artifact  # noqa: E501

        :return: The push_time of this Artifact.  # noqa: E501
        :rtype: datetime
        """
        return self._push_time

    @push_time.setter
    def push_time(self, push_time):
        """Sets the push_time of this Artifact.

        The push time of the artifact  # noqa: E501

        :param push_time: The push_time of this Artifact.  # noqa: E501
        :type: datetime
        """

        self._push_time = push_time

    @property
    def pull_time(self):
        """Gets the pull_time of this Artifact.  # noqa: E501

        The latest pull time of the artifact  # noqa: E501

        :return: The pull_time of this Artifact.  # noqa: E501
        :rtype: datetime
        """
        return self._pull_time

    @pull_time.setter
    def pull_time(self, pull_time):
        """Sets the pull_time of this Artifact.

        The latest pull time of the artifact  # noqa: E501

        :param pull_time: The pull_time of this Artifact.  # noqa: E501
        :type: datetime
        """

        self._pull_time = pull_time

    @property
    def extra_attrs(self):
        """Gets the extra_attrs of this Artifact.  # noqa: E501


        :return: The extra_attrs of this Artifact.  # noqa: E501
        :rtype: ExtraAttrs
        """
        return self._extra_attrs

    @extra_attrs.setter
    def extra_attrs(self, extra_attrs):
        """Sets the extra_attrs of this Artifact.


        :param extra_attrs: The extra_attrs of this Artifact.  # noqa: E501
        :type: ExtraAttrs
        """

        self._extra_attrs = extra_attrs

    @property
    def annotations(self):
        """Gets the annotations of this Artifact.  # noqa: E501


        :return: The annotations of this Artifact.  # noqa: E501
        :rtype: Annotations
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Artifact.


        :param annotations: The annotations of this Artifact.  # noqa: E501
        :type: Annotations
        """

        self._annotations = annotations

    @property
    def references(self):
        """Gets the references of this Artifact.  # noqa: E501


        :return: The references of this Artifact.  # noqa: E501
        :rtype: list[Reference]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this Artifact.


        :param references: The references of this Artifact.  # noqa: E501
        :type: list[Reference]
        """

        self._references = references

    @property
    def tags(self):
        """Gets the tags of this Artifact.  # noqa: E501


        :return: The tags of this Artifact.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Artifact.


        :param tags: The tags of this Artifact.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def addition_links(self):
        """Gets the addition_links of this Artifact.  # noqa: E501


        :return: The addition_links of this Artifact.  # noqa: E501
        :rtype: AdditionLinks
        """
        return self._addition_links

    @addition_links.setter
    def addition_links(self, addition_links):
        """Sets the addition_links of this Artifact.


        :param addition_links: The addition_links of this Artifact.  # noqa: E501
        :type: AdditionLinks
        """

        self._addition_links = addition_links

    @property
    def labels(self):
        """Gets the labels of this Artifact.  # noqa: E501


        :return: The labels of this Artifact.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Artifact.


        :param labels: The labels of this Artifact.  # noqa: E501
        :type: list[Label]
        """

        self._labels = labels

    @property
    def scan_overview(self):
        """Gets the scan_overview of this Artifact.  # noqa: E501

        The overview of the scan result.  # noqa: E501

        :return: The scan_overview of this Artifact.  # noqa: E501
        :rtype: ScanOverview
        """
        return self._scan_overview

    @scan_overview.setter
    def scan_overview(self, scan_overview):
        """Sets the scan_overview of this Artifact.

        The overview of the scan result.  # noqa: E501

        :param scan_overview: The scan_overview of this Artifact.  # noqa: E501
        :type: ScanOverview
        """

        self._scan_overview = scan_overview

    @property
    def accessories(self):
        """Gets the accessories of this Artifact.  # noqa: E501


        :return: The accessories of this Artifact.  # noqa: E501
        :rtype: list[Accessory]
        """
        return self._accessories

    @accessories.setter
    def accessories(self, accessories):
        """Sets the accessories of this Artifact.


        :param accessories: The accessories of this Artifact.  # noqa: E501
        :type: list[Accessory]
        """

        self._accessories = accessories

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(Artifact, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Artifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Artifact):
            return True

        return self.to_dict() != other.to_dict()
