from wagtail.core import blocks


class HeadingBlock(blocks.CharBlock):
    class Meta:
        template = 'blocks/heading.html'
