#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import grpc
import demo_pb2
import demo_pb2_grpc

from opentelemetry import trace
from opentelemetry.instrumentation.grpc import server_interceptor
from opentelemetry.instrumentation.grpc.grpcext import intercept_server
from opentelemetry.instrumentation.grpc import client_interceptor
from opentelemetry.instrumentation.grpc.grpcext import intercept_channel
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.sdk.trace.export import Span, SpanExporter, SpanExportResult



from logger import getJSONLogger
otlp_host = os.environ.get('OTLP_HOST')
otlp_port = os.environ.get('OTLP_PORT')
# create a CollectorSpanExporter
collector_exporter = OTLPSpanExporter(
     endpoint=otlp_host+":"+otlp_port,
      insecure=True
    # host_name="machine/container name",
)
resource = Resource(attributes={
    "service.name": "EmailService"
})
# Create a BatchExportSpanProcessor and add the exporter to it
# Create a BatchExportSpanProcessor and add the exporter to it
span_processor = BatchExportSpanProcessor(collector_exporter)

# Configure the tracer to use the collector exporter
tracer_provider = TracerProvider(resource=resource))
tracer_provider.add_span_processor(span_processor)
tracer = TracerProvider().get_tracer(__name__)
logger = getJSONLogger('recommendationservice-server')

if __name__ == "__main__":
    # get port
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = "8080"

    try:
        exporter = stackdriver_exporter.StackdriverExporter()
        tracer = Tracer(exporter=exporter)
        tracer_interceptor = client_interceptor.OpenCensusClientInterceptor(tracer, host_port='localhost:'+port)
    except:
        tracer_interceptor = client_interceptor.OpenCensusClientInterceptor()

    # set up server stub
    channel = grpc.insecure_channel('localhost:'+port)
    channel = grpc.intercept_channel(channel, tracer_interceptor)
    stub = demo_pb2_grpc.RecommendationServiceStub(channel)
    # form request
    request = demo_pb2.ListRecommendationsRequest(user_id="test", product_ids=["test"])
    # make call to server
    response = stub.ListRecommendations(request)
    logger.info(response)
