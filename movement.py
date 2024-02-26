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
    if direction == 'up':
        return [0, 1]
    elif direction == 'down':
        return [0, -1]
    elif direction == 'left':
        return [-1, 0]
    elif direction == 'right':
        return [1, 0]
    elif direction == 'middle':
        return [0, 0]
    elif direction == 'up_left':
        return [-1, 1]
    elif direction == 'up_right':
        return [1, 1]
    elif direction == 'down_left':
        return [-1, -1]
    elif direction == 'down_right':
        return [1, -1]
    elif direction == 'pressed':
        return None  # Handle button press
