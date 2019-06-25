from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', blog.views.home , name='home'),
    path('admin/', admin.site.urls),
    # path('blog/' , include('blog.urls')),
    path('blog/<int:blog_id>', blog.views.detail, name='detail'),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create', blog.views.create, name='create'),
    path('blog/newblog/' , blog.views.blogpost , name='newBlogPost'),
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
    path('accounts/', include('accounts.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
