from django.db import models

# Create your models here.

STATUS = (('active','active'),('inactivate','inactivate'))
STOCK = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
LABELS = (('new','new'),('hot','hot'),('sale','sale'),('','default'))
class Category(models.Model):
	title = models.CharField(max_length = 300)
	description = models.TextField(blank = True)
	slug = models.CharField(max_length = 500)
	image = models.TextField(blank = True)

	def __str__(self):
		return self.title


class SubCategory(models.Model):
	title = models.CharField(max_length = 300)
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	description = models.TextField(blank = True)
	slug = models.CharField(max_length = 500)
	image = models.TextField(blank = True)

	def __str__(self):
		return self.title


class Brand(models.Model):
	title = models.CharField(max_length = 300)
	description = models.TextField(blank = True)
	slug = models.CharField(max_length = 500)
	image = models.TextField(blank = True,null = True)

	def __str__(self):
		return self.title

class Item(models.Model):
	title = models.CharField(max_length=400)
	slug = models.CharField(max_length=500)
	price = models.IntegerField()
	discounted_price = models.IntegerField()
	description = models.TextField()
	image = models.ImageField(upload_to = 'media')
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	subcategory = models.ForeignKey(SubCategory,on_delete = models.CASCADE)
	status = models.CharField(max_length=40,choices =STATUS,blank = True)
	stock = models.CharField(max_length = 50,choices = STOCK,blank = True)
	labels = models.CharField(max_length=30,choices=LABELS,blank = True)

	def __str__(self):
		return self.title


class Ad(models.Model):
	name = models.CharField(max_length=200)
	rank = models.IntegerField()
	image = models.ImageField(upload_to = 'media')
	description = models.TextField(blank = True)

	def __str__(self):
		return self.name

class Slider(models.Model):
	name = models.CharField(max_length = 200)
	rank = models.IntegerField()
	image = models.ImageField(upload_to = 'media',null = True)
	status = models.CharField(choices =STATUS,default = False,max_length = 30)
	description = models.TextField(blank = True)

	def __str__(self):
		return self.name