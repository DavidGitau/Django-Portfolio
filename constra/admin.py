from django.contrib import admin
from .models import (
    Category,
    Comment,
    Fact,
    News,
    PricingFeatures,
    Pricing,
    Project,
    Service,
    Solution,
    Team,
    Testimonial,
)

admin.site.register([
    Category,
    Comment,
    Fact,
    News,
    PricingFeatures,
    Pricing,
    Project,
    Service,
    Solution,
    Team,
    Testimonial,
])