# -*- encoding:utf8 -*-
# chart test
from django.shortcuts import render, HttpResponse, render_to_response
import random, json
import cx_Oracle
import dr_eis.models as mdl

# Create your views here.
def data_json(request):
    Fluctuation_ratio = 50  # 등락비율(%)
    ratio = Fluctuation_ratio / float(100)
    init_cost = 1000000  # 백만원
    Counts = [None, ]
    Costs = ['주식가격', ]

    for i in range(1, 101):
        Counts.append(str(i))
        if random.choice((True, False)):
            init_cost += init_cost * ratio
            Costs.append(init_cost)
        else:
            init_cost -= init_cost * ratio
            Costs.append(init_cost)
    data = {
        'columns': [
            Counts,
            Costs,
        ]
    }
    return HttpResponse(json.dumps(data), content_type='text/json')

def hichart_sample(request):
    return render_to_response('hichart_sample.html')

def chartjs_sample(request):
    return render_to_response('chartjs_sample.html')

def json_data(request):
    conn = cx_Oracle.connect('erpman/erpman@61.76.134.83:1521/sangil')
    sql = "SELECT ITNBR, ITDSC FROM ITEMAS"
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchmany(numRows=3)
    cur.close()
    conn.close()

    return HttpResponse(json.dumps(data), content_type='text/json')

#영업정보-계획대비매출실적
def sales_pvsr(request):
    cdata1 = mdl.SalesPvsrCym.objects.filter(yymm__startswith='2018').order_by('yymm')
    cdata2 = mdl.SalesPvsrCy.objects.filter(yyyy__startswith='2018').order_by('yyyy')
    ldata1 = mdl.SalesPvsrYm.objects.filter(yymm__startswith='2018').order_by('yymm')
    #return render(request, 'sales_pvsr.html', {'cdata1': cdata1, 'cdata2': cdata2, 'ldata1': ldata1})
    return render(request, 'sales_pvsr.html', {'cdata1': list(cdata1)})
