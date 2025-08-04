# 🧳 Travel Packing List Generator Component (Terminal-Based)

This is a simple, terminal-based Python component that generates a customized travel packing list based on:

- **Climate** (required)
- **Activities** (optional)
- **Destination** (optional)
- **Budget** (optional)

---

## 📁 Files Included

| File                    | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `packingData.py`       | Contains packing list data by climate, budget, activity, and destination    |
| `getPackingList.py`   | A python script that takes in the climate, activites, destination, and budget and will return the packing list that matches the parameters provided |
| `TestPackingList.py` | A terminal script that calls the packing list generator with hardcoded values |

---

## 🚀 How It Works

The script combines:
- A **climate-specific** packing list (based on your selected climate and budget)
- **Activity-specific** add-ons (e.g., hiking, relaxing)
- **Destination-specific** extras (for fun or practical items like a metro pass)

---

## ✅ Usage

1. Open `TestPackingList.py`
2. Modify the variables at the bottom of the file:

```python
climate = "cold"
activities = ["relaxing", "cultural"]
destination = "Paris"
budget = "high"
