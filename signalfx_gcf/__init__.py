import signalfx_serverless_common

# backwards compatibility
def wrapper(*args, **kwargs):
    return signalfx_serverless_common.wrapper(*args, **kwargs)


def emits_metrics(*args, **kwargs):
    return signalfx_serverless_common.emits_metrics(*args, **kwargs)


def is_traced(*args, **kwargs):
    return signalfx_serverless_common.is_traced(*args, **kwargs)


# less convenient method
def send_metric(counters=[], gauges=[]):
    signalfx_serverless_common.send_metric(counters, gauges)


# convenience method
def send_counter(metric_name, metric_value=1, dimensions={}):
    signalfx_serverless_common.send_counter(metric_name, metric_value, dimensions)


# convenience method
def send_gauge(metric_name, metric_value, dimensions={}):
    signalfx_serverless_common.send_gauge(metric_name, metric_value, dimensions)

