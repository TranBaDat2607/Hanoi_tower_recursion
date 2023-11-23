def hanoi_tower_recursion(disk, colum_1, colum_2, colum_3):
    if disk == 1:
        print(f"move {disk} from {colum_1} to {colum_2}")
    else:
        hanoi_tower_recursion(disk-1, colum_1, colum_3, colum_2)
        
        hanoi_tower_recursion(1, colum_1, colum_2, colum_3)
        hanoi_tower_recursion(disk-1, colum_3, colum_2, colum_1)
disk = int(input("How many disk: "))
colum_1 = "A"
colum_2 = "B"
colum_3 = "C"
hanoi_tower_recursion(disk, colum_1, colum_2, colum_3)