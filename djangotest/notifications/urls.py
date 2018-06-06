from django.conf.urls import url

from . import views

print('notificatiln/urls')
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Notifications.as_view(),
        name='notifications'
    ),
]
