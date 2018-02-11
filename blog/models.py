from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User
from comments.models import Comment
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from markdown_deux import markdown

# Create your models here.




class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title=models.CharField(max_length=120)
    image=models.ImageField(null=True,blank=True,
                            width_field="width_field",
                            height_field="height_field")

    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    content=models.TextField()
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail",kwargs={"id":self.id})

    def get_api_url(self):
        return reverse("posts-api:detail",kwargs={"id":self.id})

    class Meta:
        ordering=["-timestamp","-updated"]

    def get_markdown(self):
        content=self.content
        markdown_text=markdown(content)
        return mark_safe(markdown_text)

    @property
    def comments(self):
        instance=self
        qs=Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type




