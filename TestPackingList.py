from getPackingList import *
from packingData import *
import unittest


class Test(unittest.TestCase):
    def testOne(self):
        """Test the function with the climate, activities, destination, and budget populated"""
        print("----------------TEST ONE-----------------")
        climate = "cold"
        activities = ["relaxing", "cultural"]
        destination = "Paris"
        budget = "high"

        # --- Generate Packing List ---
        print(
            f"\n🎒 Packing List for {destination.title()} ({climate}, budget: {budget}):\n"
        )
        packing_list = get_packing_list(climate, activities, destination, budget)

        for item in packing_list:
            print(f"- {item}")
        print("----------------TEST ONE-----------------")

    def testTwo(self):
        """Test the function without having a destination"""
        print("----------------TEST TWO-----------------")
        climate = "hot"
        activities = ["relaxing", "cultural"]
        destination = None
        budget = "high"

        # --- Generate Packing List ---
        print(f"\n🎒 Packing List for ({climate}, budget: {budget}):\n")
        packing_list = get_packing_list(climate, activities, destination, budget)

        for item in packing_list:
            print(f"- {item}")
        print("----------------TEST TWO-----------------")

    def testThree(self):
        """Test the function without having a destination"""
        print("----------------TEST THREE-----------------")
        climate = "freezing"
        activities = []
        destination = None
        budget = "mid"

        # --- Generate Packing List ---
        print(f"\n🎒 Packing List for ({climate}, budget: {budget}):\n")
        packing_list = get_packing_list(climate, activities, destination, budget)

        for item in packing_list:
            print(f"- {item}")
        print("----------------TEST THREE-----------------")


if __name__ == "__main__":
    unittest.main()
