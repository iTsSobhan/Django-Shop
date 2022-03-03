from django.db import models




class ArticleCategory(models.Model):
    parent = models.ForeignKey(to='ArticleCategory' , null=True , blank=True , on_delete=models.CASCADE , verbose_name='Parent Category')
    title = models.CharField(max_length=200 , verbose_name='Title')
    url_title = models.CharField(max_length=200 , unique=True , verbose_name='URL Title')
    is_active = models.BooleanField(default=True , verbose_name='Active / Inactive')
    
    def __str__(self) -> str:
        super(ArticleCategory , self).__str__()
        return self.title
    
    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'
        
        
        
        

class Article(models.Model):
    title = models.CharField(max_length=300 , verbose_name='Title')
    slug = models.SlugField(max_length=400 , db_index=True , allow_unicode=True , verbose_name='URL Title')
    image = models.ImageField(upload_to='images/articles' , verbose_name='Article Image')
    short_description = models.TextField(verbose_name='Short Description')
    text = models.TextField(verbose_name='Text')
    is_active = models.BooleanField(verbose_name='Active / Inactive' , default=True)
    selected_categories = models.ManyToManyField(to=ArticleCategory , verbose_name='Categories')
    
    def __str__(self) -> str:
        super(Article , self).__str__()
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'