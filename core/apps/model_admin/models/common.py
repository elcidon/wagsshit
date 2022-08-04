import uuid

from django.db import models


class CommonInfo(models.Model):
    #TODO: Remover esse todo
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Modificado em", auto_now=True)

    class Meta:
        abstract = True
