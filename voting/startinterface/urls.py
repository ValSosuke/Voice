from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.SelectStatus, name='SelectStatus'), 
    url(r'DetaleActive$', views.DetaleActive, name='DetaleActive'),
    url(r'DetaleCompleted$', views.DetaleCompleted, name='DetaleCompleted'),
    url(r'CompletedVoiting$', views.CompletedVoiting, name='CompletedVoiting'),
    url(r'Hendler$', views.Handler, name='Handler'),
]
