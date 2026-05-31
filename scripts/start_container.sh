#!/bin/bash

set -e

docker pull lineesh3329/sample-python-project

docker run -d -p 5000:5000 lineesh3329/sample-python-project
