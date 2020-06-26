from game_settings.display import window_width, window_height, fps

# Sensible parameters
'''
buttons_displayed is the number of buttons on the title screen at the same time.
Also changing it would mostly work, the sizes of the buttons or their place on the screen would be messed up.
It may work if you set an odd number, definitely not an even.
'''
buttons_displayed = 3

# Timings
time_end_standstill = 1
time_start_appear = 1.3
time_end_intro = 1.8
time_move = 0.33

# Display values
button_width= window_width * 0.2
button_height = window_height * 0.1
buttons_top = window_height * 0.7
buttons_spacing = 1 / buttons_displayed * window_width - button_width     # window_width = buttons_displayed * (button_width + button_spacing)
buttons_speed = (window_width / buttons_displayed) / round(fps * time_move)
title_width = window_width * 0.8
title_height = window_height * 0.4
title_left = window_width * 0.1
title_top = window_height * 0.3
title_speed = [0, -2]


