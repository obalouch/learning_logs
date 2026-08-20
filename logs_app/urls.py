from django.urls import path
from . import views

app_name = 'logs_app'
urlpatterns = [
    # homepage
    path('',views.index , name = 'index' ),
    path('mine',views.mine,name = 'test'),
    path('topics',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    path('new_topic',views.newTopic,name='newTopic'),
    path('new_entry/<int:topic_id>',views.newEntry,name='newEntry'),
    path('editentry/<int:entry_id>',views.editentry,name='edit_entry')

]