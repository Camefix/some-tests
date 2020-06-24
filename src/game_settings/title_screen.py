from game_settings.display import window_width, window_height, fps

# Important parameters
'''
These are parameters that take parts in some calculation, but also influence the whole design of the code.
As such, they cannot be changed as easily as the others, you need to rethink the code.
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
buttons_spacing = 1/3 * window_width - button_width     # window_width = 3 * (button_width + button_spacing)
buttons_speed = (window_width / buttons_displayed) / round(fps * time_move)
title_width = window_width * 0.8
title_height = window_height * 0.4
title_left = window_width * 0.1
title_top = window_height * 0.3
title_speed = [0, -2]


