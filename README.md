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
# 🎒 Packing List Microservice (Microservice A)

This microservice generates a customized packing list based on climate, activities, destination, and travel budget.

⚠️ This communication contract is final and will not change. Your teammate relies on this to integrate with your work.

---

## 📥 How to Request Data

User must **call the `generate_packing_list()` function** directly with the required arguments.

### Function Signature

```python
generate_packing_list(climate: str, activities: list[str], destination: str, budget: str) -> dict
```
### Example Request
```python
from packing_list import generate_packing_list

my_list = generate_packing_list(
    climate="cold",
    activities=["relaxing", "cultural"],
    destination="Paris",
    budget="high"
)
```
### Example Response
```python
{
    "destination": "Paris",
    "climate": "cold",
    "activities": ["relaxing", "cultural"],
    "budget": "high",
    "packing_list": [
        "wool coat",
        "comfortable walking shoes",
        "universal power adapter",
        "museum pass",
        "gloves",
        "travel insurance documents"
    ]
}
```
### UML Sequence Diagram
```sql
+------------------+         +--------------------------+
|  Teammate Code   |         | Packing List Microservice|
+------------------+         +--------------------------+
        |                               |
        |  Call generate_packing_list() |
        |------------------------------>|
        |                               |
        |     Generate in-memory list   |
        |                               |
        |      Return packing data      |
        |<------------------------------|
        |                               |

```





