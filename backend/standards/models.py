from django.db import models

VERIFICATION_CHOICES = [
    ('official_verified', 'Verified against official BIS/gazette source'),
    ('public_data', 'Sourced from public secondary references'),
    ('demo', 'Placeholder / illustrative data'),
]
STATUS_CHOICES = [
    ('current', 'Current'), ('withdrawn', 'Withdrawn'),
    ('superseded', 'Superseded'), ('unknown', 'Unknown'),
]
STD_TYPE_CHOICES = [
    ('product', 'Product'), ('test_method', 'Test method'),
    ('terminology', 'Terminology'), ('sampling', 'Sampling'),
    ('safety', 'Safety'), ('installation', 'Installation'),
    ('code_of_practice', 'Code of practice'), ('packaging', 'Packaging'),
    ('normative_reference', 'Normative reference'),
]
EDGE_TYPE_CHOICES = [
    ('normative_reference', 'Normative reference'), ('test_method', 'Test method'),
    ('terminology', 'Terminology'), ('sampling', 'Sampling'), ('safety', 'Safety'),
    ('installation', 'Installation'), ('code_of_practice', 'Code of practice'),
    ('packaging', 'Packaging'), ('co_cited', 'Commonly co-cited'),
]
CERT_STATE_CHOICES = [
    ('notified', 'Notified'), ('in_force', 'In force'),
    ('deferred', 'Deferred'), ('revoked', 'Revoked'), ('superseded', 'Superseded'),
]

class ProductFamily(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    keywords = models.TextField()

    class Meta:
        verbose_name_plural = 'Product families'
        ordering = ['name']

    def __str__(self):
        return self.name

    def keyword_list(self):
        return [k.strip() for k in self.keywords.split(',') if k.strip()]

class Standard(models.Model):
    is_number = models.CharField(max_length=40)
    part = models.CharField(max_length=40, blank=True, default='')
    year = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=500)
    family = models.ForeignKey(ProductFamily, on_delete=models.SET_NULL, null=True, blank=True, related_name='standards')
    std_type = models.CharField(max_length=30, choices=STD_TYPE_CHOICES, default='product')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unknown')
    replaced_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replaces')
    amendments = models.JSONField(default=list, blank=True)
    amendment_note = models.TextField(blank=True)
    source_url = models.URLField(blank=True, max_length=500)
    verification = models.CharField(max_length=20, choices=VERIFICATION_CHOICES, default='public_data')
    last_verified = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    triggers = models.JSONField(default=list, blank=True)

    class Meta:
        unique_together = [('is_number', 'part', 'year')]
        ordering = ['is_number', 'part', 'year']

    def __str__(self):
        n = self.is_number
        if self.part: n += f' ({self.part})'
        if self.year: n += f':{self.year}'
        return n

    def display_number(self):
        n = self.is_number
        if self.part: n += f' ({self.part})'
        if self.year: n += f':{self.year}'
        return n

class StandardEdge(models.Model):
    src = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='outgoing_edges')
    dst = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='incoming_edges')
    edge_type = models.CharField(max_length=30, choices=EDGE_TYPE_CHOICES)
    mandatory = models.BooleanField(default=False)
    condition = models.TextField(blank=True)
    evidence = models.TextField(blank=True)
    source_url = models.URLField(blank=True, max_length=500)

    class Meta:
        unique_together = ('src', 'dst', 'edge_type')

    def __str__(self):
        return f'{self.src} --{self.edge_type}--> {self.dst}'

class CertificationRule(models.Model):
    family = models.ForeignKey(ProductFamily, on_delete=models.CASCADE, related_name='cert_rules')
    is_number = models.CharField(max_length=40)
    scheme = models.CharField(max_length=40)
    order_ref = models.CharField(max_length=300)
    effective_date = models.DateField(blank=True, null=True)
    since_year = models.PositiveIntegerField(blank=True, null=True)
    enterprise_size = models.CharField(max_length=10, default='all')
    state = models.CharField(max_length=20, choices=CERT_STATE_CHOICES, default='in_force')
    notes = models.TextField(blank=True)
    source_url = models.URLField(blank=True, max_length=500)
    verification = models.CharField(max_length=20, choices=VERIFICATION_CHOICES, default='public_data')
    last_verified = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('family', 'order_ref', 'enterprise_size')
        ordering = ['family', 'effective_date']

    def __str__(self):
        return f'{self.family.slug}: {self.order_ref[:50]} ({self.enterprise_size})'

class ParamRule(models.Model):
    OPERATOR_CHOICES = [('min', 'Minimum'), ('max', 'Maximum'), ('equal', 'Equal')]
    family = models.ForeignKey(ProductFamily, on_delete=models.CASCADE, related_name='param_rules')
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='param_rules')
    grade = models.CharField(max_length=40, blank=True, default='')
    param = models.CharField(max_length=60)
    operator = models.CharField(max_length=10, choices=OPERATOR_CHOICES)
    value = models.FloatField()
    unit = models.CharField(max_length=20)
    clause_ref = models.CharField(max_length=200, blank=True)
    source_url = models.URLField(blank=True, max_length=500)
    verification = models.CharField(max_length=20, choices=VERIFICATION_CHOICES, default='public_data')

    class Meta:
        unique_together = ('family', 'standard', 'grade', 'param')
        ordering = ['family', 'grade', 'param']

    def __str__(self):
        return f'{self.family.slug} [{self.grade}]: {self.param} {self.operator} {self.value} {self.unit}'

class Feedback(models.Model):
    ACTION_CHOICES = [('accept', 'Accept'), ('reject', 'Reject'), ('flag', 'Flag')]
    analysis_id = models.CharField(max_length=64, blank=True)
    is_number = models.CharField(max_length=40)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.action} on {self.is_number}'
