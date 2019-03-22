import os
import warnings

from .version import name, version

fields = {}
dim_prefix = 'gcf'

def get_fields():
    env_dims = {
        'FUNCTION_REGION': dim_prefix + '_region',
        'GCP_PROJECT': dim_prefix + '_project_id',
        'FUNCTION_NAME': dim_prefix + '_function_name',
        'X_GOOGLE_FUNCTION_VERSION': dim_prefix + '_function_version'
    }

    for env_name, dim in env_dims.items():
        runtime_env = os.environ.get(env_name)
        if env_name is not None:
            fields[dim] = runtime_env
    
    fields['function_wrapper_version'] = name + '_' + version

    return fields.copy()


def get_metrics_url():
    url = os.environ.get('SIGNALFX_INGEST_ENDPOINT')
    if url:
        warnings.warn('SIGNALFX_INGEST_ENDPOINT is deprecated, use SIGNALFX_METRICS_URL instead.', DeprecationWarning)
    else:
        url = os.environ.get('SIGNALFX_METRICS_URL')

    if not url:
        url = os.environ.get('SIGNALFX_ENDPOINT_URL', 'https://pops.signalfx.com')

    return url


def get_tracing_url():
    url = os.environ.get('SIGNALFX_TRACING_URL')

    if not url:
        url = os.environ.get('SIGNALFX_ENDPOINT_URL')

        if url:
            # if the common endpoint url is used, we need to append the trace path
            url = url + '/v1/trace'
        else:
            url = 'https://ingest.signalfx.com/v1/trace'

    return url


def get_access_token():
    token = os.environ.get('SIGNALFX_ACCESS_TOKEN')
    if not token:
        warnings.warn('SIGNALFX_AUTH_TOKEN is deprecated, use SIGNALFX_ACCESS_TOKEN instead.', DeprecationWarning)
        token = os.environ.get('SIGNALFX_AUTH_TOKEN')

    return token
