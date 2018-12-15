from django.shortcuts import render
from django.views import View

from test_1.tasks import Task1, Task2, Task3


class SpiderDec(View):
    http_method_names = ['get', 'post']

    def get(self, request):
        context = {
            'senior': '0',
            'ieflg': {'I': '进口', 'E': '出口'},
            'clear_customs': {'0': '否', '1': '是'},
            'customs_unit': {'A': '报关申报单位', 'B': '消费使用/生产销售单位', 'C': '报关收发货人', 'D': '报关录入单位'},
            'dec_type_dict': {'0': '一般报关单', '1': '转关提前报关单', '2': '备案清单', '3': '转关提前备案清单', '4': '出口二次转关'},
        }
        # Task2().apply_async(queue='machine2', routing_key='machine2')
        Task2().delay()
        return render(request, 'spider_dec.html', context)

    def post(self, request):
        seqno = request.POST.get('seqno')
        entryid = request.POST.get('entryid')
        ieflag = request.POST.get('ieflag')
        is_clear = request.POST.get('is_clear')
        enterprise = request.POST.get('enterprise')
        dec_type = request.POST.get('dec_type')
        etpsno = request.POST.get('etpsno')
        senior = request.POST.get('senior')
        Task1().apply_async(queue='machine1', routing_key='machine1')
        context = {
            'seqno': seqno,
            'entryid': entryid,
            'senior': senior,
            'ieflag': ieflag,
            'etpsno': etpsno,
            'is_clear': is_clear,
            'enterprise': enterprise,
            'ieflg': {'I': '进口', 'E': '出口'},
            'clear_customs': {'0': '否', '1': '是'},
            'customs_unit': {'A': '报关申报单位', 'B': '消费使用/生产销售单位', 'C': '报关收发货人', 'D': '报关录入单位'},
            'dec_type_dict': {'0': '一般报关单', '1': '转关提前报关单', '2': '备案清单', '3': '转关提前备案清单', '4': '出口二次转关'},
        }
        return render(request, 'spider_dec.html', context)