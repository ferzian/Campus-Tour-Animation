from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor
import math

app = Ursina()

music = Audio('assets/sound/bg_music.mp3', loop=True, autoplay=True)
music.volumevolume = 5

window.fps_counter.enabled = False
window.entity_counter.enabled = False
window.collider_counter.enabled = False
window.exit_button.visible = False

player = FirstPersonController(position=(0, 0, -80), speed = 10)

sky = Sky()

ground = Entity(
    model='plane',
    texture='assets/texture/floor.jpeg',
    scale=(200, 1, 200),
    texture_scale=(100, 100),
    collider='box'
)

wall_thickness = 2
wall_height = 10
area_size = 200

wall_left = Entity(
    model='cube',
    texture = 'assets/texture/wall.jpeg',
    texture_scale= (10, 1),
    scale=(wall_thickness, wall_height, area_size),
    position=(-area_size/2, wall_height/2, 0),
    collider='box'
)

wall_right = Entity(
    model='cube',
    texture = 'assets/texture/wall.jpeg',
    texture_scale= (10, 1),
    scale=(wall_thickness, wall_height, area_size),
    position=(area_size/2, wall_height/2, 0),
    collider='box'
)

wall_front = Entity(
    model='cube',
    texture = 'assets/texture/wall.jpeg',
    texture_scale= (10, 1),
    scale=(area_size, wall_height, wall_thickness),
    position=(0, wall_height/2, -area_size/2),
    collider='box'
)

wall_back = Entity(
    model='cube',
    texture = 'assets/texture/wall.jpeg',
    texture_scale= (10, 1),
    scale=(area_size, wall_height, wall_thickness),
    position=(0, wall_height/2, area_size/2),
    collider='box'
)

volleyball = Entity(
    model='assets/models/volleyball.glb',
    position=(0, 0.1, 20),
    rotation = Vec3(0, 90, 0)
)

building_putih = Entity(
    model='assets/models/gedung_hukum.glb',
    position=(-30, -17, 25),
    rotation = Vec3(0, -17, 0),
    scale=0.8
)

main_building = Entity(
    model='assets/models/gedung_f_-_filkom.glb',
    position=(5, 0, 90),
    rotation = Vec3(0, -90, 0),
    scale=2,
    collider = 'mesh'
)

koridor_kiri = Entity(
    model='assets/models/gedung_koridor_-_filkom.glb',
    position=(-10, 0, 73),
    rotation = Vec3(0, -90, 0),
    scale=2.5
)

koridor_kiri = Entity(
    model='assets/models/gedung_koridor_-_filkom.glb',
    position=(-23, 0, 73),
    rotation = Vec3(0, -90, 0),
    scale=2.5
)
koridor_kanan = Entity(
    model='assets/models/gedung_koridor_-_filkom.glb',
    position=(23, 0, 70),
    rotation = Vec3(0, -90, 0),
    scale=2.5
)

koridor_kanan = Entity(
    model='assets/models/gedung_koridor_-_filkom.glb',
    position=(36, 0, 70),
    rotation = Vec3(0, -90, 0),
    scale=2.5
)

classroom_kiri_bawah = Entity(
    model='assets/models/japanese_classroom.glb',
    position=(-65, 0, 1),
    rotation = Vec3(0, 0, 0),
    scale=1.7
)

classroom_kiri_atas = Entity(
    model='assets/models/japanese_classroom.glb',
    position=(-80.5, 0, 35),
    rotation = Vec3(0, 180, 0),
    scale=1.7
)

classroom_hitam = Entity(
    model='assets/models/classroom.glb',
    position=(-60, 0, -20),
    rotation = Vec3(0, 90, 0),
    scale=0.02
)

classroom_hitam = Entity(
    model='assets/models/classroom.glb',
    position=(-80.3, 0, -20),
    rotation = Vec3(0, 90, 0),
    scale=0.02
)

brick_classroom = Entity(
    model='assets/models/my_classroom.glb',
    position=(60, 0.1, 10),
    rotation = Vec3(0, 90, 0),
    scale=2
)

anime_classroom = Entity(
    model='assets/models/anime_classroom.glb',
    position=(46, -1, -25),
    rotation = Vec3(0, 0, 0),
    scale=0.185
)

classroom2 = Entity(
    model='assets/models/japanese_classroom.glb',
    position=(46, 0, -48),
    scale=1.7,
)

gravel_road_kiri = Entity(
    model= 'assets/models/gravel_road.glb',
    position = (-56, 0.5, 17),
    scale = (7,1,10)
)

gravel_road_kiri = Entity(
    model= 'assets/models/gravel_road.glb',
    position = (-65, 0.38, -6),
    rotation = Vec3(0, 90, 0),
    scale = (7,1,14 )
)
gravel_atas = Entity(
    model= 'assets/models/gravel_road.glb',
    position = (-56, 0.38, 43),
    rotation = Vec3(0, 90, 0),
    scale = (7,1,14 )
)
gravel_atas = Entity(
    model= 'assets/models/gravel_road.glb',
    position = (-2.7, 0.38, 43),
    rotation = Vec3(0, 90, 0),
    scale = (7,1,14 )
)

gravel_kanan = Entity(
    model= 'assets/models/gravel_road.glb',
    position = (22, 0.5, 17.3),
    scale = (7,1,10)
)

gravel_tengah = Entity(
    model= 'assets/models/gravel_road.glb',
    position = (-21, 0.5, 16),
    scale = (7,1,10)
)

tree1 = Entity(
    model='assets/models/tree.glb',
    position=(0, 0, 25),
    scale=0.05
)

tree2 = Entity(
    model='assets/models/tree.glb',
    position=(6, 0, 10),
    scale=0.08,
    # collider='box'
)

locust_tree_left = Entity(
    model='assets/models/locust_tree_pack.glb',
    position=(-45, 0, -32),
    scale=0.3
)

locust_tree_right = Entity(
    model='assets/models/locust_tree_pack.glb',
    position=(25, 0, -32),
    scale=0.3,
)

palm_tree = Entity(
    model='assets/models/realistic_palm_tree_5_free.glb',
    position=(-0, 0, -39),
    scale=1,
    # collider='box'
)

bench = Entity(
    model='assets/models/park_bench.glb',
    position=(-21.7, 0.2, 23),
    rotation = Vec3(0, 180, 0),
    scale=1.7,
)

bench_waterfall = Entity(
    model='assets/models/park_bench.glb',
    position=(-55, 0.2, -40),
    rotation = Vec3(0, 180, 0),
    scale=1.7,
)

bench_kanan = Entity(
    model='assets/models/park_bench.glb',
    position=(9, 0.2, 4.5),
    rotation = Vec3(0, 90, 0),
    scale=1.7,
)

bike_parking = Entity(
    model='assets/models/bicycle_parking.glb',
    position=(-45, -0.01, -17),
    rotation = Vec3(0, 90, 0),
    scale=1.7,
    # collider='box'
)

bike_parking = Entity(
    model='assets/models/bicycle_parking.glb',
    position=(-45, -0.01, -23),
    rotation = Vec3(0, 90, 0),
    scale=1.7,
    # collider='box'
)

rock_terrain_left = Entity(
    model='assets/models/lowpoly_rock_terrain.glb',
    position=(-42, -0.8, -15),
    rotation = Vec3(0, 800, 0),
    scale=1.7
)

rock_terrain_right = Entity(
    model='assets/models/lowpoly_rock_terrain.glb',
    position=(-32, -0.8, 4),
    rotation = Vec3(0, 240, 0),
    scale=1.7
)

waterfall = Entity(
    model = 'assets/models/waterfall_mountain_river.glb',
    position = (-45, -40, -90),
    rotation = Vec3(0, 120, 0),
    scale = 3,
    # collider = 'mesh'
)

lamp_left = Entity(
    model = 'assets/models/moscow_lamp_post.glb',
    position = (-34, 0, 0.5),
    rotation = Vec3(0, 120, 0),
    # collider='box'
)

lamp_right = Entity(
    model = 'assets/models/moscow_lamp_post.glb',
    position = (23, 0, -40),
    rotation = Vec3(0, 120, 0),
    # collider='box'
)

lamp_right = Entity(
    model = 'assets/models/moscow_lamp_post.glb',
    position = (27, 0, -5),
    rotation = Vec3(0, 120, 0),
    # collider='box'
)

lamp_front = Entity(
    model = 'assets/models/moscow_lamp_post.glb',
    position = (27, 0, 40),
    rotation = Vec3(0, 120, 0),
    # collider='box'
)

# tes = Entity(
#     model = 'assets/models/ground_scan_8k_001.glb',
#     position = (0, 5, 20),
#     # rotation = Vec3(0, 120, 0),
#     scale = 10
# )

npc = Entity(
    position=(-20, 0.5, 40),
    scale=(1.25, 1.25, 1.25),
    rotation=Vec3(0, -90, 0),
    collider='box'
)

actor = Actor('assets/models/npc.glb')
actor.reparent_to(npc)
print(actor.get_anim_names())
actor.loop('Armature|mixamo.com|Layer0')

corners = [Vec3(-20, 0.5, 45), Vec3(20, 0.5, 45), Vec3(20, 0.5, 10), Vec3(-20, 0.5, 10)]
corner_index = 0
kecepatan_npc = 5

def update():
    global corner_index
    target_position = corners[corner_index]
    direction = (target_position - npc.position).normalized()
    npc.position += direction * kecepatan_npc * time.dt
    npc.rotation_y = -math.degrees(math.atan2(direction.x, direction.z))
    
    if distance(npc.position, target_position) < 0.5:
        corner_index = (corner_index + 1) % len(corners)
        
is_crouching = False
normal_height = player.height
crouch_height = 2
normal_camera_offset = player.camera_pivot.y
crouch_camera_offset = crouch_height / 2

def input(key):
    if key == 'escape':
        application.quit()
    elif key == 'shift':
        player.speed = 100 
    elif key == 'shift up':
        player.speed = 10 
    elif key == 'control':
        is_crouching = True
        player.height = crouch_height
        player.speed = 1
        player.camera_pivot.y = crouch_camera_offset
    elif key == 'control up':
        is_crouching = False
        player.height = normal_height
        player.speed = 10
        player.camera_pivot.y = normal_camera_offset
        
music = Audio('assets/sound/bg_music.mp3', loop=True, autoplay=True)
music.volumevolume = 5

app.run()
