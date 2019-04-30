from rest_framework.renderers import JSONRenderer, BaseRenderer
from rest_framework.status import HTTP_204_NO_CONTENT


class UserAppJsonRenderer(JSONRenderer, BaseRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):

        if len(data) == 1:
            data = data[0:1][0]
            data = {'user': data}

        elif len(data) > 1:
            data = {'users': data}

        else:
            data = None
            renderer_context['response'].status_code = HTTP_204_NO_CONTENT

        return super(UserAppJsonRenderer, self).render(data, accepted_media_type, renderer_context)
