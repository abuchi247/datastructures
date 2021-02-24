def hanoi(disk, source, middle, destination):
  # this is the base case - index 0 is always the smallest plate
  # we manipulate the smallest plate in the base case
  if disk == 0:
    print(f"Disk {disk} from {source} to {destination}")
    return

  hanoi(disk-1, source, destination, middle)
  # This is not necessarily the latest plate - this is not the plate 0
  print(f"Disk {disk} from {source} to {destination}")
  hanoi(disk-1, middle, source, destination)


hanoi(2, 'A', 'B', 'C')