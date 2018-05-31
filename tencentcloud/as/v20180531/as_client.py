# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cvm.v20170312 import models


class AutoScalingClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'scaling.api.qcloud.com'


    def CreateScalingConfiguration(self, request):
        """本接口 (CreateScalingConfiguration) 用于创建新的启动配置。

        1）启动配置无法编辑更改。如需使用新的启动配置，只能重新创建新的启动配置。
        2）创建启动配置时，必须要选择镜像，用来确定新创建实例的系统盘配置。
        3）创建启动配置时，当前仅支持指定一个安全组，具体相关限制详见创建实例。
        4）系统盘类型与数据盘类型一致。
        5）每个项目最多只能创建20个启动配置，详见使用限制。

        :param request: 调用CreateScalingConfiguration所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateScalingConfigurationRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateScalingConfigurationResponse`
        """
        try:
            params = request._serialize()
            body = self.call("CreateScalingConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScalingConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)

    def DescribeScalingConfiguration(self, request):
        """本接口 (DescribeScalingConfiguration) 用于查询启动配置的信息。

        :param request: 调用DescribeScalingConfiguration所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeScalingConfigurationRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeScalingConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScalingConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScalingConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)

    def DeleteScalingConfiguration(self, request):
        """本接口 (DeleteScalingConfiguration) 用于删除启动配置。

        1）若启动配置在伸缩组中属于生效状态，则该启动配置不允许删除。
        2）若某个启动配置创建的任意一个CVM实例仍存在于伸缩组中，则该启动配置不允许删除。

        :param request: 调用DeleteScalingConfiguration所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteScalingConfigurationRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteScalingConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScalingConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScalingConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateScalingGroup(self, request):
        """本接口 (CreateScalingGroup) 用于创建新的伸缩组。

        1）伸缩组、负载均衡实例必须在同一个地域、同一项目。
        2）每个项目最多只能创建20个伸缩组。
        3）一个伸缩组只能对应1个启动配置。

        :param request: 调用CreateScalingGroup所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateScalingGroupRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScalingGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)

    def DescribeScalingGroup(self, request):
        """本接口(DescribeScalingGroup)用于查询伸缩组的详细信息，可根据伸缩组ID、伸缩组名称、启动配置ID等对结果进行过滤。

        :param request: 调用DescribeScalingGroup所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeScalingGroupRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScalingGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyScalingGroup(self, request):
        """本接口 (ModifyScalingGroup) 用于修改特定伸缩组的属性。

        1）本接口是根据scalingGroupId对相应伸缩组属性进行修改的，且只允许修改以下属性：
             maxSize：最大伸缩数，即伸缩组内CVM实例的最大值
             minSize：最小伸缩数，即伸缩组内CVM实例的最小值
             removePolicy：移除策略，指的是当需要移除实例时，移除最先还是最后加入伸缩组的实例
             scalingGroupName：伸缩组名称
             desiredCapacity：期望实例数
             scalingConfigurationId：启动配置
             zoneIds：伸缩组关联可用区
             subnetIds：伸缩组关联子网
             loadBalancerIds：伸缩组关联的传统型负载均衡
             forwardLBInfos：伸缩组关联的应用型负载均衡
           其余属性无法修改。
        2）当伸缩组的CVM实例数不满足修改后的maxSize、minSize、desiredCapacity，弹性伸缩服务会自动加入或移出CVM实例，
           使得伸缩组的CVM实例数满足在maxSize和minSize之间并且等于desiredCapacity。

        :param request: 调用ModifyScalingGroup所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyScalingGroupRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyScalingGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetCvmProtectedDetach(self, request):
        """本接口（SetCvmProtectedDetach）用于设置子机移除保护。

        子机设置为移除保护之后，当发生不健康替换、报警策略、期望值变更等触发缩容时，将不对此子机缩容操作。

        :param request: 调用SetCvmProtectedDetach所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.SetCvmProtectedDetachRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.SetCvmProtectedDetachResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetCvmProtectedDetach", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetCvmProtectedDetachResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScalingInstance(self, request):
        """本接口 (DescribeScalingInstance) 用于查询伸缩组绑定的云服务器。

        1）查询时可以根据伸缩组ID、云服务器ID、实例健康状态、实例创建类型等对结果进行过滤。
        2）加入伸缩组的CVM实例有两种类型：自动创建的CVM实例、手工添加的CVM实例。
           “自动创建的CVM实例”是指根据用户的伸缩配置和伸缩规则，由弹性伸缩服务自动创建的CVM实例。
           “手工添加的CVM实例”是指不是由弹性伸缩服务创建，但由用户手工添加到伸缩组中的CVM实例。
        3）CVM实例在伸缩组中的生命周期，通过以下几种状态描述：
            创建中（Creating）-表示正在创建CVM实例。
            运行中（InService）-表示实例正在运行。
            移除中（Removing）-表示伸缩组正在移除实例。
            绑定中（Attaching）-表示正在将实例绑定到伸缩组。
            解绑中（Detaching）-表示正在将实例从伸缩组解绑。
            备份中（Backuping）-表示正在备份实例。
            解除备份中（UnBackuping）-表示正在删除备份的实例。
            绑定LB中（AttachLb）-表示正在绑定负载均衡。
            解绑LB中（DetachLb）-表示正在解绑负载均衡。
            预热中（Preheating）-表示实例正在预热。
        4）CVM实例在伸缩组中的健康状态为：
            健康（Healthy）
            不健康（Unhealthy）
            AS会自动移出伸缩组中不健康的CVM实例。对于“自动创建的CVM实例”，CVM会停止和释放该CVM实例。
            对于“手工添加的CVM实例”，AS不会停止和释放该CVM实例。

        :param request: 调用DescribeScalingInstance所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeScalingInstanceRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeScalingInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScalingInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScalingInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachInstance(self, request):
        """本接口 (AttachInstance) 用于向指定的伸缩组添加CVM实例。

        1）加入的CVM实例有以下几点限定条件：
            加入的CVM实例必须与伸缩组在同一个地域。
            加入的CVM实例的状态必须是“运行”状态。
            加入的CVM实例不能已加入到其它伸缩组中。
        2）当伸缩组为生效（active）状态，才可以执行此功能。
        3）当伸缩组没有伸缩活动正在执行，才可以执行此功能。
        4）当伸缩组没有伸缩活动正在执行时，该功能可以绕过冷却时间（Cooldown）直接执行。
        5）如果该功能指定的实例数加上当前伸缩组的实例数大于该伸缩组规定的最大伸缩数时，则调用失败。
        6）手工添加的CVM实例不与伸缩组生效的伸缩配置进行关联。

        :param request: 调用AttachInstance所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.AttachInstanceRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.AttachInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachInstance(self, request):
        """本接口(DetachInstance)用于从指定的伸缩组移出CVM实例。

        :param request: 调用DetachInstance所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DetachInstanceRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DetachInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScalingActivity(self, request):
        """本接口（DescribeScalingActivity）用于查询伸缩组的伸缩活动记录。

        :param request: 调用DescribeScalingActivity所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeScalingActivityRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeScalingActivityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScalingActivity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScalingActivityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteScalingGroup(self, request):
        """本接口(DeleteScalingGroup) 用于删除特定伸缩组。本接口是根据scalingGroupId来删除相应伸缩组的。

        1）必须同时满足以下两个条件，才能删除伸缩组。
           条件一：伸缩组没有任何伸缩活动正在执行。
           条件二：伸缩组当前的CVM实例数量为0。
        2）删除伸缩组时会删除相关联的伸缩配置、伸缩规则、伸缩活动、伸缩请求的信息。
        3）删除伸缩组时不会删除以下任务或实例：定时任务、云监控报警任务、负载均衡实例。

        :param request: 调用DeleteScalingGroup所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteScalingGroupRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScalingGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


