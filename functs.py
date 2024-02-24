try:
  from sense_hat import SenseHat
except:
  from sense_emu import SenseHat
import imports
import logo
class s:
    def setrow(self, pixel_array, row):
        sh = SenseHat()
        if len(pixel_array) == 8:
            for i in range(len(pixel_array)):
                sh.set_pixel(i, row, pixel_array[i])

    def setcolumn(self, pixel_array, column):
        sh = SenseHat()
        if len(pixel_array) == 8:
            for i in range(len(pixel_array)):
                sh.set_pixel(column, i, pixel_array[i])
class utils:
  def clamp(value, minimum, maximum):
    if value < minimum:
      return minimum
    elif value > maximum:
      return maximum
    else:
      return value
  def wrap(value, min_value, max_value):
    range_size = max_value - min_value + 1
    if value < min_value:
        value2 = max_value - (min_value - value) % range_size + 1
    elif value > max_value:
        value2 = min_value + (value - max_value - 1) % range_size
    else:
        value2=value
    return utils.clamp(value2,min_value,max_value)

