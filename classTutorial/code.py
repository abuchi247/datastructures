class Device:

  def __init__(self, name, connected_by):
    self.name = name
    self.connected_by = connected_by
    self.connected = True

  def __str__(self):
    return f"Device {self.name!r} ({self.connected_by})"

  def disconnect(self):
    self.connected = False
    print("Device disconnected!")


class Printer(Device):

  def __init__(self, name, connected_by, capacity):
    super().__init__(name, connected_by)
    self.capacity = capacity
    self.remaining_pages = capacity

  def __str__(self):
    return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

  def print_page(self, pages):
    if not self.connected:
      print("Your printer is not connected")
      return

    if pages >= self.remaining_pages:
      pages_left_to_print = pages - self.remaining_pages
      print(f"Printed {self.remaining_pages} page(s). Need to reload {pages_left_to_print} page(s).")
      self.remaining_pages = 0
      return
    else:
      print(f"Printing {pages} pages.")
      self.remaining_pages -= pages


if __name__ == "__main__":
  printer = Printer("Printer", "USB", 10)
  printer.print_page(20)
  print(printer)