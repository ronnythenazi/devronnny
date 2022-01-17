#https://youtu.be/ULYrOrTNczs  #dynamic links
#https://www.geeksforgeeks.org/update-view-function-based-views-django/ update view
#http://www.learningaboutelectronics.com/Articles/How-to-retrieve-all-objects-of-a-database-table-in-Django.php #retruve all objects
#https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi #create a simple blog, full tutorial, including aythonitcation, and
#mulitply ckeditors with different height property https://stackoverflow.com/questions/11124182/how-to-set-up-ckeditor-for-multiple-instances-with-different-heights
#judonazim-z6fn3.ondigitalocean.app
# generate random password django python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

#https://stackoverflow.com/questions/9430770/django-error-importing-storages-backends
#https://stackoverflow.com/questions/60765418/can-i-use-digital-ocean-spaces-for-user-uploaded-files-with-django
#https://www.youtube.com/watch?v=FjWbMNw6Wk0 34 - Deploy Django to Digital Ocean App Platform - Python & Django 3.2 Tutorial Series

#https://sayari3.com/articles/19-django-digitalocean-spaces-tutorial/1
#https://stackoverflow.com/questions/41329858/how-to-delete-an-imagefield-image-in-a-django-model remove image from db
#https://stackoverflow.com/questions/14351048/django-optional-url-parameters

#login using either email or username
#https://stackoverflow.com/questions/25316765/log-in-user-using-either-email-address-or-username-in-django/57138652

#notification tutorial
#https://youtu.be/_JKWYkz597c



"""
Inline formsets¶
class models.BaseInlineFormSet¶
Inline formsets is a small abstraction layer on top of model formsets. These simplify the case of working with related objects via a foreign key. Suppose you have these two models:

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
If you want to create a formset that allows you to edit books belonging to a particular author, you could do this:

>>> from django.forms import inlineformset_factory
>>> BookFormSet = inlineformset_factory(Author, Book, fields=('title',))
>>> author = Author.objects.get(name='Mike Royko')
>>> formset = BookFormSet(instance=author)




<form method="post">
    {{ formset.management_form }}
    {% for form in formset %}
        {{ form.id }}
        <ul>
            <li>{{ form.name }}</li>
            <li>{{ form.age }}</li>
        </ul>
    {% endfor %}
</form>

>> instances = formset.save(commit=False)
>>> for obj in formset.deleted_objects:
...     obj.delete()

<form method="post">
    {{ formset.management_form }}
    {% for form in formset %}
        <ul>
            <li>{{ form.title }}</li>
            <li>{{ form.pub_date }}</li>
            {% if formset.can_delete %}
                <li>{{ form.DELETE }}</li>
            {% endif %}
        </ul>
    {% endfor %}
</form>

from django.forms import formset_factory
>>> from myapp.forms import ArticleForm
>>> ArticleFormSet = formset_factory(ArticleForm, can_delete=True) #can_order = true

from django.forms import modelformset_factory
from django.shortcuts import render
from myapp.models import Author

def manage_authors(request):
    AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
    if request.method == "POST":
        formset = AuthorFormSet(
            request.POST, request.FILES,
            queryset=Author.objects.filter(name__startswith='O'),
        )
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset = AuthorFormSet(queryset=Author.objects.filter(name__startswith='O'))
    return render(request, 'manage_authors.html', {'formset': formset})



dynamically-adding-a-form-to-a-django-formset
    https://stackoverflow.com/questions/501719/dynamically-adding-a-form-to-a-django-formset

How to dynamically delete object using django formset
https://stackoverflow.com/questions/47954063/how-to-dynamically-delete-object-using-django-formset

work-with-ajax-django
https://www.pluralsight.com/guides/work-with-ajax-django


html inputfile

https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file
"""
