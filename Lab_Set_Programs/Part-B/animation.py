# Explosion animation
# Demonstrates creating an animation

from superwires import games

games.init(screen_width = 1280, screen_height = 720, fps = 50)

back_image=games.load_image("download.jpg", transparent = 0)
games.screen.background = back_image

explosion_files = ["wolf1.bmp","wolf2.bmp"]
explosion = games.Animation(images = explosion_files,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            n_repeats = 0,
                            repeat_interval = 20)
games.screen.add(explosion)
games.screen.mainloop()
