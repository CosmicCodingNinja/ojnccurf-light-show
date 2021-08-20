basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")

def on_forever():
    led.set_brightness(input.sound_level())
basic.forever(on_forever)
