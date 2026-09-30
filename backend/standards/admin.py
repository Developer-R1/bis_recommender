from django.contrib import admin
from standards.models import CertificationRule, Feedback, ParamRule, ProductFamily, Standard, StandardEdge

@admin.register(ProductFamily)
class ProductFamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug', 'keywords')

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('is_number', 'part', 'year', 'title', 'family', 'std_type', 'status', 'verification')
    list_filter = ('family', 'std_type', 'status', 'verification')
    search_fields = ('is_number', 'title')

@admin.register(StandardEdge)
class StandardEdgeAdmin(admin.ModelAdmin):
    list_display = ('src', 'dst', 'edge_type', 'mandatory')
    list_filter = ('edge_type', 'mandatory')

@admin.register(CertificationRule)
class CertificationRuleAdmin(admin.ModelAdmin):
    list_display = ('family', 'scheme', 'order_ref', 'effective_date', 'enterprise_size', 'state', 'verification')
    list_filter = ('family', 'scheme', 'state', 'enterprise_size')

@admin.register(ParamRule)
class ParamRuleAdmin(admin.ModelAdmin):
    list_display = ('family', 'grade', 'param', 'operator', 'value', 'unit', 'standard', 'verification')
    list_filter = ('family', 'param', 'verification')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('is_number', 'action', 'created_at')
    list_filter = ('action',)
