# -*- coding: utf-8 -*-
"""
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""

class GatewayProxyBaseExp(Exception):
    def __init__(self, app_name="", path="", msg="", env=""):
        self.app_name = app_name
        self.path = path
        self.msg = msg
        self.env = env

    def __str__(self):
        return "Gateway Proxy Exception, app_name:{}, path is:({}), msg:{}".format(self.app_name, self.path, self.msg)

    def __repr__(self):
        return self.__str__()


class EnvTypeExp(GatewayProxyBaseExp):
    pass


class SetUpUriExp(GatewayProxyBaseExp):
    pass


class SetUpRegisterExp(GatewayProxyBaseExp):
    pass


class GetRegisterTokenErr(GatewayProxyBaseExp):
    pass


class SetUpGatewayExp(GatewayProxyBaseExp):
    pass


class RegisterUriExp(GatewayProxyBaseExp):
    pass


class RegisterMetaDataExp(GatewayProxyBaseExp):
    pass


class RegisterAllMetaDataExp(GatewayProxyBaseExp):
    pass
