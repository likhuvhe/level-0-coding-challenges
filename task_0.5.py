def area_of_triangle(side1, side2, side3):
   semi_perimeter = 0.5 * (side1 + side2 + side3)
   area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5
   return area