# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import utils.morphology_pb2 as morphology__pb2


class MorphologyServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.AnalyzeSentence = channel.unary_unary(
            "/zemberek.morphology.MorphologyService/AnalyzeSentence",
            request_serializer=morphology__pb2.SentenceAnalysisRequest.SerializeToString,
            response_deserializer=morphology__pb2.SentenceAnalysisProto.FromString,
        )
        self.AnalyzeWord = channel.unary_unary(
            "/zemberek.morphology.MorphologyService/AnalyzeWord",
            request_serializer=morphology__pb2.WordAnalysisRequest.SerializeToString,
            response_deserializer=morphology__pb2.WordAnalysisProto.FromString,
        )


class MorphologyServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def AnalyzeSentence(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AnalyzeWord(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MorphologyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AnalyzeSentence": grpc.unary_unary_rpc_method_handler(
            servicer.AnalyzeSentence,
            request_deserializer=morphology__pb2.SentenceAnalysisRequest.FromString,
            response_serializer=morphology__pb2.SentenceAnalysisProto.SerializeToString,
        ),
        "AnalyzeWord": grpc.unary_unary_rpc_method_handler(
            servicer.AnalyzeWord,
            request_deserializer=morphology__pb2.WordAnalysisRequest.FromString,
            response_serializer=morphology__pb2.WordAnalysisProto.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "zemberek.morphology.MorphologyService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
