from django.db import models
from django.urls import reverse



class ProductCategory(models.Model):
    title = models.CharField(max_length=300 , verbose_name='title' , db_index=True)
    url_title = models.CharField(max_length=300 , verbose_name='url title' , db_index=True)
    is_active = models.BooleanField(verbose_name='active / inactive')

    def __str__(self) -> str:
        super(ProductCategory , self).__str__()
        return "{0} {1}".format(self.title , self.url_title)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"



class ProductBrand(models.Model):
    title = models.CharField(max_length=300 , verbose_name="brand name" , db_index=True)
    is_active = models.BooleanField(verbose_name="active / inactive")

    def __str__(self) -> str:
        super(ProductBrand , self).__str__()
        return self.title

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"



class Product(models.Model):
    title = models.CharField(max_length=300 , verbose_name='title')
    category = models.ManyToManyField(to=ProductCategory , related_name='category' , verbose_name='category')
    image = models.ImageField(upload_to='images/products' , null=True , blank=True , verbose_name='Product Picture')
    brand = models.ForeignKey(to=ProductBrand , on_delete=models.CASCADE , verbose_name="brand" , null=True , blank=True)
    price = models.IntegerField(verbose_name='price')
    short_description = models.CharField(max_length=300 , db_index=True , null=True , verbose_name='short description')
    description = models.TextField(verbose_name='description' , db_index=True)
    is_active = models.BooleanField(default=False , verbose_name='active / inactive')
    slug = models.SlugField(max_length=200 , default="" , null=False , blank=True , db_index=True , unique=True , verbose_name='url title')
    is_delete = models.BooleanField(verbose_name='deleted / not deleted')

    def get_absolute_url(self):
        return reverse(viewname='product_detail' , args=[self.id])

    def save(self , *args , **kwargs):
        super().save(*args , **kwargs)

    def __str__(self) -> str:
        super(Product , self).__str__()
        return "{0} {1}".format(self.title , self.price)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"



class ProductTag(models.Model):
    caption = models.CharField(max_length=200 , verbose_name='tag' , db_index=True)
    product = models.ForeignKey(to=Product , on_delete=models.CASCADE , related_name='product_tags')

    class Meta:
        verbose_name = "Product Tag"
        verbose_name_plural = "Product Tags"

    def __str__(self) -> str:
        super(ProductTag , self).__str__()
        return self.caption