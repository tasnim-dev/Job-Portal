from django.contrib import admin
from django.urls import path
from myApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.signupPage, name='signupPage'),
    path("loginPage", views.loginPage, name='loginPage'),
    path("logoutPage", views.logoutPage, name="logoutPage"),
    path("dashboardPage",views.dashboardPage, name='dashboardPage'),
    path("viewjobPage", views.viewjobPage, name='viewjobPage'),
    path("addjobPage", views.addjobPage, name='addjobPage'),
    path("deletePage/<str:myid>", views.deletePage, name='deletePage'),
    path("editPage/<str:myid>", views.editPage, name='editPage'),
    path("updatePage", views.updatePage, name='updatePage'),
    path("applyPage/<str:myid>", views.applyPage, name='applyPage'),
    path("profilePage", views.profilePage, name='profilePage'),
    path("editprofilePage", views.editprofilePage, name='editprofilePage'),
    path("changepasswordPage", views.changepasswordPage, name='changepasswordPage'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
