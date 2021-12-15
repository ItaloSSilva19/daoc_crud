from rest_framework import routers
from crud.viewsets import PessoaViewSets

router = routers.DefaultRouter()
router.register('pessoa',PessoaViewSets)