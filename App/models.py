from django.db import models

# Create your models here.
class base(models.Model):
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True


class axf_wheel(base):

    class Meta:
        db_table = 'axf_wheel'

class axf_nav(base):

    class Meta:
        db_table = 'axf_nav'

class axf_mustbuy(base):

    class Meta:
        db_table = 'axf_mustbuy'

class axf_shop(base):

    class Meta:
        db_table = 'axf_shop'

class axf_mainshow(base):
    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    img1 = models.CharField(max_length=200)
    childcid1= models.CharField(max_length=20)
    productid1= models.CharField(max_length=20)
    longname1= models.CharField(max_length=20)
    price1= models.CharField(max_length=50)
    marketprice1= models.CharField(max_length=50)
    img2= models.CharField(max_length=200)
    childcid2= models.CharField(max_length=20)
    productid2= models.CharField(max_length=20)
    longname2= models.CharField(max_length=200)
    price2= models.CharField(max_length=50)
    marketprice2= models.CharField(max_length=50)
    img3= models.CharField(max_length=200)
    childcid3= models.CharField(max_length=20)
    productid3= models.CharField(max_length=20)
    longname3= models.CharField(max_length=20)
    price3= models.CharField(max_length=50)
    marketprice3= models.CharField(max_length=50)

    class Meta:
        db_table = 'axf_mainshow'


class axf_foodtypes(models.Model):
    typeid= models.CharField(max_length=20)
    typename= models.CharField(max_length=50)
    childtypenames= models.CharField(max_length=200)
    typesort= models.IntegerField()
    class Meta:
        db_table = 'axf_foodtypes'

class axf_goods(models.Model):
    productid= models.CharField(max_length=20)
    productimg= models.CharField(max_length=200)
    productname= models.CharField(max_length=100)
    productlongname= models.CharField(max_length=100)
    isxf= models.IntegerField(default=0)
    pmdesc= models.IntegerField(default=0)
    specifics= models.CharField(max_length=20)
    price= models.DecimalField(max_digits=6,decimal_places=2)
    marketprice= models.DecimalField(max_digits=10,decimal_places=6)
    categoryid=  models.IntegerField()
    childcid=  models.IntegerField()
    childcidname= models.CharField(max_length=20)
    dealerid= models.CharField(max_length=20)
    storenums= models.IntegerField(default=200)
    productnum= models.IntegerField(default=3)


    class Meta:
        db_table = 'axf_goods'


class member(models.Model):

    mname = models.CharField(max_length=20)
    password = models.CharField(max_length=32)


class role(models.Model):

    rname = models.CharField(max_length=20)
    rdesc = models.CharField(max_length=20)

class role_member(models.Model):
    member = models.ForeignKey(member,on_delete=models.PROTECT)
    role = models.ForeignKey(role,on_delete=models.PROTECT)

class auth(models.Model):
    aname = models.CharField(max_length=20)
    apath = models.CharField(max_length=100)

    fid = models.IntegerField()


class auth_role(models.Model):

    auth = models.ForeignKey(auth,on_delete=models.PROTECT)
    role = models.ForeignKey(role,on_delete=models.PROTECT)



class axf_shopcar(models.Model):

    memberid = models.ForeignKey(member,on_delete=models.CASCADE)
    goodsid = models.ForeignKey(axf_goods,on_delete=models.CASCADE)

    number = models.IntegerField(default=1)
    isselect = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_shopcar'




