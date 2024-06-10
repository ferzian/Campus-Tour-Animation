from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from ursina.prefabs.first_person_controller import FirstPersonController

# Atop-R99O3
# Freedom-10eM
# ChrustyRock-ORLA
FONT = 'assets/font/ChrustyRock-ORLA.ttf'
FONT_COLOR = color.rgba(48/255, 48/255, 48/255, 1)

class LandingPage(Entity):
    def __init__(self):
        super().__init__()
        
        self.main_menu = Entity(
            parent = self,
            enabled = True
        )
        
        Entity(
            model = 'quad',
            parent = self.main_menu,
            position = (0, 0, 1),
            scale = (850/55, 478/55),
            texture = 'assets/texture/bg_menu.jpg'
        )
        
        self.title = Text(
            text = 'Campus Tour',
            parent = self.main_menu,
            position = (-3, 3, 0),
            scale = 25
        )
 
        self.start_button = Button (
            text = 'Start Game',
            parent = self.main_menu,
            color = color.rgba(121/255, 79/255, 53/255, 0.8),
            scale = (4, 1),
            position = (4, 2.2, 0),
            radius = 0.5,
            highlight_color = color.rgba(56/255, 59/255, 52/255, 0.9)
        )
        self.start_button.text_entity.font = FONT
        self.start_button.text_entity.color = FONT_COLOR
        self.start_button.on_click = self.start_game
        
        self.settings_button = Button(
            text="Settings",
            parent = self.main_menu,
            color = color.rgba(121/255, 79/255, 53/255, 0.8),
            scale = (4, 1),
            position = (4, 1, 0),
            radius = 0.5,
            highlight_color = color.rgba(56/255, 59/255, 52/255, 0.9)
        )
        self.settings_button.text_entity.font = FONT
        self.settings_button.text_entity.color = FONT_COLOR
        self.settings_button.on_click = self.show_setting

        self.quit_button = Button(
            text="Quit",
            parent = self.main_menu,
            color = color.rgba(121/255, 79/255, 53/255, 0.8),
            scale = (4, 1),
            position = (4, -0.2, 0),
            radius = 0.5,
            highlight_color = color.rgba(56/255, 59/255, 52/255, 0.9)
        )
        self.quit_button.text_entity.font = FONT
        self.quit_button.text_entity.color = FONT_COLOR
        self.quit_button.on_click = application.quit
        
    def start_game(self):
            print('start game')
            self.disable()
            # Main.enable()
            
    def show_setting(self):
            print('Masuk Setting')
            self.disable()
            Setting.enable()
   
class SettingPage(Entity):
    def __init__(self):
        super().__init__()
        
        self.game_settings = Entity(
            parent=self,
            enabled=True,
        )

        Entity(
            model="quad",
            parent=self.game_settings,
            position = (0, 0, 1),
            scale = (4096/268, 4096/400),
            texture="assets/texture/bg_setting.jpg",
        )
        
        self.back_button = Button(
            text = 'Back',
            parent= self.game_settings,
            color = color.rgba(122/255, 197/255, 167/255, 0.8),
            scale = (3, 1),
            position = (-5, 3, 0),
            radius = 0.5,
            color_highlight=color.rgba(56/255, 59/255, 52/255, 0.9),
            enabled = False
        )
        self.back_button.text_entity.font = FONT
        self.back_button.text_entity.color = FONT_COLOR
        self.back_button.on_click = self.go_back
        
        self.container = Entity(
            model = 'quad',
            color = color.rgba(45/255, 80/255, 66/255, 0.6),
            scale = (10, 5),
            position = (-1.5, -0.5, 0),
            enabled = False
        )
        
        self.music_dropdown = DropdownMenu(
            'Music',
            buttons = [
                DropdownMenuButton('On', 
                                   color = color.rgba(45/255, 80/255, 66/255, 0.6), 
                                   text_color =  color.rgb(200/255, 200/255, 200/255),
                                   ), 
                DropdownMenuButton('Off', 
                                   color = color.rgba(45/255, 80/255, 66/255, 0.6), 
                                   text_color =  color.rgb(200/255, 200/255, 200/255),
                                   )],
            position = (-6, 1.7, -0.02),
            scale = (7, 0.8),
            color = color.rgba(45/255, 80/255, 66/255, 0.6),
            text_color =  color.rgb(200/255, 200/255, 200/255)
        )
        self.music_dropdown.parent = self.game_settings
        
         # Slider for music volume
        self.music_volume_slider = Slider(
            min=1,
            max=100,
            default=90,
            position=(-3.8, -1, -0.02),
            scale=(13, 13),
            text='Music Volume',
            enabled=False,
            color=color.rgba(45/255, 80/255, 66/255, 0.6),
            text_color=color.rgb(200/255, 200/255, 200/255)
        )
        self.music_volume_slider.parent = self.game_settings
        
         # Slider for mouse sensitivity
        self.mouse_sensitivity_slider = Slider(
            min=1,
            max=5,
            default=2.5,
            position=(-3.3, -2, -0.02),
            scale=(13, 13),
            text='Mouse Sensitivity',
            enabled=False,
            color=color.rgba(45/255, 80/255, 66/255, 0.6),
            text_color=color.rgb(200/255, 200/255, 200/255)
        )
        self.mouse_sensitivity_slider.parent = self.game_settings
        
    def enable(self):
        super().enable()
        self.back_button.enabled = True
        self.container.enabled = True
        self.music_dropdown.enabled = True
        self.music_volume_slider.enabled = True
        self.mouse_sensitivity_slider.enabled = True

    def disable(self):
        super().disable()
        self.back_button.enabled = False
        self.container.enabled = False
        self.music_dropdown.enabled = False
        self.music_volume_slider.enabled = False
        self.mouse_sensitivity_slider.enabled = False
        
    def go_back(self):
        self.disable()
        Home.enable()
        
# class Main(Entity):        
#     def __init__(self):
#         super().__init__()


    
    
app = Ursina()

Home = LandingPage()
Setting = SettingPage()
# Main = Main()

Setting.enabled = False
# Main.enable = False

music = Audio('assets/sound/music.mp3', loop=True, autoplay=True)
music.volume = SettingPage.music_volume_slider.value

def input(key):
    if key == 'escape':
        application.quit()

# Menjalankan aplikasi
app.run()