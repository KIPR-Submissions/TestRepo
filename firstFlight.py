from pyparrot.Minidrone import Mambo

# create the drone object and connect
drone = Mambo(use_wifi=True)
drone.connect(num_retries=3)

# maximum speeds - DO NOT CHANGE
drone.set_max_tilt(10)
drone.set_max_vertical_speed(1)

# keeps drone from wondering before command is given
drone.flat_trim()

# takeoff
drone.safe_takeoff(5)

# fly forward a small amount for two seconds
drone.fly_direct(roll=0, pitch=10, yaw=0, vertical_movement=0, duration=3)
drone.smart_sleep(1)

# land and disconnect
drone.safe_land(5)
drone.disconnect()