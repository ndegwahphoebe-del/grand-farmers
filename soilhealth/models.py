from django.db import models


# Crop model
class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Soil Type model
class SoilType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Soil sample submitted by a farmer
class SoilSample(models.Model):
    farmer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True, blank=True)  # Farmer’s target crop
    soil_type = models.ForeignKey(SoilType, on_delete=models.SET_NULL, null=True, blank=True)

    # Lab results / field data
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    organic_matter = models.DecimalField(max_digits=5, decimal_places=2)
    nitrogen = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    phosphorus = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    potassium = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    date_tested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer_name} - {self.location} ({self.date_tested.date()})"


# Crop-specific recommendation model
class Recommendation(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name="recommendations")
    soil_type = models.ForeignKey(SoilType, on_delete=models.SET_NULL, null=True, blank=True)

    # Optimal ranges
    ph_range = models.CharField(max_length=50, blank=True, help_text="e.g. '5.5 - 7.0' for display")
    ph_min = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ph_max = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    rec_n_min = models.DecimalField("Recommended N (kg/ha)", max_digits=7, decimal_places=2, null=True, blank=True)
    rec_p_min = models.DecimalField("Recommended P (kg/ha)", max_digits=7, decimal_places=2, null=True, blank=True)
    rec_k_min = models.DecimalField("Recommended K (kg/ha)", max_digits=7, decimal_places=2, null=True, blank=True)
    rec_om_min = models.DecimalField("Recommended OM (%)", max_digits=5, decimal_places=2, null=True, blank=True)

    # Advice
    nutrients = models.TextField(blank=True, help_text="Key nutrients to prioritize")
    management_practices = models.TextField(blank=True)
    ph_low_advice = models.TextField(blank=True, null=True, help_text="Advice for acidic soils")
    ph_high_advice = models.TextField(blank=True, null=True, help_text="Advice for alkaline soils")
    nutrient_advice = models.TextField(blank=True, null=True, help_text="Nutrient deficiency advice")
    organic_matter_advice = models.TextField(blank=True, null=True, help_text="Advice to build organic matter")

    def __str__(self):
        return f"Recommendation for {self.crop.name}"


# Soil Recommendation (links crop + soil type, farmer-friendly tip)
class SoilRecommendation(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    soil_type = models.ForeignKey(SoilType, on_delete=models.CASCADE)
    recommendation = models.TextField()
    climate_adaptation_tip = models.TextField(blank=True)

    def __str__(self):
        return f"{self.crop.name} - {self.soil_type.name}"


# Climate Insights (general climate-smart tips)
class ClimateInsight(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


