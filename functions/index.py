# import area_of_rectangle as aor







#### import module using "from"
from area_of_rectangle import calculate_rectangle_area,calculate_box_volume


length1=int(input("enter your length "))
width1=int(input("please enter your width "))
height1=int(input("please enter your height "))
area= calculate_rectangle_area(length1,width1)
print(f"The calculated area is = {area}")
# volume=area*height1
volume= calculate_box_volume(area,height1)
print(f"The calculated volume is = {volume} ")