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
            text = 'Classroom Simulation Game',
            parent = self.main_menu,
            position = (-0.6, 0.35, 0),
            scale = 2
            
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
        
    def enable(self):
        super().enable()
        self.back_button.enabled = True
        self.container.enabled = True
        self.music_dropdown.enabled = True

    def disable(self):
        super().disable()
        self.back_button.enabled = False
        self.container.enabled = False
        self.music_dropdown.enabled = False
        
    def go_back(self):
        self.disable()
        Home.enable()
        
# class Main(Entity):
#     # Fungsi untuk membuat dinding dengan tekstur
#     # def create_wall(position, scale, color, texture, texture_scale):
#     #     return Entity(model='cube', position=position, scale=scale, color=color, texture=texture, texture_scale=texture_scale, collider='box')
    
#     # # Membuat dinding sesuai ukuran ground
#     # walls = []
#     # ground_size = ground.scale

#     # wall_positions_scales_colors_textures_texture_scale = [
#     #     (Vec3(-ground_size.x / 2, 5, 0), Vec3(0.2, 10, ground_size.z), color.white, 'brick', (10, 10)),    # Dinding kiri
#     #     (Vec3(ground_size.x / 2, 5, 0), Vec3(0.2, 10, ground_size.z), color.white, 'brick', (10, 10)),    # Dinding kanan
#     #     (Vec3(0, 5, ground_size.z / 2), Vec3(ground_size.x, 10, 0.2), color.white, 'brick', (10, 10)),   # Dinding belakang
#     #     (Vec3(0, 5, -ground_size.z / 2), Vec3(ground_size.x, 10, 0.2), color.white, 'brick', (10, 10))  # Dinding depan
#     # ]

#     # for pos, scale, color, texture, texture_scale in wall_positions_scales_colors_textures_texture_scale:
#     #     walls.append(create_wall(pos, scale, color, texture, texture_scale))
        
#     def __init__(self):
#         super().__init__()

#         # Lantai
#         self.ground = Entity(
#         model='plane',
#         texture='texture/floor.jpeg',
#         scale=(100, 1, 100),
#         texture_scale=(100, 100),
#         collider='box'
#         )
            
#         self.kursi_meja = Entity(
#             model = 'models/chair_table_class.glb',
#             position = (0, 0, 45),  #utara
#             scale = 0.7,
#             collider = 'box'
#         )
#         self.meja_dosen = Entity(
#             model = 'models/meja.glb',
#             position= (5, 0, 0),  #timur
#             scale = 0.03,
#             collider = 'box'
#         )
#         self.classroom = Entity(
#             model = 'models/classroom.glb',
#             position = (0, -1, 0),
#             scale = 1.5,
#             texture = 'grass',
#             collider = None
#         ) 

#         # Membuat atap
#         self.roof = Entity(
#             model='plane', 
#             position=(0, 10, 0),
#             scale=(100, 1, 100),
#             texture='white_cube',  # Tambahkan tekstur untuk atap jika diinginkan
#             texture_scale = (10, 10),
#             collider='box',
#             rotation=(180, 0, 0)
#         )
        
#         self.player = FirstPersonController(
#             parent=self,
#             position=(0, 1, 0)  # Mulai di atas lantai
#         )
        

#         # Fungsi untuk menangani input
#     def input(key):
#         if key == 'escape':  # Tutup aplikasi ketika tombol 'esc' ditekan
#             application.quit()

#         # Player controller
#     # player = FirstPersonController()

    
    
app = Ursina()

Home = LandingPage()
Setting = SettingPage()
# Main = Main()

Setting.enabled = False
# Main.enable = False

def input(key):
    if key == 'escape':
        application.quit()

# Menjalankan aplikasi
app.run()
