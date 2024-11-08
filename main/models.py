from django.db import models
from django.utils.safestring import mark_safe
from uuid import uuid4

# Create your models here.


class BaseModel(models.Model):
    guid = models.UUIDField(default=uuid4, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.guid)
    
    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=512)

    def __str__(self):
        return str(self.title)


class Product(BaseModel):
    thumbnail = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=512)
    description = models.TextField()
    price = models.DecimalField(max_digits=16, decimal_places=8)

    def __str__(self):
        return str(self.title)


IMAGE_SCRIPT = """
<div id="content-{id}">
    <button onclick="() => { document.getElementById('{id}').innerHTML = `<img src='{image}' width='300px' alt='{title}'/>`; }">Watch image for ``{title}``</button>
</div>
"""


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ims')
    content = models.ImageField(upload_to='images/')

    def __str__(self):
        return mark_safe(IMAGE_SCRIPT.format(**{
            'id': self.guid,
            'title': f"Image for {self.product.title}",
            'image': self.content.url
        }))
