#!/usr/bin/env bash

set -ex

export PROJ_HOME=/home/logic/_workspace/LYNKED_QA_project
export DOCS_DIR=$PROJ_HOME/docs
export FLOWS_DIR=$DOCS_DIR/flows
export TEST_SITE_FLOWS_DIR=$FLOWS_DIR/test_site_flows
export PATH=$PATH:$TEST_SITE_FLOWS_DIR/node_modules/.bin

# mmdc -i happy_flow_1.mmd -o happy_flow_1.png
# mmdc -i happy_flow_1.mmd -o happy_flow_1.png

# npm install

mmdc -i $FLOWS_DIR/user_flow/happy-flow-1.mmd -o $FLOWS_DIR/user_flow/happy-flow-1.png
