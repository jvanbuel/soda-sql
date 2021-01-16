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
import random
import string

from tests.common.sql_test_case import TARGET_BIGQUERY
from tests.common.sql_test_suite import SqlTestSuite


class BigQuerySuite(SqlTestSuite):

    def setUp(self) -> None:
        self.target = TARGET_BIGQUERY
        super().setUp()

    @staticmethod
    def generate_test_table_name():
        """
        We need to generate a different table name for each BigQuery test, otherwise we exceed the daily rate
        limits for table operation.
        """
        return 'test_table_' + ''.join([random.choice(string.ascii_lowercase) for _ in range(5)])
