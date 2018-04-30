from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.core.permissions import IsOwnerOrReadOnly
from api.v1.polls.serializers import QuestionSerializer, ChoiceSerializer
from polls.models import Question, Choice


class QuestionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    retrieve:
    Return the given question.

    list:
    Return a list of all questions created by current user.

    create:
    Create a new question.

    update:
    Update the given question.

    destroy:
    Delete the given question.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteViewSet(viewsets.GenericViewSet):
    """
    This viewset provides `vote` action.

    vote:
    Vote for given choice for given question. Allowed only one vote per user per day.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    throttle_scope = 'voters'

    @action(detail=True)
    def vote(self, request, *args, **kwargs):
        choice = self.get_object()
        choice.vote()

        return Response(f'You voted for "{choice}"')
