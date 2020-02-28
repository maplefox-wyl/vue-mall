from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.forms.models import model_to_dict

from .models import *


def index_shop(request):
    return render(request, "index_shop.html")


# Create your views here.
# 增加商品
def add_shop(request):
    if request.method == "GET":
        return render(request, "add_shop.html")
    elif request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
        number = request.POST["number"]
        print(type(number), number)
        price = request.POST["price"]
        print(type(price), price)
        total = str(int(price) * int(number))
        if not id:
            result = {'code': 203, 'error': '请填写商品编号 !'}
            return JsonResponse(result)
        if not name:
            result = {'code': 204, 'error': '请填写商品名称 !'}
            return JsonResponse(result)

        if not number:
            result = {'code': 205, 'error': '请填写商品数量 !'}
            return JsonResponse(result)

        if not price:
            result = {'code': 206, 'error': '请填写商品单价 !'}
            return JsonResponse(result)

        # 检查商品编号是否存在
        old_id = Shop.objects.filter(id=id)
        print("123123123",old_id)
        if old_id:
            result = {'code': 208, 'error': '该商品编号已经存在 !!! '}
            return JsonResponse(result)
        # 查询商品是否存在
        old_name = Shop.objects.filter(name=name)
        if old_name:
            result = {'code': 208, 'error': '该商品名称已经存在 !!! '}
            return JsonResponse(result)
        try:
            Shop.objects.create(id=id, name=name, number=number, price=price)
        except Exception as e:
            print('添加失败')
            result = {'code': 500, 'error': '服务器繁忙 !'}
            return JsonResponse(result)
        # result = {'code': 200, 'name': name}
        return render(request, "index_shop.html")


# 删除商品
def del_shop(request, id):
    ashop = Shop.objects.get(id=id)
    ashop.delete()
    return HttpResponseRedirect('/shop/all_shop')


# 更新商品
def mod_shop(request, id):
    shop = Shop.objects.get(id=id)
    if request.method == "GET":
        return render(request, "mod_shop.html", locals())
    elif request.method == "POST":
        m_price = request.POST["market_price"]
        print(m_price)
        m_num = request.POST["market_num"]
        print(m_num)
        shop.price = m_price
        shop.number = m_num
        shop.save()

        return HttpResponse("修改成功")


# 查询商品
def search_shop(request):
    if request.method == "GET":
        return render(request, "index_shop.html")
    elif request.method == "POST":
        name = request.POST["name"]
        shops = Shop.objects.filter(name__contains=name)
        for i in shops:
            data = model_to_dict(i)
            print(data.get('number'))
        print(shops)
        if not shops:
            return HttpResponse("该商品名称不存在 !!! ")
        return render(request, "search_shop.html", locals())


def all_shop(request):
    shops = Shop.objects.all()
    print(shops)
    return render(request, "all_shop.html", locals())


def test(request):
    if request.method == "POST":
        name = request.POST["name"]
        print(name)
