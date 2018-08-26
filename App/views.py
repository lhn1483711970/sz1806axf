import hashlib
import random

from PIL import Image, ImageDraw, ImageFont
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from App.models import axf_wheel, axf_nav, axf_mustbuy, axf_shop, axf_mainshow, axf_foodtypes, axf_goods, member, \
    role_member, auth_role, axf_shopcar


def home(request):

    wheels = axf_wheel.objects.all()

    navs = axf_nav.objects.all()

    mustbuys =axf_mustbuy.objects.all()

    shops = axf_shop.objects.all()
    # for shop in shops:
    #     print(shop.name)
    shop1 = shops[0]
    shop2 = shops[1:3]
    shop3 = shops[3:7]
    shop4 = shops[7:11]

    mainshows = axf_mainshow.objects.all()

    # for am in mainshows:
    #     print(am.name)
    data ={
        'title':'主页',
        'wheels':wheels,
        'navs': navs,
        'mustbuys':mustbuys,
        'shop1':shop1,
        'shop2':shop2,
        'shop3':shop3,
        'shop4':shop4,
        'mainshows':mainshows

    }

    return render(request,'home.html',data)


def market(request):
    #如果没有传值过来 就默认是热销榜 0
    typeid = request.GET.get('typeid') if request.GET.get('typeid') else '104749'
    childid = request.GET.get('childid') if request.GET.get('childid') else '0'
    sort = request.GET.get('sort') if request.GET.get('sort') else '0'

    foodtypes = axf_foodtypes.objects.all()

    flist =[]
    for fdt in foodtypes.filter(typeid = typeid):
        fts = fdt.childtypenames.split("#")

        for ft in fts:
            flist.append(ft.split(':'))
        print(flist)

    goodlist = axf_goods.objects.filter(categoryid= typeid)
    for goods in goodlist:
        print(goods.id)

    if childid !='0':
        goodlist = goodlist.filter(childcid = childid)
        #根据排序方式进行·排序
    if sort == '1':
        goodlist = goodlist.order_by('productid')
    elif sort == '2':
        goodlist = goodlist.order_by('price')
    elif sort == '3':
        goodlist = goodlist.order_by('-price')

    data ={'foodtypes':foodtypes,
           'typeid':typeid,
           'goodlist':goodlist,
           'flist':flist,
           'childid':childid,
           'sort':sort,

           }
    return render(request, 'market.html', data)

def shopcar(request):
    # nav = axf_nav.objects.all()
    data = {
        'title': '购物车',
        # 'nav': nav,
    }
    return render(request, 'shopcar.html', data)


def mine(request):
    # nav = axf_nav.objects.all()
    data = {
        'title': '我的',
        # 'nav': nav,
    }
    return render(request, 'mine.html', data)

def regist(request):

    if request.method == 'GET':
       return render(request,'regist.html')


    name = request.POST.get('name')
    password  = request.POST.get('password')
    print(password)

    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    password = md5.hexdigest()
    print(password)

    meb = member()
    meb.mname = name
    meb.password = password
    meb.save()
    return HttpResponse('注册成功')


#用户名预校验
def regist_jyname(request):
    name =request.POST.get('name')
    meb = member.objects.filter(mname = name).first()
    data = {}
    if meb:

        data={'result':'0001'}
    else:
        data={'result':'0000'}

    return JsonResponse(data)

#登录
def login(request):
    if request.method =='GET':
       return render(request,'login.html')

    name = request.POST.get('name')
    password = request.POST.get('password')

    md5 =hashlib.md5()
    md5.update(password.encode('utf-8'))
    password = md5.hexdigest()

    code = request.POST.get('code')

    sessioncode = request.session.get('code')

    if code != sessioncode:
        return render(request,'login.html',{'msg':'验证码错误'})

    #根据用户名查询用户是否存在
    temp = member.objects.filter(mname = name).first()

    if temp:

        if password == temp.password:

            #
            #根据用户去查询权限
            mem_roles = role_member.objects.filter(member_id =temp.id)
            auths = set()
            #根据角色查询权限（去重）
            for mr in mem_roles:
                role_auths = auth_role.objects.filter(role_id= mr.role.id)

                for auth in role_auths:  #所有用户权限信息
                    auths.add(auth.auth.apath)

            request.session['auths'] = str(auths)
            request.session['mname'] = temp.mname
            request.session['memberid'] = temp.id

            # return HttpResponse('登录成功')
            return HttpResponseRedirect('/market/')




    return render(request,'login.html',{'msg':'用户名或者密码错误'})


def yzcode(request):

    #1: 有一张画布
    iamge = Image.new('RGB',(100,38),randomcolor())

    #２：　有一支画笔　　画笔和画布需要绑定
    imageDraw = ImageDraw.Draw(iamge)

    #指定一下字体
    imagefont = ImageFont.truetype('static/fonts/ADOBEARABIC-BOLD.OTF',25)

    strs = '1234567890qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ'

    code = ''
    for i in range(4):

        index = random.randrange(len(strs))
        imageDraw.text((5+i*22, random.randrange(3, 20)), strs[index], fill=randomcolor(), font=imagefont)
        code += strs[index]

    #在画布上面画３００个点
    for ie in range(300):
        imageDraw.point(randomxy(),fill=randomcolor())


    #需要将画好的验证码，保存到ｓｅｓｓｉｏｎ里面。
    request.session['code'] = code
    print(code)

    #３：　作画

    # imageDraw.text((29, random.randrange(10,35)), 't', fill=randomcolor(), font=imagefont)
    # imageDraw.text((53, random.randrange(10,35)), 'u', fill=randomcolor(), font=imagefont)
    # imageDraw.text((79, random.randrange(10,35)), 'm', fill=randomcolor(), font=imagefont)

    #４：　输出到前台
    import  io
    #获取ｂｙｔｅｓｉｏ流
    ib = io.BytesIO()
    #将图片保存到这个流里面
    iamge.save(ib,'png')

    #通过ｉｏ流将图片输出到前台，以图片的格式
    return HttpResponse(ib.getvalue(),'image/png')

def randomxy():
    x = random.randrange(100)
    y = random.randrange(38)

    return (x,y)

def randomcolor():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)

    return (r,g,b)

def addshopcar(request):
    goodsid = request.POST.get('goodsid')
    memberid = request.POST.get('memberid')
    # isselect = request.POST.get('isslect')

    number = request.POST.get('number') if request.POST.get('number') else 1

    scar = axf_shopcar.objects.filter(goodsid_id =goodsid).first()
    #如果购物车已经存在 数量加1
    if scar:
        scar.number += number
        scar.save()
    # 如果不存在 就往购物车中添加一条数据
    else:
        scar = axf_shopcar()
        scar.goodsid_id = goodsid
        scar.memberid_id = memberid

       #保存到数据库中
    scar.save()

    return JsonResponse({'result':'0000','number':scar.number})




    pass
def subshopcar(request):
    pass
def selshopcar(request):
    pass
