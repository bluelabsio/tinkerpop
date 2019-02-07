'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''
import codecs
import os
import sys
import time
from setuptools import setup

install_requires = [
    'aenum>=1.4.5',
    'tornado>=4.4.1,<5.0',
    'six>=1.10.0'
]

if sys.version_info < (3,2):
    install_requires += ['futures>=3.0.5']

setup(
    name='gremlinpython',
    version=3.3.6,
    packages=['gremlin_python', 'gremlin_python.driver',
              'gremlin_python.driver.tornado', 'gremlin_python.process',
              'gremlin_python.structure', 'gremlin_python.structure.io'],
    license='Apache 2',
    url='http://tinkerpop.apache.org',
    description='Gremlin-Python for Apache TinkerPop',
    long_description=codecs.open("README", "r", "UTF-8").read(),
    test_suite="tests",
    data_files=[("", ["LICENSE", "NOTICE"])],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'mock',
        'radish-bdd==0.8.6',
        'PyHamcrest'
    ],
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ]
)
