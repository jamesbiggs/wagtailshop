from uuid import uuid4

from django.db import models

from wagtail.models import Page, ParentalKey
from wagtail.admin.panels import FieldPanel, MultipleChooserPanel

class ShopCategoryPage(Page):
    

    parent_page_types = ["shop.ShopIndexPage"]
    subpage_types = ["shop.ShopCategoryPage", "shop.ShopProductPage"]
    

class ShopProductPage(Page):
    product_id = models.UUIDField("UUID", unique=True, default=uuid4, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    display_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("price"),
        FieldPanel("description"),
        FieldPanel("display_image"),
        MultipleChooserPanel("product_images", label="Product Images", chooser_field_name="image"),
    ]

    parent_page_types = ["shop.ShopCategoryPage"]
    subpage_types = []
    template = "shop/shop_product_page.html"


class ProductImage(models.Model):
    page = ParentalKey(ShopProductPage, on_delete=models.CASCADE, related_name='product_images')
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.CASCADE,
        related_name="+",
    )
    caption = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]

    def __str__(self):
        return self.image.title

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

class ShopIndexPage(Page):
    pass
