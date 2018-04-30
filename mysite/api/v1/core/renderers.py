from rest_framework.renderers import BaseRenderer


class PyRenderer(BaseRenderer):
    """
    Renderer which serializes to TEXT file with .py extension.
    """
    media_type = 'text/plain'
    format = 'py'
    charset = 'utf-8'
    render_style = 'text'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into text, returning a bytestring.
        """

        if data is None:
            return bytes()

        return data
