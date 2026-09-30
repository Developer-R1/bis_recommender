from django.conf import settings
from django.contrib import admin
from django.http import FileResponse, HttpResponse
from django.urls import include, path


def home(request):
    """
    Serves the frontend's index.html at the site root, so the whole app is
    one deployed service at one URL. See settings.py (FRONTEND_DIR,
    WHITENOISE_ROOT) for how the frontend's assets/ folder gets served
    alongside this.
    """
    index_path = settings.FRONTEND_DIR / "index.html"
    if not index_path.exists():
        return HttpResponse(
            "Frontend not found. This backend is running correctly (try /api/health/), "
            "but the ../frontend folder wasn't found alongside it.",
            status=200,
        )
    return FileResponse(open(index_path, "rb"), content_type="text/html")


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("standards.urls")),
]
