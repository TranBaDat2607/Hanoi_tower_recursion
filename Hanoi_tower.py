def hanoi_tower_recursion(disk, colum_1, colum_2, colum_3):
    # We need to move n disks from colum A to colum B 
    if disk == 1:
        print(f"move {disk} from {colum_1} to {colum_2}")
    else:
        # Move n-1 disk from colum A to colum C
        hanoi_tower_recursion(disk-1, colum_1, colum_3, colum_2)
        # Move the biggest disk from colum A to colum B
        hanoi_tower_recursion(1, colum_1, colum_2, colum_3)
        # Move n-1 disks from colum C to B
        hanoi_tower_recursion(disk-1, colum_3, colum_2, colum_1)
disk = int(input("How many disk: "))
colum_1 = "A"
colum_2 = "B"
colum_3 = "C"
hanoi_tower_recursion(disk, colum_1, colum_2, colum_3)
