from django.db.models import (
    Model,
    DateTimeField,
    BooleanField,
)


class CommonBaseModel(Model):
    """
    this is an abstract model
    We inherit this table for most of our tables to add latest created and updated in table
    is_deleted is a property when we dont want to actually delete something and we just
        dont want to show it to the user
    """

    created_date = DateTimeField(
        auto_now_add=True,
    )
    updated_date = DateTimeField(
        auto_now=True,
    )
    is_deleted = BooleanField(
        default=False,
    )
    is_active = BooleanField(
        default=True,
    )

    class Meta:
        abstract = True

    def safe_delete(self):
        self.is_active = False
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):
        if self.is_deleted:
            self.is_active = False
        super().save(*args, **kwargs)