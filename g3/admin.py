from django.contrib import admin
from g3.models import anapath, comment_anap, anatomie, comment_anat, biologie_clinique, comment_biocli, embryologie, comment_embryo, immunologie, comment_immuno, microbiologie, comment_immuno, parasito, comment_parasito, pharmacologie, comment_pharm, physio_speciale, comment_physios, physiopathologie, comment_physio, radiologie, comment_radio


# Register your models here.

admin.site.register(anatomie)
admin.site.register(anapath)
admin.site.register(parasito)
admin.site.register(physio_speciale)
admin.site.register(pharmacologie)
admin.site.register(physiopathologie)
admin.site.register(biologie_clinique)
admin.site.register(radiologie)
admin.site.register(microbiologie)
admin.site.register(embryologie)
admin.site.register(immunologie)
admin.site.register(comment_anap)
admin.site.register(comment_anat)
admin.site.register(comment_biocli)
admin.site.register(comment_embryo)
admin.site.register(comment_immuno)
admin.site.register(comment_parasito)
admin.site.register(comment_pharm)
admin.site.register(comment_physios)
admin.site.register(comment_physio)
admin.site.register(comment_radio)