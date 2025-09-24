from django.contrib import admin
from .models import SoilSample, Recommendation, Crop, SoilType, SoilRecommendation, ClimateInsight


@admin.register(SoilSample)
class SoilSampleAdmin(admin.ModelAdmin):
    list_display = ("farmer_name", "location", "ph", "organic_matter", "date_tested")
    search_fields = ("farmer_name", "location")
    list_filter = ("location", "date_tested")
    ordering = ("-date_tested",)  # newest first
    readonly_fields = ("date_tested",)  # protect dates
    fieldsets = (
        ("Farmer Info", {"fields": ("farmer_name", "location")}),
        ("Soil Health Info", {"fields": ("ph", "organic_matter", "date_tested")}),
    )


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("crop", "ph_min", "ph_max", "nutrient_advice")
    search_fields = ("crop__name", "nutrient_advice")
    list_filter = ("crop",)
    ordering = ("crop",)
    fieldsets = (
        ("Crop Needs", {"fields": ("crop",)}),
        ("Soil Requirements", {"fields": ("ph_min", "ph_max", "nutrient_advice")}),
    )


class SoilRecommendationInline(admin.TabularInline):
    model = SoilRecommendation
    extra = 1


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    inlines = [SoilRecommendationInline]


@admin.register(SoilType)
class SoilTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    inlines = [SoilRecommendationInline]


@admin.register(SoilRecommendation)
class SoilRecommendationAdmin(admin.ModelAdmin):
    list_display = ("crop", "soil_type", "recommendation")
    search_fields = ("crop__name", "soil_type__name")
    list_filter = ("crop", "soil_type")


@admin.register(ClimateInsight)
class ClimateInsightAdmin(admin.ModelAdmin):
    list_display = ("title", "date_added")
    search_fields = ("title",)
    list_filter = ("date_added",)
    ordering = ("-date_added",)
    date_hierarchy = "date_added"
