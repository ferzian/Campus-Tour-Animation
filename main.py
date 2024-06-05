from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Fungsi untuk membuat dinding dengan tekstur
def create_wall(position, scale, color, texture, texture_scale):
    return Entity(model='cube', position=position, scale=scale, color=color, texture=texture, texture_scale=texture_scale, collider='box')

# Lantai
ground = Entity(
    model='plane',
    texture='texture/floor.jpeg',
    scale=(100, 1, 100),
    texture_scale=(100, 100),
    collider='box'
)

# Membuat dinding sesuai ukuran ground
walls = []
ground_size = ground.scale

wall_positions_scales_colors_textures_texture_scale = [
    (Vec3(-ground_size.x / 2, 5, 0), Vec3(0.2, 10, ground_size.z), color.white, 'brick', (10, 10)),    # Dinding kiri
    (Vec3(ground_size.x / 2, 5, 0), Vec3(0.2, 10, ground_size.z), color.white, 'brick', (10, 10)),    # Dinding kanan
    (Vec3(0, 5, ground_size.z / 2), Vec3(ground_size.x, 10, 0.2), color.white, 'brick', (10, 10)),   # Dinding belakang
    (Vec3(0, 5, -ground_size.z / 2), Vec3(ground_size.x, 10, 0.2), color.white, 'brick', (10, 10))  # Dinding depan
]

for pos, scale, color, texture, texture_scale in wall_positions_scales_colors_textures_texture_scale:
    walls.append(create_wall(pos, scale, color, texture, texture_scale))
    
    kursi_meja = Entity(
        model = 'models/chair_table_class.glb',
        position = (0, 0, 45),  #utara
        scale = 0.7,
        collider = 'box'
    )
    meja_dosen = Entity(
        model = 'models/meja.glb',
        position= (5, 0, 0),  #timur
        scale = 0.03,
        collider = 'box'
    )
    classroom = Entity(
        model = 'models/classroom.glb',
        position = (0, -1, 0),
        scale = 1.5,
        texture = 'grass',
        collider = None
    )
    
    # i1 = load_texture('contoh/textures/Bag 1.png')
    # i2 = load_texture('contoh/textures/Bag 2.jpg')
    # i3 = load_texture('contoh/textures/Bag 3.jpg')
    # i4 = load_texture('contoh/textures/Wal.jpg')

    # textures = ['i1', 'i2', 'i3', 'i4']

    # contoh = Entity(
    #     model = 'contoh/source/contoh.obj',
    #     texture = 'grass',
    #     position = (0, -1, 0),
    #     scale = 0.5,
    #     collider = None
    # )
        

# Membuat atap
roof = Entity(
    model='plane', 
    position=(0, 10, 0),
    scale=(ground_size.x, 1, ground_size.z),
    texture='white_cube',  # Tambahkan tekstur untuk atap jika diinginkan
    texture_scale = (10, 10),
    collider='box',
    rotation=(180, 0, 0)
)

# Fungsi untuk menangani input
def input(key):
    if key == 'escape':  # Tutup aplikasi ketika tombol 'esc' ditekan
        application.quit()

# Player controller
player = FirstPersonController()

# Menjalankan aplikasi
app.run()
