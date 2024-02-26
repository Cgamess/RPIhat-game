try:
  import sense_hat as sho
  sense=sho.Sensehat()
except:
  import sense_emu as sho
  sense=sho.SenseHat()

# Function to get joystick event
def get_joystick_event():
    for event in sense.stick.get_events():
        if event.action == 'pressed' or event.action == 'held':
            return event.direction
    return None

# Function to get movement matrix based on joystick direction
def get_movement_matrix():
    direction=get_joystick_event()
    if direction == 'U':
        return [0, 1]
    elif direction == 'D':
        return [0, -1]
    elif direction == 'L':
        return [-1, 0]
    elif direction == 'R':
        return [1, 0]
    elif direction == 'M':
        return [0, 0]
    elif direction == 'pressed':
        return None  # Handle button press
