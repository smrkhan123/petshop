from django.shortcuts import render,redirect
import smtplib
from django.contrib.auth.models import User,auth
# Create your views here.
from . models import Pet,Cart,Orders
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm




usern=''
c=[]
def cart(request,id):
	Car=Cart.objects.all()
	count=Car.count()
	c.append(count)
	print(c)
	print(count)
	pr=Pet.objects.get(pk=id)
	cart=Cart()
	cart.name=pr.name
	cart.color=pr.color
	cart.category=pr.category
	cart.breed=pr.breed
	cart.price=pr.price
	cart.age=pr.age
	cart.Image=pr.Image
	cart.pub_date=pr.pub_date
	if request.user.is_authenticated:
		cart.usern=request.user.username
		cart.save()
		return redirect('index')

	return render(request,'cart.html')



def cartitem(request):
	car=Cart.objects.all()
	a=car.count()
	for i in car:
		b=i.name
		print(b)
	print(a)
	sum=0
	for i in car:
		print(i.price)
		sum=sum+i.price
	print('Total: ',sum)
	return render(request,'cartitem.html',{'cart':car,'total':sum,'cartt':a})



def index(request):
	pet=Pet.objects.all()
	cart=Cart.objects.all()
	car=cart.count()
	list=[]
	print()
	c=0
	d=0
	for i in pet:
		if i.category=='dog':
			c=c+1
			if c<3:
				list.append(i)
		elif i.category=="cat":
			d=d+1
			if d<3: 
				list.append(i)
	return render(request,'index.html',{'pet':list,'cartt':car})
def about(request):
	cart=Cart.objects.all()
	car=cart.count()
	return render(request,'about.html',{'cartt':car})
def blog(request):
	cart=Cart.objects.all()
	car=cart.count()
	return render(request,'blog.html',{'cartt':car})
def contact(request):
	cart=Cart.objects.all()
	car=cart.count()
	return render(request,'contact.html',{'cartt':car})
def petguide(request):
	cart=Cart.objects.all()
	car=cart.count()
	return render(request,'petguide.html',{'cartt':car})
def petmart(request):
	cart=Cart.objects.all()	
	car=cart.count()
	return render(request,'petmart.html',{'cartt':car})
def dog(request):
	cart=Cart.objects.all()	
	car=cart.count()
	dog = Pet.objects.all()
	print(dog)
	b=0
	g=0
	l=0
	a=0
	c=0
	list=[]
	for i in dog:
		if i.breed=='bulldog':
			if b<1:
				b=b+1
				list.append(i)
			else:
				pass
		elif i.breed=='german_shepherd':
			if g<1:
				g=g+1
				list.append(i)
			else:
				pass
		elif i.breed=='labrador':
			if l<1:
				l=l+1
				list.append(i)
			else:
				pass
		print(list)

		# elif i.category=='bulldog':
		# 	if b<2:
		# 		b=b+1
		# 		list.append(i)
		# 	else:
		# 		break
		# elif i.category=='bulldog':
		# 	if b<2:
		# 		b=b+1
		# 		list.append(i)
		# 	else:
		# 		break

	return render(request,'dog.html',{'dog':list,'cartt':car})
def cat(request):
	cart=Cart.objects.all()
	car=cart.count()
	return render(request,'cat.html',{'cartt':car})
def myaccount(request):
	return render(request,'myaccount.html')
def register(request):
	if request.method=="POST":
		first_name=request.POST['firstname']
		last_name=request.POST['lastname']
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		confirm_password=request.POST['confirmpassword']
		if password==confirm_password:
			if User.objects.filter(username=username).exists():
				messages.error(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.error(request,'Email Taken')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
				user.save();
				messages.success(request,'Account Created Successfully')
				return redirect('login')
		else:
			message.error(request,'Password & Confirm Password Are Not Matching')
			return redirect('register')
	else:
		return render(request,'register.html')
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else:
			messages.error(request,"Username or Password is Incorrect")
			return redirect('login')
	return render(request,'login.html')
def logout(request):
	auth.logout(request)
	return redirect('index')


def breed(request,id):
	cart=Cart.objects.all()
	car=cart.count()
	pet=Pet.objects.get(pk=id)
	print(pet.breed)
	breed=pet.breed
	l=[]
	dog=Pet.objects.all()
	for i in dog:
		if i.breed==pet.breed:
			l.append(i)
	print(l)
	return render(request,'breed.html',{'dog':l,'cartt':car,'breed':breed})

def view(request,id):
	cart=Cart.objects.all()
	car=cart.count()
	pet=Pet.objects.get(pk=id)
	return render(request,'view.html',{'pet':pet,'cartt':car})

def change_password(request):
	if request.method=="POST":
		form=PasswordChangeForm(request.user,request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'Your password was Successfully changed')
			return redirect('login')
		else:
			message.error(request,'Please correct the error below')
	else:
		form= PasswordChangeForm(request.user)
	return render(request,'change_password.html',{'form':form})



def allpet(request):
	dog=Pet.objects.all()
	return render(request,'allpet.html',{'dog':dog})
def deletepet(request,id):
	pet=Pet.objects.get(pk=id)
	pet.delete();
	return redirect('allpet')

def addpet(request):
	if request.method=="POST":
		pet=Pet()
		pet.name=request.POST['name']
		pet.category=request.POST['category']
		pet.breed=request.POST['breed']
		pet.color=request.POST['color']
		pet.price=request.POST['price']
		pet.pub_date=request.POST['pub_date']
		pet.Image=request.FILES['image']
		pet.save()
		return redirect('allpet')
	return render(request,'addpet.html')

def editpet(request,id):
	pet=Pet.objects.get(pk=id)
	if request.method=="POST":
		pet.name=request.POST['name']
		pet.category=request.POST['category']
		pet.breed=request.POST['breed']
		pet.color=request.POST['color']
		pet.price=request.POST['price']
		pet.pub_date=request.POST['pub_date']
		pet.Image=request.FILES['image']
		pet.save()
		return redirect('allpet')
	return render(request,'editpet.html',{'i':pet})




def deletecartitem(request,id):
	cart=Cart.objects.get(pk=id)
	cart.delete();
	return redirect('cartitem')

def buynow(request,id):
	pr=Cart.objects.get(pk=id)
	a=pr.Image
	if request.method=="POST":
		email=request.POST['email']
		name=request.POST['name']
		print(name)
		address1=request.POST['address1']
		address2=request.POST['address2']
		city=request.POST['city']
		state=request.POST['state']
		zip_code=request.POST['zip_code']
		product_details=pr.name
		order=Orders(email=email,name=name,address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,product_details=product_details)
		order.save()
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login('sk862147@gmail.com','smrkhan123')
		message=f'Hi {name}, Your Order {product_details} Is Successfully Placed. We will Deliver it soon at {address1}, {address2}, {city}, {state}, {zip_code} '
		server.sendmail('sk862147@gmail.com',email,message)
		server.quit()
		pr.delete();
		return redirect('index')
	return render(request,'buynow.html')



def buynow1(request,id):
	tr=Pet.objects.get(pk=id)
	if request.method=="POST":
		email=request.POST['email']
		name=request.POST['name']
		address1=request.POST['address1']
		address2=request.POST['address2']
		city=request.POST['city']
		state=request.POST['state']
		zip_code=request.POST['zip_code']
		product_details=tr.name
		order=Orders(email=email,name=name,address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,product_details=product_details)
		order.save()
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login('sk862147@gmail.com','smrkhan123')
		message=f'Hi {name}, Your Order {product_details} Is Successfully Placed. We will Deliver it soon at {address1}, {address2}, {city}, {state}, {zip_code} '
		server.sendmail('sk862147@gmail.com',email,message)
		server.quit()
		return redirect('index')
	return render(request,'buynow.html')



def buyall(request):
	cart=Cart.objects.all()
	a=cart.count()
	if request.method=='POST':
		email=request.POST['email']
		name=request.POST['name']
		address1=request.POST['address1']
		address2=request.POST['address2']
		city=request.POST['city']
		state=request.POST['state']
		zip_code=request.POST['zip_code']
		pd=[]
		for i in cart:
			email=request.POST['email']
			name=request.POST['name']
			address1=request.POST['address1']
			address2=request.POST['address2']
			city=request.POST['city']
			state=request.POST['state']
			zip_code=request.POST['zip_code']
			product_details=i.name
			pd.append(i.name)
			order=Orders(email=email,name=name,address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,product_details=product_details)
			order.save()
			i.delete()
		print(pd)
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login('sk862147@gmail.com','smrkhan123')
		message=f'Hi {name}, Your Order {pd} Is Successfully Placed. We will Deliver it soon at {address1}, {address2}, {city}, {state}, {zip_code} '
		server.sendmail('sk862147@gmail.com',email,message)
		server.quit()
		return redirect('index')
	return render(request,'buynow.html')
