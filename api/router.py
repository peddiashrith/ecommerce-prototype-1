from .viewsets import *
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('profiles', profileviewset)
router.register('permissions', permissionviewset)
router.register('roles', roleviewset)
router.register('users', userviewset)
