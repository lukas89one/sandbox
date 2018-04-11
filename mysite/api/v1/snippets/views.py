from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, renderers, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.core.renderers import PyRenderer
from snippets.models import Snippet
from api.v1.core.permissions import IsOwnerOrReadOnly
from api.v1.snippets.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filter_fields = ('title', 'language')
    search_fields = ('code',)
    ordering_fields = ('title', 'language', 'style',)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer, PyRenderer])
    def highlight(self, request, *args, **kwargs):
        format = kwargs.pop('format', 'html')
        snippet = self.get_object()

        if format == 'html':
            return Response(snippet.highlighted)
        else:
            return Response(f'{snippet.title}\n\n{snippet.code}')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
