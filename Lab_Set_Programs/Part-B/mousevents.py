#moving marbles object
#demonstrate mouse input

from superwires import games

games.init(screen_width = 980, screen_height = 720, fps = 50)

class Pan(games.Sprite):
    """ A Pan controlled by the mouse."""
    def update(self):
        """ Move to mouse position."""
        self.x = games.mouse.x
        self.y = games.mouse.y

def main():
    wall_image = games.load_image("download.jpg", transparent = False)
    games.screen.background = wall_image

    pan_image = games.load_image("pizza.bmp")
    the_pan = Pan(image = pan_image,
                  x = games.mouse.x,
                  y = games.mouse.y)
    games.screen.add(the_pan)

    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()


main()