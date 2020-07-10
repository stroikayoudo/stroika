from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


class FollowerPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return HttpResponseRedirect(reverse('adverts:products',))
        return super().dispatch(request, *args, **kwargs)

    def has_permissions(self):
        return self.request.user in [*self.get_object().category3.members.all(),
                                     *self.get_object().category3.parent_category.members.all(),
                                     *self.get_object().category3.parent_category.parent_category.members.all()]
