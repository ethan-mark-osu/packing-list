# 🧳 Travel Packing List Generator Component (Terminal-Based)

This is a simple, terminal-based Python component that generates a customized travel packing list based on:

- **Climate** (required)
- **Activities** (optional)
- **Destination** (optional)
- **Budget** (optional)

⚠️ This communication contract is final and will not change. Your teammate relies on this to integrate with your work.

---

## 📁 Files Included

| File                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `packingData.py`    | Contains packing list data categorized by climate, budget, activity, and destination |
| `getPackingList.py` | Contains the `generate_packing_list()` function that generates the list     |
| `TestPackingList.py`| Example script that calls the packing list generator with hardcoded inputs  |

---

## 🚀 How It Works

The generator builds a packing list using:
- A **base list** based on climate and budget
- **Activity-specific** additions (e.g., hiking gear, swimwear)
- **Destination-specific** extras (e.g., metro card, guidebook)

All logic runs in-memory, with no external API calls or file dependencies.

---

## 📥 How to Programmatically Request Data

Teammates must call the function `generate_packing_list()` with four arguments:

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





