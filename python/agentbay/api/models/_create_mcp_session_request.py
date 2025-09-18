# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wuyingai20250506 import models as main_models
from darabonba.model import DaraModel

class CreateMcpSessionRequest(DaraModel):
    def __init__(
        self,
        authorization: str = None,
        context_id: str = None,
        external_user_id: str = None,
        image_id: str = None,
        labels: str = None,
        mcp_policy_id: str = None,
        network_id: str = None,
        persistence_data_list: List[main_models.CreateMcpSessionRequestPersistenceDataList] = None,
        session_id: str = None,
        vpc_resource: bool = None,
    ):
        self.authorization = authorization
        self.context_id = context_id
        self.external_user_id = external_user_id
        self.image_id = image_id
        self.labels = labels
        self.mcp_policy_id = mcp_policy_id
        self.network_id = network_id
        self.persistence_data_list = persistence_data_list
        self.session_id = session_id
        self.vpc_resource = vpc_resource

    def validate(self):
        if self.persistence_data_list:
            for v1 in self.persistence_data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization is not None:
            result['Authorization'] = self.authorization

        if self.context_id is not None:
            result['ContextId'] = self.context_id

        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.mcp_policy_id is not None:
            result['McpPolicyId'] = self.mcp_policy_id

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        result['PersistenceDataList'] = []
        if self.persistence_data_list is not None:
            for k1 in self.persistence_data_list:
                result['PersistenceDataList'].append(k1.to_map() if k1 else None)

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.vpc_resource is not None:
            result['VpcResource'] = self.vpc_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')

        if m.get('ContextId') is not None:
            self.context_id = m.get('ContextId')

        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('McpPolicyId') is not None:
            self.mcp_policy_id = m.get('McpPolicyId')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        self.persistence_data_list = []
        if m.get('PersistenceDataList') is not None:
            for k1 in m.get('PersistenceDataList'):
                temp_model = main_models.CreateMcpSessionRequestPersistenceDataList()
                self.persistence_data_list.append(temp_model.from_map(k1))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('VpcResource') is not None:
            self.vpc_resource = m.get('VpcResource')

        return self

class CreateMcpSessionRequestPersistenceDataList(DaraModel):
    def __init__(
        self,
        context_id: str = None,
        path: str = None,
        policy: str = None,
    ):
        self.context_id = context_id
        self.path = path
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_id is not None:
            result['ContextId'] = self.context_id

        if self.path is not None:
            result['Path'] = self.path

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextId') is not None:
            self.context_id = m.get('ContextId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

