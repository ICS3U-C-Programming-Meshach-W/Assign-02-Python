#!/usr/bin/env python3

# Created By: Meshach Wallace
# Date: Oct 9, 2023
# Calculates Surface Area and Volume of cone with input.
import math

def main():
    for i in range(1, 7):
        print("\nCalculations for cone {}: ".format(i))
        
        try:
            radius = float(input("Enter the radius of the cone: "))
            height = float(input("Enter the height of the cone: "))

            if radius < 0 or height < 0:
                print("Radius and height should be non-negative numbers.")
                continue

            volume = (math.pi * radius ** 2 * height) / 3
            surface_area = math.pi * radius * (radius + math.sqrt(height ** 2 + radius ** 2))
            
            print("Volume of the cone {} is: {:.2f}".format(i, volume))
            print("Surface area of the cone {} is: {:.2f}".format(i, surface_area))

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()