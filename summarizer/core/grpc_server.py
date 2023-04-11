import grpc
import utils.morphology_pb2 as z_morphology
import utils.morphology_pb2_grpc as z_morphology_g
import utils.normalization_pb2 as z_normalization
import utils.normalization_pb2_grpc as z_normalization_g


channel = grpc.insecure_channel("localhost:6789")
morphology_stub = z_morphology_g.MorphologyServiceStub(channel)
normalization_stub = z_normalization_g.NormalizationServiceStub(channel)
