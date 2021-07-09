# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER
#
# Copyright 2018 Juniper Networks, Inc. 
# All rights reserved.
#
# Licensed under the Juniper Networks Script Software License (the "License").
# You may not use this script file except in compliance with the License, which is located at
# http://www.juniper.net/support/legal/scriptlicense/
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Please make sure to run this file as a root user

GET_VERSION= python -c 'import versioneer;print(versioneer.get_version())'

build:
	cd docs && make html
	cp -r docs/jnpr_healthbot_swagger/swagger_client/ lib/jnpr/healthbot/swagger/
	cd lib/jnpr/healthbot/swagger/ && sed -i '' -e 's/from\ swagger_client/from\ jnpr.healthbot.swagger/g' *.py
	cd lib/jnpr/healthbot/swagger/ && sed -i '' -e 's/swagger_client/jnpr.healthbot.swagger/g' *.py
	cd lib/jnpr/healthbot/swagger/api && sed -i '' -e 's/from\ swagger_client/from\ jnpr.healthbot.swagger/g' *.py
	cd lib/jnpr/healthbot/swagger/models && sed -i '' -e 's/from\ swagger_client/from\ jnpr.healthbot.swagger/g' *.py
	python3 setup.py bdist_wheel

.PHONY: version clean
version:
	@$(call GET_VERSION)

test:
	tox -e unittest

clean:
	rm -rf build dist docs/_build .tox .coverage lib/hbez.egg-info
