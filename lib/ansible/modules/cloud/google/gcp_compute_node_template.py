#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_node_template
description:
- Represents a NodeTemplate resource. Node templates specify properties for creating
  sole-tenant nodes, such as node type, vCPU and memory requirements, node affinity
  labels, and region.
short_description: Creates a GCP NodeTemplate
version_added: '2.10'
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  description:
    description:
    - An optional textual description of the resource.
    required: false
    type: str
  name:
    description:
    - Name of the resource.
    required: false
    type: str
  node_affinity_labels:
    description:
    - Labels to use for node affinity, which will be used in instance scheduling.
    required: false
    type: dict
  node_type:
    description:
    - Node type to use for nodes group that are created from this template.
    - Only one of nodeTypeFlexibility and nodeType can be specified.
    required: false
    type: str
  node_type_flexibility:
    description:
    - Flexible properties for the desired node type. Node groups that use this node
      template will create nodes of a type that matches these properties. Only one
      of nodeTypeFlexibility and nodeType can be specified.
    required: false
    type: dict
    suboptions:
      cpus:
        description:
        - Number of virtual CPUs to use.
        required: false
        type: str
      memory:
        description:
        - Physical memory available to the node, defined in MB.
        required: false
        type: str
  region:
    description:
    - Region where nodes using the node template will be created .
    required: true
    type: str
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates)'
- 'Sole-Tenant Nodes: U(https://cloud.google.com/compute/docs/nodes/)'
- for authentication, you can set service_account_file using the c(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the c(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a node template
  gcp_compute_node_template:
    name: test_object
    region: us-central1
    node_type: n1-node-96-624
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
description:
  description:
  - An optional textual description of the resource.
  returned: success
  type: str
name:
  description:
  - Name of the resource.
  returned: success
  type: str
nodeAffinityLabels:
  description:
  - Labels to use for node affinity, which will be used in instance scheduling.
  returned: success
  type: dict
nodeType:
  description:
  - Node type to use for nodes group that are created from this template.
  - Only one of nodeTypeFlexibility and nodeType can be specified.
  returned: success
  type: str
nodeTypeFlexibility:
  description:
  - Flexible properties for the desired node type. Node groups that use this node
    template will create nodes of a type that matches these properties. Only one of
    nodeTypeFlexibility and nodeType can be specified.
  returned: success
  type: complex
  contains:
    cpus:
      description:
      - Number of virtual CPUs to use.
      returned: success
      type: str
    memory:
      description:
      - Physical memory available to the node, defined in MB.
      returned: success
      type: str
    localSsd:
      description:
      - Use local SSD .
      returned: success
      type: str
region:
  description:
  - Region where nodes using the node template will be created .
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            description=dict(type='str'),
            name=dict(type='str'),
            node_affinity_labels=dict(type='dict'),
            node_type=dict(type='str'),
            node_type_flexibility=dict(type='dict', options=dict(cpus=dict(type='str'), memory=dict(type='str'))),
            region=dict(required=True, type='str'),
        ),
        mutually_exclusive=[['node_type', 'node_type_flexibility']],
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#nodeTemplate'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    delete(module, self_link(module), kind)
    create(module, collection(module), kind)


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#nodeTemplate',
        u'description': module.params.get('description'),
        u'name': module.params.get('name'),
        u'nodeAffinityLabels': module.params.get('node_affinity_labels'),
        u'nodeType': module.params.get('node_type'),
        u'nodeTypeFlexibility': NodeTemplateNodetypeflexibility(module.params.get('node_type_flexibility', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/nodeTemplates/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/nodeTemplates".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'name': response.get(u'name'),
        u'nodeAffinityLabels': response.get(u'nodeAffinityLabels'),
        u'nodeType': response.get(u'nodeType'),
        u'nodeTypeFlexibility': NodeTemplateNodetypeflexibility(response.get(u'nodeTypeFlexibility', {}), module).from_response(),
    }


def region_selflink(name, params):
    if name is None:
        return
    url = r"https://www.googleapis.com/compute/v1/projects/.*/regions/.*"
    if not re.match(url, name):
        name = "https://www.googleapis.com/compute/v1/projects/{project}/regions/%s".format(**params) % name
    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#nodeTemplate')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class NodeTemplateNodetypeflexibility(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'cpus': self.request.get('cpus'), u'memory': self.request.get('memory')})

    def from_response(self):
        return remove_nones_from_dict({u'cpus': self.request.get(u'cpus'), u'memory': self.request.get(u'memory')})


if __name__ == '__main__':
    main()
