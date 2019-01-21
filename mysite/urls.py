"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import dr_eis.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'', include('blog.urls')),
    url(r'^data.json$', dr_eis.views.data_json),
    url(r'^hichart/', dr_eis.views.hichart_sample),
    url(r'^$', dr_eis.views.chartjs_sample),
    url(r'^json_data$', dr_eis.views.json_data, name='json_data'),
    url(r'^sales_pvsr$', dr_eis.views.sales_pvsr),  #영업정보-계획대비매출실적
]
