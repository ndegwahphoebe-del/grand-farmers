from django.shortcuts import render, redirect
from .models import SoilSample, Recommendation, Crop
from django.utils.timezone import now

# Home page
def home(request):
    return render(request, "soilhealth/home.html")

# Recommendations page
def recommendations(request):
    crops = [
        {
            "name": "🌽 Maize",
            "ph": "5.5 – 7.0",
            "nutrients": "Needs plenty of nitrogen and good phosphorus for strong growth.",
            "climate_tip": "Mulch and rotate with legumes to keep soil fertile and hold moisture.",
            "empowerment": "Healthy soils give you stronger maize harvests and better food security."
        },
        {
            "name": "☕ Coffee",
            "ph": "5.0 – 6.5",
            "nutrients": "Loves rich organic matter, nitrogen, and enough potassium.",
            "climate_tip": "Plant shade trees to protect coffee from heat stress and conserve water.",
            "empowerment": "With climate-smart care, your coffee trees stay productive for many years."
        },
        {
            "name": "🫘 Beans",
            "ph": "6.0 – 7.5",
            "nutrients": "Do well with phosphorus and benefit from Rhizobium inoculation.",
            "climate_tip": "Beans fix nitrogen, helping your soil recover naturally for the next crop.",
            "empowerment": "Planting beans not only feeds your family but also heals your soil."
        },
        {
            "name": "🥑 Avocado",
            "ph": "5.5 – 7.0",
            "nutrients": "Needs balanced nitrogen, potassium, calcium, and organic matter.",
            "climate_tip": "Mulch with dry leaves to keep moisture and improve soil health.",
            "empowerment": "A well-nourished avocado tree gives fruits for years and boosts farm income."
        },
        {
            "name": "🌾 Wheat",
            "ph": "6.0 – 7.0",
            "nutrients": "Needs nitrogen for tillering and phosphorus for strong roots.",
            "climate_tip": "Plant early to escape drought stress and add organic matter for soil health.",
            "empowerment": "Healthy soils grow golden wheat that feeds the community and market."
        },
        {
            "name": "🥬 Cabbages",
            "ph": "6.0 – 7.5",
            "nutrients": "Heavy feeder, requires high nitrogen, calcium, and boron.",
            "climate_tip": "Practice crop rotation to reduce pests and save soil nutrients.",
            "empowerment": "Strong, healthy cabbages mean higher yields and better family nutrition."
        },
        {
            "name": "🧅 Onions",
            "ph": "6.0 – 7.0",
            "nutrients": "Need phosphorus for bulb growth and sulfur for good flavor.",
            "climate_tip": "Irrigate wisely and mulch to reduce heat stress and conserve water.",
            "empowerment": "Healthy onions bring steady income and improve household diets."
        },
        {
            "name": "🍉 Watermelons",
            "ph": "6.0 – 6.8",
            "nutrients": "High potassium for sweetness, nitrogen early for vine growth.",
            "climate_tip": "Plant on raised beds to avoid waterlogging during heavy rains.",
            "empowerment": "Sweet, juicy watermelons from healthy soils bring profit and joy."
        },
    ]
    return render(request, "soilhealth/recommendations.html", {"crops": crops})

def soil_sample(request):
    crops = Crop.objects.all()

    if request.method == "POST":
        farmer_name = request.POST.get("farmer_name")
        location = request.POST.get("location")
        ph = float(request.POST.get("ph"))
        organic_matter = float(request.POST.get("organic_matter"))
        nitrogen = float(request.POST.get("nitrogen"))
        phosphorus = float(request.POST.get("phosphorus"))
        potassium = float(request.POST.get("potassium"))
        crop_id = request.POST.get("crop")

        crop = Crop.objects.get(id=crop_id)

        # Save to DB
        sample = SoilSample.objects.create(
            farmer_name=farmer_name,
            location=location,
            ph=ph,
            organic_matter=organic_matter,
            nitrogen=nitrogen,
            phosphorus=phosphorus,
            potassium=potassium,
        )

        # Recommendations with color codes
        recommendations = []

        def recommend(param, value, low, high, name):
            if value < low:
                return {"text": f"{name} is low. Take corrective action.", "color": "red"}
            elif low <= value <= high:
                return {"text": f"{name} is ideal. Keep up the good work.", "color": "green"}
            else:
                return {"text": f"{name} is high. Avoid over-application.", "color": "orange"}

        # Customize ideal ranges per crop (example: Wheat)
        recommendations.append(recommend("Soil pH", ph, 5.5, 7, "Soil pH"))
        recommendations.append(recommend("Organic Matter (%)", organic_matter, 3, 6, "Organic Matter"))
        recommendations.append(recommend("Nitrogen (N)", nitrogen, 10, 20, "Nitrogen"))
        recommendations.append(recommend("Phosphorus (P)", phosphorus, 15, 30, "Phosphorus"))
        recommendations.append(recommend("Potassium (K)", potassium, 40, 60, "Potassium"))

        return render(request, "soilhealth/diagnosis.html", {
            "sample": sample,
            "crop": crop,
            "farmer_name": farmer_name,
            "location": location,
            "ph": ph,
            "organic_matter": organic_matter,
            "nitrogen": nitrogen,
            "phosphorus": phosphorus,
            "potassium": potassium,
            "recommendations": recommendations
        })

    return render(request, "soilhealth/soil_sample.html", {"crops": crops})
# Climate insights page
def climate_insights(request):
    return render(request, "soilhealth/climate_insights.html")
