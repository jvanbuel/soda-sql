#  Copyright 2020 Soda
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import json

import pyathena
from google.cloud import bigquery
from google.cloud.bigquery import dbapi
from google.oauth2.service_account import Credentials

from sodasql.credentials.aws_credentials import AwsCredentials
from sodasql.scan.dialect import Dialect
from sodasql.scan.parse_logs import ParseLogs


class AthenaDialect(Dialect):

    def __init__(self, warehouse_configuration: dict, parse_logs: ParseLogs):
        super().__init__()
        self.aws_credentials = AwsCredentials.from_configuration(warehouse_configuration)
        self.athena_staging_dir = warehouse_configuration.get('staging_dir')
        self.database = warehouse_configuration.get('database')
        self.schema = warehouse_configuration.get('schema')

    def create_connection(self):
        # pyathena.connect will do the role resolving
        # aws_credentials = self.aws_credentials.resolve_role('soda_scan')
        return pyathena.connect(
            aws_access_key_id=self.aws_credentials.access_key_id,
            aws_secret_access_key=self.aws_credentials.secret_access_key,
            s3_staging_dir=self.athena_staging_dir,
            region_name=self.aws_credentials.region_name,
            role_arn=self.aws_credentials.role_arn)