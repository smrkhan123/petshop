from django.db import models
from django.utils import timezone
# Create your models here.
class Pet(models.Model):

	Pet_Choice = [
	('dog','DOG'),
	('cat','CAT'),
	]

	Breed_Choice = [
	('labrador','LABRADOR'),
	('bulldog','BULLDOG'),
	('german_shepherd','GERMAN_SHERPHERD'),
	('beagle','BEAGLE'),
	('poodle','POODLE'),
	('exotic_shorthair','EXOTIC SHORTHAIR'),
	('ragdoll','RAGDOLL'),
	('british_shorthair','BRITISH SHORTHAIR'),
	('persian','PERSIAN'),
	('maine_coon','MAINE COON'),
	]

	name = models.CharField(max_length=100,null=True)
	category = models.CharField(max_length=100,choices=Pet_Choice,default='dog')
	breed = models.CharField(max_length=100,choices=Breed_Choice,default='labrador')
	color = models.CharField(max_length=100,null=True)
	price = models.IntegerField(null=True)
	age = models.IntegerField(null=True)
	Image = models.ImageField(upload_to="shop/images",null=True)
	pub_date = models.DateField()

	def __str__(self):
		return self.name




class Cart(models.Model):
	name = models.CharField(max_length=100,null=True)
	#desc = models.CharField(max_length=1000,null=True)
	category = models.CharField(max_length=100,null=True)
	breed = models.CharField(max_length=100,null=True)
	color = models.CharField(max_length=100,null=True)
	price = models.IntegerField(null=True)
	age = models.IntegerField(null=True)
	usern = models.CharField(max_length=100,null=True)
	Image = models.ImageField(upload_to="shop/images",null=True)
	pub_date = models.DateField()



class Orders(models.Model):

	STATE_CHOICES = [
    ('up','UP'),
    ('delhi', 'DELHI'),
    ('mp','MP'),
    ('maharastra','MAHARATRA'),
    ('gujrat','GUJRAT'),
    ('rajasthan','RAJASTHAN'),
    ('punjab','PUNJAB')
    ]
	order_id =models.AutoField(primary_key=True)
	email=models.EmailField(max_length=50,default="")
	name=models.CharField(max_length=100,default="")
	address1=models.CharField(max_length=100,default="")
	address2=models.CharField(max_length=100,default="")
	city=models.CharField(max_length=100,default="")
	state=models.CharField(max_length=100,choices=STATE_CHOICES,default="up")
	zip_code=models.IntegerField(default="")
	product_details=models.CharField(max_length=100,default="")


