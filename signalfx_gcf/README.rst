SignalFx Python Google Cloud Function Wrapper
=============================================

SignalFx Python Google Cloud Function Wrapper


Usage
-----

The SignalFx Python Google Cloud Function Wrapper is a wrapper around a Google
Cloud Function Python function handler, used to instrument execution of the
function and send metrics and traces to SignalFx.

Installation
~~~~~~~~~~~~

To install from PyPi

::

    $ pip install signalfx_serverless_gcf

Configuring the ingest endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, this function wrapper will send to the `us0` realm. If you are
not in this realm you will need to set the `SIGNALFX_INGEST_ENDPOINT`
environment variable to the correct realm ingest endpoint
(https://ingest.{REALM}.signalfx.com).
To determine what realm you are in, check your profile page in the SignalFx
web application (click the avatar in the upper right and click My Profile).


Environment Variables
~~~~~~~~~~~~~~~~~~~~~

**Note: the environment variables SIGNALFX_INGEST_ENDPOINT and
SIGNALFX_AUTH_TOKEN are being deprecated and will not be supported in future
releases.**

::

    SIGNALFX_ACCESS_TOKEN=access token

    # endpoint for both metrics and tracer. Overridden by SIGNALFX_METRICS_URL
    # and SIGNALFX_TRACING_URL if set
    SIGNALFX_ENDPOINT_URL=endpoint url

    # optional metrics and tracing configuration

    SIGNALFX_METRICS_URL=ingest endpoint [ default: https://pops.signalfx.com ]
    SIGNALFX_SEND_TIMEOUT=timeout in seconds for sending datapoint [ default: 0.3 ]

    SIGNALFX_TRACING_URL=tracing endpoint [ default: https://ingest.signalfx.com/v1/trace ]

SIGNALFX_ENDPOINT_URL can be used to configure a common endpoint for metrics
and traces, as is the case when forwarding with the Smart Gateway.
The path :code:`/v1/traces` will automatically be added to the endpoint for
traces.

If either SIGNALFX_TRACING_URL or SIGNALFX_METRICS_URL are set, they will take
precendence over SIGNALFX_ENDPOINT_URL for their respective components.

For example, if only SIGNALFX_ENDPOINT_URL is set:

::

    SIGNALFX_ENDPOINT_URL=<gateway_address>

both metrics and traces will be sent to the gateway address.

If SIGNALFX_ENDPOINT_URL and SIGNALFX_METRICS_URL are set:

::

    SIGNALFX_METRICS_URL=https://pops.signalfx.com

    SIGNALFX_ENDPOINT_URL=<gateway_address>

Traces will be sent to the gateway and metrics will go through POPS.

Wrapping a function
~~~~~~~~~~~~~~~~~~~

There are two wrappers provided.

For metrics, decorate your handler with @signalfx_gcf.emits_metrics

::

    import signalfx_gcf

    @signalfx_gcf.emits_metrics
    def handler(request):
        # your code

For tracing, use the @signalfx_gcf.is_traced decorator

::

    import signalfx_gcf

    @signalfx_gcf.is_traced
    def handler(request):
        # your code

The decorators can be used individually or together.

Metrics and dimensions sent by the metrics wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Google Cloud Function wrapper sends the following metrics to SignalFx:

+-----------------------+-----------------------+-----------------------+
| Metric Name           | Type                  | Description           |
+=======================+=======================+=======================+
| function.invocations  | Counter               | Count number of Cloud |
|                       |                       | Funtion invocations   |
+-----------------------+-----------------------+-----------------------+
| function.cold_starts  | Counter               | Count number of cold  |
|                       |                       | starts                |
+-----------------------+-----------------------+-----------------------+
| function.errors       | Counter               | Count number of       |
|                       |                       | errors from           |
|                       |                       | underlying Cloud      |
|                       |                       | Function handler      |
+-----------------------+-----------------------+-----------------------+
| function.duration     | Gauge                 | Milliseconds in       |
|                       |                       | execution time of     |
|                       |                       | underlying Cloud      |
|                       |                       | Function handler      |
+-----------------------+-----------------------+-----------------------+

The Google Cloud Function wrapper adds the following dimensions to all data
points send to SignalFx:

+----------------------------------+----------------------------------+
| Tag                              | Description                      |
+==================================+==================================+
| gcf_region                       | Google Cloud Function Region     |
+----------------------------------+----------------------------------+
| gcf_project_id                   | Google Cloud Function Project ID |
+----------------------------------+----------------------------------+
| gcf_function_name                | Google Cloud Function Name       |
+----------------------------------+----------------------------------+
| gcf_function_version             | Google Cloud Function Version    |
+----------------------------------+----------------------------------+
| function_wrapper_version         | SignalFx function wrapper        |
|                                  | qualifier                        |
|                                  | (e.g. signalfx_gcf_0.0.2)        |
+----------------------------------+----------------------------------+
| metric_source                    | The literal value of             |
|                                  | ‘gcf_wrapper’                    |
+----------------------------------+----------------------------------+

Traces and tags sent by the Tracing wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tracing wrapper creates a span for the wrapper handler. This span has the
following tags:

+----------------------------------+----------------------------------+
| Tag                              | Description                      |
+==================================+==================================+
| gcf_region                       | Google Cloud Function Region     |
+----------------------------------+----------------------------------+
| gcf_project_id                   | Google Cloud Function Project ID |
+----------------------------------+----------------------------------+
| gcf_function_name                | Google Cloud Function Name       |
+----------------------------------+----------------------------------+
| gcf_function_version             | Google Cloud Function Version    |
+----------------------------------+----------------------------------+
| function_wrapper_version         | SignalFx function wrapper        |
|                                  | qualifier                        |
|                                  | (e.g. signalfx_gcf_0.0.2)        |
+----------------------------------+----------------------------------+
| component                        | The literal value of             |
|                                  | ‘python-gcf-wrapper’             |
+----------------------------------+----------------------------------+

Sending custom metric from the Google Cloud Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import signalfx_gcf

    # sending application_performance metric with value 100 and dimension abc:def
    signalfx_gcf.send_gauge('application_performance', 100, {'abc':'def'})

    # sending counter metric with no dimension
    signalfx_gcf.send_counter('database_calls', 1)

Adding manual tracing to the Google Cloud Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Manual instrumentation can be added to trace critical parts of your handler
function.

::

    import opentracing

    tracer = opentracing.tracer

    def some_function():
        with tracer.start_active_span("span_name", tags=tags) as scope:

            # do some work

            span = scope.span
            span.set_tag("example_tag", "example_value")

More examples and usage information can be found in the Jaeger Python Tracer
`documentation <https://github.com/signalfx/jaeger-client-python>`_.


Packaging
~~~~~~~~~

::

    python setup.py bdist_wheel --universal

License
~~~~~~~

Apache Software License v2. Copyright © 2019 SignalFx
