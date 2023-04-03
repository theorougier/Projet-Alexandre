from wagtail.core.blocks import BooleanBlock, StructBlock, StreamBlock, RichTextBlock, TextBlock, IntegerBlock, \
    CharBlock, \
    ChoiceBlock, PageChooserBlock, URLBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock

class Paragraphe(StructBlock):
    text = RichTextBlock(required=False)

    class Meta:
        template = "blocks/paragraphe.html"

class Social_block(StructBlock):
    text = RichTextBlock(required=False)

    class Meta:
        template = "blocks/social_block.html"

class Link_button(StructBlock):
    text = RichTextBlock(required=False)
    link = URLBlock(required=False)

    class Meta:
        template = "blocks/link_button.html"