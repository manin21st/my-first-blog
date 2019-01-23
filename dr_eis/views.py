# -*- encoding:utf8 -*-
# chart test
from django.shortcuts import render, HttpResponse, render_to_response
import random, json
import cx_Oracle
from rest_framework import viewsets
import dr_eis.models as mdl
import dr_eis.serializers as srlz

# Create your views here.
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

#영업정보-계획대비매출실적-년간월별그래프
class SalesPvsrCymViewSet(viewsets.ModelViewSet):
    queryset = mdl.SalesPvsrCym.objects.all()
    serializer_class = srlz.SalesPvsrCymSerializer

#영업정보-계획대비매출실적-5개년그래프
class SalesPvsrCyViewSet(viewsets.ModelViewSet):
    queryset = mdl.SalesPvsrCy.objects.all()
    serializer_class = srlz.SalesPvsrCySerializer

#영업정보-계획대비매출실적-년간월별리스트
class SalesPvsrYmViewSet(viewsets.ModelViewSet):
    queryset = mdl.SalesPvsrYm.objects.all()
    serializer_class = srlz.SalesPvsrYmSerializer
