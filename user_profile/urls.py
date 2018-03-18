from django.urls import path
from .views import login, JobDetailsViewSet, TaskViewSet, JobApplyDetailsViewSet


urlpatterns = [
	path('jobs', JobDetailsViewSet.as_view({'get': 'list'}), name='JobDetailsViewSet'),
	#path('jobs/<int:pk>', JobDetailsViewSet.as_view(), name='JobDetailsViewSet-detail'),
	path('task', TaskViewSet.as_view({'get': 'list'}), name='TaskViewSet'),
	#path('task/<int:pk>', TaskViewSet.as_view({'get': 'list'}), name='TaskViewSet-detail'),
	path('jobapply', JobApplyDetailsViewSet.as_view({'get': 'list'}), name='JobApplyDetailsViewSet'),
	#path('jobapply/<int:pk>', JobApplyDetailsViewSet.as_view(), name='JobApplyDetailsViewSet-detail'),
	path('login', login, name='login'),
]

