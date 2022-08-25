from typing import Any, Dict, List

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context, Template


DATA = {
    "name": "Jezebel",
    "best_songs": [
        {"name": "Jezebel"},
        {"name": "Cassie Eats Cockroaches"},
        {"name": "The Blue"},
        {"name": "Dr. Seuss is dead"}
    ]
}


@receiver(
    post_save,
    sender="acid_bath.AcidBath",
    dispatch_uid="acid_bath_post_save",
)
def acid_bath_post_save(sender, instance, **kwargs):

    content = instance.content
    template = Template(content)
    context = Context(DATA)

    with open("output.html", "w") as f:
        f.write(template.render(context))
