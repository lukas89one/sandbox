from rest_framework import serializers

from polls.models import Question, Choice


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    vote = serializers.HyperlinkedIdentityField(view_name='api:v1:choice-vote')

    class Meta:
        model = Choice
        fields = ('choice_text', 'votes', 'vote',)
        read_only = ('votes',)


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    choices = ChoiceSerializer(many=True, required=True)

    class Meta:
        model = Question
        fields = ('url', 'owner', 'question_text', 'pub_date', 'was_published_recently', 'choices')
        read_only = ('was_published_recently', 'owner',)
        extra_kwargs = {
            'url': {'view_name': 'api:v1:question-detail'}
        }

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)

        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)

        return question
