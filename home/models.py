from django.db import models
from wagtail.core.blocks import RichTextBlock, TextBlock, PageChooserBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel, ObjectList, TabbedInterface
from wagtail.images.edit_handlers import ImageChooserPanel
from home.blocks import *

from wagtail.models import Page


class HomePage(Page):
    header_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    header_title = RichTextField(features=['h1', 'bold', 'italic', 'center', 'textcolour'], blank=True, null=True)
    header_slogan = RichTextField(blank=True, null=True)
    body = StreamField([
        ('paragraphe', Paragraphe()),
        ('link_button', Link_button()),
        ('social_block', Social_block())
    ])

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('header_logo'),
            FieldPanel('header_title'),
            FieldPanel('header_slogan'),
        ], 'Header'),
       StreamFieldPanel('body')
    ]


class DefaultPage(Page):
    header_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    header_title = RichTextField(features=['h1', 'bold', 'italic', 'center'], blank=True, null=True)
    header_slogan = RichTextField(blank=True, null=True)
    body = StreamField([
        ('paragraphe', Paragraphe()),
        ('link_button', Link_button()),
        ('social_block', Social_block())
    ])

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('header_logo'),
            FieldPanel('header_title'),
            FieldPanel('header_slogan'),
        ], 'Header'),
       StreamFieldPanel('body')
    ]
