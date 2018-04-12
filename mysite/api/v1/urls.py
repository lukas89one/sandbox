from django.conf.urls import url
from django.urls import include

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api.v1.polls.views import QuestionViewSet, VoteViewSet
from api.v1.snippets.views import SnippetViewSet
from api.v1.users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'snippets', SnippetViewSet)
router.register(r'polls/questions', QuestionViewSet)
router.register(r'polls/vote', VoteViewSet)

schema_view = get_schema_view(title='Mysite API')

app_name = 'mysite'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view, name='schema'),
]
