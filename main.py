def on_button_pressed_a():
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO7, 45, 64)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO5, 45, 64)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO10, 45, 64)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO12, 135, 64)
    basic.pause(200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO7, 180, 64)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO6, 180, 64)
    basic.pause(500)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO7, 90, 64)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO6, 100, 64)
    basic.pause(500)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO5, 0, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO5, 90, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO5, 0, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO5, 90, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO7, 180, 64)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO6, 180, 64)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.pause(2000)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO13, 180, 64)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO4, 0, 64)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

PCA9685.reset(PCA9685.chip_address("0x40"))