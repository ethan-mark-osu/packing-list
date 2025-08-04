import os
from packingData import *


def get_packing_list(climate, activities=None, destination=None, budget="high"):
    """
    Returns a packing list tailored to climate, activities, and destination.

    Parameters:
    - climate (str): 'hot', 'warm', 'cold', or 'freezing'
    - activities (list[str] or None): activity keywords like 'relaxing', 'urban'
    - destination (str or None): for destination-specific extras
    - budget (str): 'high' (default) or 'mid'

    Returns:
    - list[str]: combined packing list
    """

    # Choose base list
    if budget == "mid":
        climate_base = {
            "hot": HOT_CLIMATE_BUDGET,
            "warm": WARM_CLIMATE_BUDGET,
            "cold": COLD_CLIMATE_BUDGET,
            "freezing": FREEZING_CLIMATE_BUDGET,
        }.get(climate.lower(), [])
    else:
        climate_base = {
            "hot": HOT_CLIMATE_BASE,
            "warm": WARM_CLIMATE_BASE,
            "cold": COLD_CLIMATE_BASE,
            "freezing": FREEZING_CLIMATE_BASE,
        }.get(climate.lower(), [])

    # Add activities (optional)
    activity_add_ons = []
    if activities:
        for act in activities:
            if act == "relaxing":
                activity_add_ons += ACTIVITY_RELAXING
            elif act == "fast-paced":
                activity_add_ons += ACTIVITY_FAST
            elif act == "urban":
                activity_add_ons += ACTIVITY_URBAN
            elif act == "adventure":
                activity_add_ons += ACTIVITY_ADVENTURE
            elif act == "cultural":
                activity_add_ons += ACTIVITY_CULTURE
            elif act == "food":
                activity_add_ons += ACTIVITY_FOOD

    # Destination-specific extras
    extras = DESTINATION_EXTRAS.get(destination.title(), []) if destination else []

    # Combine and deduplicate
    full_list = list(dict.fromkeys(climate_base + activity_add_ons + extras))
    return full_list
