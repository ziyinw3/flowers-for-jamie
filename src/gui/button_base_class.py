# button base class

# or rather, clickable?

# extend entity base class

from src.entities.entity_base_class import Entity


class Button(Entity):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__(x_coord, y_coord, width, height)
        self.sound_played = False
    
    def setter(self, sound = None, hover_img = None, navigate_destination = None):
        self.sound = sound
        self.hover_img = hover_img
        self.navigate_destination = navigate_destination
    
    def navigate(self):
        pass

    def hover_feedback(self):
        if not self.sound_played:
            # self.sound.play()
            self.sound_played = True
        else:
            self.sound_played = False
