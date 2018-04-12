from pathlib import Path

from django.contrib.auth.models import User

from snippets.models import Snippet


def do_import(path_to_snippets, username):
    print('Import Started')

    owner = User.objects.get(username=username)

    for s in Path(path_to_snippets).glob('*.py'):
        print('Importing', s)

        with open(s) as f:
            title, *code = f.readlines()

            Snippet.objects.create(
                title=title,
                code=''.join(code),
                owner=owner
            )

        print('Import Finished')
