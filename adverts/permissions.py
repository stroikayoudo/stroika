from django.http import Http404


class FollowerPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)

    def has_permissions(self):
        return self.request.user in [*self.get_object().category3.members.all(),
                                     *self.get_object().category3.parent_category.members.all(),
                                     *self.get_object().category3.parent_category.parent_category.members.all()]
