# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from netograph.dsetapi import dset_pb2 as dsetapi_dot_dset__pb2


class DsetStub(object):
  """Methods that operate on an individual dataset, either public or private.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubmitCapture = channel.unary_unary(
        '/io.netograph.dset.Dset/SubmitCapture',
        request_serializer=dsetapi_dot_dset__pb2.SubmitCaptureRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.SubmitCaptureResult.FromString,
        )
    self.CaptureInfo = channel.unary_unary(
        '/io.netograph.dset.Dset/CaptureInfo',
        request_serializer=dsetapi_dot_dset__pb2.CaptureInfoRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.CaptureInfoResult.FromString,
        )
    self.CaptureLog = channel.unary_stream(
        '/io.netograph.dset.Dset/CaptureLog',
        request_serializer=dsetapi_dot_dset__pb2.CaptureLogRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.CaptureLogResult.FromString,
        )
    self.CertDomainSearch = channel.unary_stream(
        '/io.netograph.dset.Dset/CertDomainSearch',
        request_serializer=dsetapi_dot_dset__pb2.CertDomainSearchRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.CertDomainSearchResult.FromString,
        )
    self.CertIPSearch = channel.unary_stream(
        '/io.netograph.dset.Dset/CertIPSearch',
        request_serializer=dsetapi_dot_dset__pb2.CertIPSearchRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.CertIPSearchResult.FromString,
        )
    self.DomainHistory = channel.unary_stream(
        '/io.netograph.dset.Dset/DomainHistory',
        request_serializer=dsetapi_dot_dset__pb2.DomainHistoryRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.DomainHistoryResult.FromString,
        )
    self.DomainSearch = channel.unary_stream(
        '/io.netograph.dset.Dset/DomainSearch',
        request_serializer=dsetapi_dot_dset__pb2.DomainSearchRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.DomainSearchResult.FromString,
        )
    self.DomainsForIP = channel.unary_stream(
        '/io.netograph.dset.Dset/DomainsForIP',
        request_serializer=dsetapi_dot_dset__pb2.DomainsForIPRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.DomainsForIPResult.FromString,
        )
    self.IPHistory = channel.unary_stream(
        '/io.netograph.dset.Dset/IPHistory',
        request_serializer=dsetapi_dot_dset__pb2.IPHistoryRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.IPHistoryResult.FromString,
        )
    self.IPLogSearch = channel.unary_stream(
        '/io.netograph.dset.Dset/IPLogSearch',
        request_serializer=dsetapi_dot_dset__pb2.IPLogSearchRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.IPLogSearchResult.FromString,
        )
    self.IPSearch = channel.unary_stream(
        '/io.netograph.dset.Dset/IPSearch',
        request_serializer=dsetapi_dot_dset__pb2.IPSearchRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.IPSearchResult.FromString,
        )
    self.IPsForDomain = channel.unary_stream(
        '/io.netograph.dset.Dset/IPsForDomain',
        request_serializer=dsetapi_dot_dset__pb2.IPsForDomainRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.IPsForDomainResult.FromString,
        )
    self.MetaForCapture = channel.unary_stream(
        '/io.netograph.dset.Dset/MetaForCapture',
        request_serializer=dsetapi_dot_dset__pb2.MetaForCaptureRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.MetaForCaptureResult.FromString,
        )
    self.MetaSearch = channel.unary_stream(
        '/io.netograph.dset.Dset/MetaSearch',
        request_serializer=dsetapi_dot_dset__pb2.MetaSearchRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.MetaSearchResult.FromString,
        )
    self.PoliciesForRoot = channel.unary_stream(
        '/io.netograph.dset.Dset/PoliciesForRoot',
        request_serializer=dsetapi_dot_dset__pb2.PoliciesForRootRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.PoliciesForRootResult.FromString,
        )
    self.PolicyDomainCaptures = channel.unary_stream(
        '/io.netograph.dset.Dset/PolicyDomainCaptures',
        request_serializer=dsetapi_dot_dset__pb2.PolicyDomainCapturesRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.PolicyDomainCapturesResult.FromString,
        )
    self.PolicyDomainStats = channel.unary_unary(
        '/io.netograph.dset.Dset/PolicyDomainStats',
        request_serializer=dsetapi_dot_dset__pb2.PolicyDomainStatsRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.PolicyDomainStatsResult.FromString,
        )
    self.PolicyURLCaptures = channel.unary_stream(
        '/io.netograph.dset.Dset/PolicyURLCaptures',
        request_serializer=dsetapi_dot_dset__pb2.PolicyURLCapturesRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.PolicyURLCapturesResult.FromString,
        )
    self.RedirsByDestination = channel.unary_stream(
        '/io.netograph.dset.Dset/RedirsByDestination',
        request_serializer=dsetapi_dot_dset__pb2.RedirsByDestinationRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.RedirsByDestinationResult.FromString,
        )
    self.RedirsBySource = channel.unary_stream(
        '/io.netograph.dset.Dset/RedirsBySource',
        request_serializer=dsetapi_dot_dset__pb2.RedirsBySourceRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.RedirsBySourceResult.FromString,
        )
    self.RootLogSearch = channel.unary_stream(
        '/io.netograph.dset.Dset/RootLogSearch',
        request_serializer=dsetapi_dot_dset__pb2.RootLogSearchRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.RootLogSearchResult.FromString,
        )
    self.RootsForSatellite = channel.unary_stream(
        '/io.netograph.dset.Dset/RootsForSatellite',
        request_serializer=dsetapi_dot_dset__pb2.RootsForSatelliteRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.RootsForSatelliteResult.FromString,
        )
    self.SatelliteLogSearch = channel.unary_stream(
        '/io.netograph.dset.Dset/SatelliteLogSearch',
        request_serializer=dsetapi_dot_dset__pb2.SatelliteLogSearchRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.SatelliteLogSearchResult.FromString,
        )
    self.SatellitesForRoot = channel.unary_stream(
        '/io.netograph.dset.Dset/SatellitesForRoot',
        request_serializer=dsetapi_dot_dset__pb2.SatellitesForRootRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.SatellitesForRootResult.FromString,
        )
    self.URLLogSearch = channel.unary_stream(
        '/io.netograph.dset.Dset/URLLogSearch',
        request_serializer=dsetapi_dot_dset__pb2.URLLogSearchRequest.SerializeToString,
        response_deserializer=dsetapi_dot_dset__pb2.URLLogSearchResult.FromString,
        )


class DsetServicer(object):
  """Methods that operate on an individual dataset, either public or private.
  """

  def SubmitCapture(self, request, context):
    """Submit a capture request to a dataset.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CaptureInfo(self, request, context):
    """Retrieve info for a specified capture by ID within a dataset.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CaptureLog(self, request, context):
    """Retrieve the capture log for a dataset, in reverse chronological order.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CertDomainSearch(self, request, context):
    """Retrieve certificates for a specified domain query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CertIPSearch(self, request, context):
    """Retrieve certificates for a specified IP query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DomainHistory(self, request, context):
    """Retrieve the capture history for a specified domain. The
    length of this history is capped at ~100.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DomainSearch(self, request, context):
    """Retrieve the capture log for a specified domain in a dataset.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DomainsForIP(self, request, context):
    """Find all domains in the dataset associated with a given IP address.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IPHistory(self, request, context):
    """Retrieve the capture history for a specified IP in a dataset. The
    length of this history is capped at ~100.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IPLogSearch(self, request, context):
    """Search the dataset log for captures that contain a given IP.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IPSearch(self, request, context):
    """Find all IPs in the dataset that match an address and integer netmask.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IPsForDomain(self, request, context):
    """Find all IPs in a dataset associated with a given domain.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetaForCapture(self, request, context):
    """Get metadata associated with a specified capture within a dataset.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetaSearch(self, request, context):
    """Search the dataset log for captures matching a metadata query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PoliciesForRoot(self, request, context):
    """Find all policies for a specified domain query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PolicyDomainCaptures(self, request, context):
    """Retrieve the policy capture log for a domain query, in reverse chronological order.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PolicyDomainStats(self, request, context):
    """Retrieve statistics for a policy domain query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PolicyURLCaptures(self, request, context):
    """Retrieve the policy capture log for specific policy URL, in reverse chronological order.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RedirsByDestination(self, request, context):
    """Find all redirections in the dataset for a given destination domain query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RedirsBySource(self, request, context):
    """Find all redirections in the dataset for a given source domain query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RootLogSearch(self, request, context):
    """Search the dataset log for captures where any root domain matches a given query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RootsForSatellite(self, request, context):
    """Find all roots in a dataset that are associated with a given satellite query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SatelliteLogSearch(self, request, context):
    """Search the dataset log for captures where any satellite domain matches a given query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SatellitesForRoot(self, request, context):
    """Find all satellites in the dataset that are associated with a given root query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def URLLogSearch(self, request, context):
    """Search the dataset log for captures where any root URL matches a given URL query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DsetServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubmitCapture': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitCapture,
          request_deserializer=dsetapi_dot_dset__pb2.SubmitCaptureRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.SubmitCaptureResult.SerializeToString,
      ),
      'CaptureInfo': grpc.unary_unary_rpc_method_handler(
          servicer.CaptureInfo,
          request_deserializer=dsetapi_dot_dset__pb2.CaptureInfoRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.CaptureInfoResult.SerializeToString,
      ),
      'CaptureLog': grpc.unary_stream_rpc_method_handler(
          servicer.CaptureLog,
          request_deserializer=dsetapi_dot_dset__pb2.CaptureLogRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.CaptureLogResult.SerializeToString,
      ),
      'CertDomainSearch': grpc.unary_stream_rpc_method_handler(
          servicer.CertDomainSearch,
          request_deserializer=dsetapi_dot_dset__pb2.CertDomainSearchRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.CertDomainSearchResult.SerializeToString,
      ),
      'CertIPSearch': grpc.unary_stream_rpc_method_handler(
          servicer.CertIPSearch,
          request_deserializer=dsetapi_dot_dset__pb2.CertIPSearchRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.CertIPSearchResult.SerializeToString,
      ),
      'DomainHistory': grpc.unary_stream_rpc_method_handler(
          servicer.DomainHistory,
          request_deserializer=dsetapi_dot_dset__pb2.DomainHistoryRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.DomainHistoryResult.SerializeToString,
      ),
      'DomainSearch': grpc.unary_stream_rpc_method_handler(
          servicer.DomainSearch,
          request_deserializer=dsetapi_dot_dset__pb2.DomainSearchRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.DomainSearchResult.SerializeToString,
      ),
      'DomainsForIP': grpc.unary_stream_rpc_method_handler(
          servicer.DomainsForIP,
          request_deserializer=dsetapi_dot_dset__pb2.DomainsForIPRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.DomainsForIPResult.SerializeToString,
      ),
      'IPHistory': grpc.unary_stream_rpc_method_handler(
          servicer.IPHistory,
          request_deserializer=dsetapi_dot_dset__pb2.IPHistoryRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.IPHistoryResult.SerializeToString,
      ),
      'IPLogSearch': grpc.unary_stream_rpc_method_handler(
          servicer.IPLogSearch,
          request_deserializer=dsetapi_dot_dset__pb2.IPLogSearchRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.IPLogSearchResult.SerializeToString,
      ),
      'IPSearch': grpc.unary_stream_rpc_method_handler(
          servicer.IPSearch,
          request_deserializer=dsetapi_dot_dset__pb2.IPSearchRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.IPSearchResult.SerializeToString,
      ),
      'IPsForDomain': grpc.unary_stream_rpc_method_handler(
          servicer.IPsForDomain,
          request_deserializer=dsetapi_dot_dset__pb2.IPsForDomainRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.IPsForDomainResult.SerializeToString,
      ),
      'MetaForCapture': grpc.unary_stream_rpc_method_handler(
          servicer.MetaForCapture,
          request_deserializer=dsetapi_dot_dset__pb2.MetaForCaptureRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.MetaForCaptureResult.SerializeToString,
      ),
      'MetaSearch': grpc.unary_stream_rpc_method_handler(
          servicer.MetaSearch,
          request_deserializer=dsetapi_dot_dset__pb2.MetaSearchRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.MetaSearchResult.SerializeToString,
      ),
      'PoliciesForRoot': grpc.unary_stream_rpc_method_handler(
          servicer.PoliciesForRoot,
          request_deserializer=dsetapi_dot_dset__pb2.PoliciesForRootRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.PoliciesForRootResult.SerializeToString,
      ),
      'PolicyDomainCaptures': grpc.unary_stream_rpc_method_handler(
          servicer.PolicyDomainCaptures,
          request_deserializer=dsetapi_dot_dset__pb2.PolicyDomainCapturesRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.PolicyDomainCapturesResult.SerializeToString,
      ),
      'PolicyDomainStats': grpc.unary_unary_rpc_method_handler(
          servicer.PolicyDomainStats,
          request_deserializer=dsetapi_dot_dset__pb2.PolicyDomainStatsRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.PolicyDomainStatsResult.SerializeToString,
      ),
      'PolicyURLCaptures': grpc.unary_stream_rpc_method_handler(
          servicer.PolicyURLCaptures,
          request_deserializer=dsetapi_dot_dset__pb2.PolicyURLCapturesRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.PolicyURLCapturesResult.SerializeToString,
      ),
      'RedirsByDestination': grpc.unary_stream_rpc_method_handler(
          servicer.RedirsByDestination,
          request_deserializer=dsetapi_dot_dset__pb2.RedirsByDestinationRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.RedirsByDestinationResult.SerializeToString,
      ),
      'RedirsBySource': grpc.unary_stream_rpc_method_handler(
          servicer.RedirsBySource,
          request_deserializer=dsetapi_dot_dset__pb2.RedirsBySourceRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.RedirsBySourceResult.SerializeToString,
      ),
      'RootLogSearch': grpc.unary_stream_rpc_method_handler(
          servicer.RootLogSearch,
          request_deserializer=dsetapi_dot_dset__pb2.RootLogSearchRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.RootLogSearchResult.SerializeToString,
      ),
      'RootsForSatellite': grpc.unary_stream_rpc_method_handler(
          servicer.RootsForSatellite,
          request_deserializer=dsetapi_dot_dset__pb2.RootsForSatelliteRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.RootsForSatelliteResult.SerializeToString,
      ),
      'SatelliteLogSearch': grpc.unary_stream_rpc_method_handler(
          servicer.SatelliteLogSearch,
          request_deserializer=dsetapi_dot_dset__pb2.SatelliteLogSearchRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.SatelliteLogSearchResult.SerializeToString,
      ),
      'SatellitesForRoot': grpc.unary_stream_rpc_method_handler(
          servicer.SatellitesForRoot,
          request_deserializer=dsetapi_dot_dset__pb2.SatellitesForRootRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.SatellitesForRootResult.SerializeToString,
      ),
      'URLLogSearch': grpc.unary_stream_rpc_method_handler(
          servicer.URLLogSearch,
          request_deserializer=dsetapi_dot_dset__pb2.URLLogSearchRequest.FromString,
          response_serializer=dsetapi_dot_dset__pb2.URLLogSearchResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'io.netograph.dset.Dset', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
