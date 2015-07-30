from django.forms import BaseForm

__all__ = ["ErrorsOnFirstFieldMixin"]


class ErrorsOnFirstFieldMixin(object):

    def add_error(self, field, error):
        """
        Adds non field errors to the first field of the form.
        """
        if field is None and len(self.fields) > 0:
            field = list(self.fields)[0]

        super(ErrorsOnFirstFieldMixin, self).add_error(field, error.messages[0])