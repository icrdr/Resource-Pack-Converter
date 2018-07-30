blockList = []
itemList = []
entityList = []
modelList = [
    ['cobblestone_wall_mossy_inventory','mossy_cobblestone_wall_inventory'],
    ['stonebrick_mossy','mossy_stone_bricks'],
    ['wall_side','template_wall_side'],
    ['wall_post','template_wall_post'],


    ['grass','grass_block'],                #-------keep the order
    ['grass_normal','grass_block'],         #---|
    ['grass_snowed','grass_block_snow'],
    ['tall_grass','grass'],
    ['double_grass_bottom','tall_grass_bottom'],
    ['double_grass_top','tall_grass_top'],

    ['unlit_redstone_torch','redstone_torch_off'],
    ['unlit_redstone_torch_wall','redstone_wall_torch_off'],
    ['lit_redstone_torch','redstone_torch'],
    ['lit_redstone_torch_wall','redstone_wall_torch'],
    ['torch','template_torch'],
    ['torch_wall','torch_wall'],
    ['normal_torch','torch'],
    ['normal_torch_wall','wall_torch'],

    ['activator_rail_flat','activator_rail'],
    ['activator_rail_active_flat','activator_rail_on'],
    ['activator_rail_raised_ne','activator_rail_raised_ne'],
    ['activator_rail_active_raised_ne','activator_rail_on_raised_ne'],
    ['activator_rail_raised_sw','activator_rail_raised_sw'],
    ['activator_rail_active_raised_sw','activator_rail_on_raised_sw'],

    ['detector_rail_flat','detector_rail'],
    ['detector_rail_powered_flat','detector_rail_on'],
    ['detector_rail_raised_ne','detector_rail_raised_ne'],
    ['detector_rail_powered_raised_ne','detector_rail_on_raised_ne'],
    ['detector_rail_raised_sw','detector_rail_raised_sw'],
    ['detector_rail_powered_raised_sw','detector_rail_on_raised_sw'],

    ['golden_rail_flat','powered_rail'],
    ['golden_rail_active_flat','powered_rail_on'],
    ['golden_rail_raised_ne','powered_rail_raised_ne'],
    ['golden_rail_active_raised_ne','powered_rail_on_raised_ne'],
    ['golden_rail_raised_sw','powered_rail_raised_sw'],
    ['golden_rail_active_raised_sw','powered_rail_on_raised_sw'],

    ['normal_rail_curved','rail_corner'],
    ['normal_rail_flat','rail'],
    ['rail_raised_ne','template_rail_raised_ne'],
    ['rail_raised_sw','template_rail_raised_sw'],
    ['normal_rail_raised_ne','rail_raised_ne'],
    ['normal_rail_raised_sw','rail_raised_sw'],

    ['farmland','template_farmland'],
    ['farmland_dry','farmland'],
    ['anvil_slightly_damaged','chipped_anvil'],
    ['anvil_very_damaged','damaged_anvil'],

    ['dark_oak_door_bottom_rh', 'dark_oak_door_bottom_hinge'],
    ['dark_oak_door_top_rh', 'dark_oak_door_top_hinge'],

    ['wooden_button', 'oak_button'],
    ['wooden_button_inventory', 'oak_button_inventory'],
    ['wooden_button_pressed', 'oak_button_pressed'],

    ['lever_off', 'lever_on'],
    ['quartz_outer_stairs', 'quartz_stairs_outer'],
    ['quartz_inner_stairs', 'quartz_stairs_inner']
    ]

stateList = [
    ['grass','grass_block'],
    ['tall_grass','grass'],
    ['double_grass','tall_grass'],
    ['golden_rail','powered_rail'],

    ['wooden_door','oak_door'],

    ['mossy_brick_monster_egg','infested_mossy_stone_bricks'],
    ['stone_brick_monster_egg','infested_stone_bricks'],
    ['chiseled_brick_monster_egg','infested_chiseled_stone_bricks'],
    ['cracked_brick_monster_egg','infested_cracked_stone_bricks'],
    ['cobblestone_monster_egg','infested_cobblestone'],
    ['stone_monster_egg','infested_stone'],

    ['stonebrick','stone_bricks'],
    ['mossy_stonebrick','mossy_stone_bricks'],
    ['chiseled_stonebrick','chiseled_stone_bricks'],
    ['cracked_stonebrick','cracked_stone_bricks'],
    ['wooden_button', 'oak_button']
    ]
'''
---------------------------------------------------------------------------
                            change list
---------------------------------------------------------------------------
'''
#BLOCKLIST： Colored blocks
colorList = [
    'white',
    'orange',
    'magenta',
    'light_blue',
    'yellow',
    'lime',
    'pink',
    'gray',
    'light_gray',
    'cyan',
    'purple',
    'blue',
    'brown',
    'green',
    'red',
    'black'
    ]

for _str in colorList:
    blockList.append(['wool_colored_' + _str, _str + '_wool'])
    blockList.append(['glass_' + _str, _str + '_stained_glass'])
    blockList.append(['glass_pane_top_' + _str, _str + '_stained_glass_pane_top'])
    blockList.append(['hardened_clay_stained_' + _str, _str + '_terracotta'])
    blockList.append(['concrete_powder_' + _str, _str + '_concrete_powder'])
    blockList.append(['concrete_' + _str, _str + '_concrete'])
    blockList.append(['glazed_terracotta_' + _str, _str + '_glazed_terracotta'])
    blockList.append(['shulker_top_' + _str, _str + '_shulker_box_top'])

#BLOCKLIST： Stones
stoneList = [
    'andesite',
    'granite',
    'diorite'
    ]

for _str in stoneList:
    blockList.append(['stone_' + _str, _str])
    blockList.append(['stone_' + _str + '_smooth' , 'polished_' + _str])

blockList.append(['cobblestone_mossy', 'mossy_cobblestone'])
blockList.append(['stonebrick', 'stone_bricks'])
blockList.append(['stonebrick_carved', 'chiseled_stone_bricks'])
blockList.append(['stonebrick_cracked', 'cracked_stone_bricks'])
blockList.append(['stonebrick_mossy', 'mossy_stone_bricks'])

sandstoneList = [
    'sandstone',
    'red_sandstone'
    ]

for _str in sandstoneList:
    blockList.append([_str + '_normal' , _str])
    blockList.append([_str + '_carved' , 'chiseled_' + _str])
    blockList.append([_str + '_smooth' , 'cut_' + _str])

#BLOCKLIST： Grass/Dirt
blockList.append(['grass_side', 'grass_block_side'])
blockList.append(['grass_side_overlay', 'grass_block_side_overlay'])
blockList.append(['grass_side_snowed', 'grass_block_snow'])
blockList.append(['grass_top', 'grass_block_top'])
blockList.append(['dirt_podzol_side', 'podzol_side'])
blockList.append(['dirt_podzol_top', 'podzol_top'])
blockList.append(['farmland_dry', 'farmland'])
blockList.append(['farmland_wet', 'farmland_moist'])
blockList.append(['grass_normal', 'grass_block'])
blockList.append(['grass_snowed', 'grass_block_snow'])

blockList.append(['double_grass_bottom', 'tall_grass_bottom'])
blockList.append(['double_grass_top', 'tall_grass_top'])

#BLOCKLIST： Quartz
blockList.append(['quartz_block_chiseled', 'chiseled_quartz_block'])
blockList.append(['quartz_block_chiseled_top', 'chiseled_quartz_block_top'])
blockList.append(['quartz_block_lines', 'quartz_pillar'])
blockList.append(['quartz_block_lines_top', 'quartz_pillar_top'])


#BLOCKLIST： Crops
cropList = [
    'wheat',
    'carrots',
    'potatoes',
    'nether_wart',
    'beetroots',
    'cocoa'
    ]

for _str in cropList:
    for i in range(8):
        blockList.append([_str + '_stage_' + str(i), _str + '_stage' + str(i)])

blockList.append(['melon_stem_disconnected', 'melon_stem'])
blockList.append(['melon_stem_connected', 'attached_melon_stem'])
blockList.append(['pumpkin_stem_disconnected', 'pumpkin_stem'])
blockList.append(['pumpkin_stem_connected', 'attached_pumpkin_stem'])
blockList.append(['reeds', 'sugar_cane'])

#BLOCKLIST： Wooden Stuff
woodenList = [
    'oak',
    'birch',
    'spruce',
    'jungle',
    'acacia',
    'dark_oak'
    ]

for _str in woodenList:
    blockList.append(['log_' + _str , _str + '_log'])
    blockList.append(['log_' + _str + '_top', _str + '_log_top'])
    blockList.append(['planks_' + _str, _str + '_planks'])
    blockList.append(['sapling_' + _str, _str + '_sapling'])
    blockList.append(['leaves_' + _str, _str + '_leaves'])
    blockList.append(['door_' + _str + '_lower', _str + '_door_bottom'])
    blockList.append(['door_' + _str + '_upper', _str + '_door_top'])

blockList.append(['door_wood_lower', 'oak_door_bottom'])
blockList.append(['door_wood_upper', 'oak_door_top'])
blockList.append(['door_iron_lower', 'iron_door_bottom'])
blockList.append(['door_iron_upper', 'iron_door_top'])
blockList.append(['trapdoor', 'oak_trapdoor'])
blockList.append(['sapling_roofed_oak', 'dark_oak_sapling'])
#blockList.append(['dark_oak_door_bottom_rh', 'dark_oak_door_bottom_hinge'])
#blockList.append(['dark_oak_door_top_rh', 'dark_oak_door_top_hinge'])


#BLOCKLIST： Plants
flowerList = [
    'allium',
    'blue_orchid',
    'dandelion',
    'oxeye_daisy'
    ]

for _str in flowerList:
    blockList.append(['flower_' + _str , _str])

flowerTulipList = [
    'orange',
    'pink',
    'red',
    'white'
    ]

for _str in flowerTulipList:
    blockList.append(['flower_tulip_' + _str , _str + '_tulip'])

doublePlantList = [
    ['paeonia','peony'],
    ['rose','rose_bush'],
    ['sunflower','sunflower'],
    ['syringa','lilac'],
    ['fern','large_fern'],
    ['grass','tall_grass']
    ]

for _str in doublePlantList:
    blockList.append(['double_plant_' + _str[0] + '_bottom', _str[1] + '_bottom'])
    blockList.append(['double_plant_' + _str[0] + '_top' , _str[1] + '_top'])

blockList.append(['tallgrass', 'grass'])
blockList.append(['deadbush', 'dead_bush'])
blockList.append(['flower_houstonia', 'azure_bluet'])
blockList.append(['flower_rose', 'poppy'])
blockList.append(['double_plant_sunflower_back', 'sunflower_back'])
blockList.append(['double_plant_sunflower_front', 'sunflower_front'])

#BLOCKLIST： Mushrooms
blockList.append(['mushroom_block_skin_stem', 'mushroom_stem'])
blockList.append(['mushroom_block_skin_brown', 'brown_mushroom_block'])
blockList.append(['mushroom_block_skin_red', 'red_mushroom_block'])
blockList.append(['mushroom_red', 'red_mushroom'])
blockList.append(['mushroom_brown', 'brown_mushroom'])

#BLOCKLIST： Rails
#in texture
powerList = [
    'detector',
    'activator'
]
for _str in powerList:
    blockList.append(['rail_' + _str, _str + '_rail'])
    blockList.append(['rail_' + _str +'_powered', _str + '_rail_on'])

blockList.append(['rail_normal', 'rail'])
blockList.append(['rail_normal_turned', 'rail_corner'])
blockList.append(['rail_golden', 'powered_rail'])
blockList.append(['rail_golden_powered', 'powered_rail_on'])

#in other
'''blockList.append(['normal_rail_curved', 'rail_corner'])
blockList.append(['normal_rail_flat', 'rail'])
blockList.append(['normal_rail_raised_ne', 'rail_raised_ne'])
blockList.append(['normal_rail_raised_sw', 'rail_raised_sw'])

blockList.append(['activator_rail_flat', 'activator_rail'])
blockList.append(['activator_rail_active_flat', 'activator_rail_on'])
blockList.append(['activator_rail_active_raised_ne', 'activator_rail_on_raised_ne'])
blockList.append(['activator_rail_active_raised_sw', 'activator_rail_on_raised_sw'])
blockList.append(['activator_rail_raised_ne', 'activator_rail_raised_ne'])
blockList.append(['activator_rail_raised_sw', 'activator_rail_raised_sw'])

blockList.append(['detector_rail_flat', 'detector_rail'])
blockList.append(['detector_rail_powered_rail', 'detector_rail_on'])
blockList.append(['detector_rail_powered_raised_ne', 'detector_rail_on_raised_ne'])
blockList.append(['detector_rail_powered_raised_sw', 'detector_rail_on_raised_sw'])
blockList.append(['detector_rail_raised_ne', 'detector_rail_raised_ne'])
blockList.append(['detector_rail_raised_sw', 'detector_rail_raised_sw'])

blockList.append(['golden_rail_flat', 'powered_rail'])
blockList.append(['golden_rail_active_flat', 'powered_rail_on'])
blockList.append(['golden_rail_active_raised_ne', 'powered_rail_on_raised_ne'])
blockList.append(['golden_rail_active_raised_sw', 'powered_rail_on_raised_sw'])
blockList.append(['golden_rail_raised_ne', 'powered_rail_raised_ne'])
blockList.append(['golden_rail_raised_sw', 'powered_rail_raised_sw'])'''

#BLOCKLIST： Fire
blockList.append(['fire_layer_0', 'fire_0'])
blockList.append(['fire_layer_1', 'fire_1'])

#BLOCKLIST： Misc
blockList.append(['furnace_front_off', 'furnace_front'])
blockList.append(['dispenser_front_horizontal', 'dispenser_front'])
blockList.append(['dropper_front_horizontal', 'dropper_front'])
blockList.append(['observer_back_lit', 'observer_back_on'])
blockList.append(['torch_on', 'torch'])
blockList.append(['redstone_torch_on', 'redstone_torch'])
blockList.append(['repeater_off', 'repeater'])
blockList.append(['comparator_off', 'comparator'])
blockList.append(['web', 'cobweb'])
blockList.append(['pumpkin_face_on', 'jack_o_lantern'])
blockList.append(['pumpkin_face_off', 'carved_pumpkin'])
blockList.append(['end_bricks', 'end_stone_bricks'])
blockList.append(['endframe_eye', 'end_portal_frame_eye'])
blockList.append(['endframe_side', 'end_portal_frame_side'])
blockList.append(['endframe_top', 'end_portal_frame_top'])
blockList.append(['piston_top_normal', 'piston_top'])
blockList.append(['anvil_base', 'anvil'])
blockList.append(['anvil_top_damaged_0', 'anvil_top'])
blockList.append(['rail_activator', 'activator_rail'])
blockList.append(['anvil_top_damaged_1', 'chipped_anvil_top'])
blockList.append(['anvil_top_damaged_2', 'damaged_anvil_top'])
blockList.append(['noteblock', 'note_block'])
blockList.append(['slime', 'slime_block'])
blockList.append(['sponge_wet', 'wet_sponge'])
blockList.append(['hardened_clay', 'terracotta'])
blockList.append(['trip_wire_source', 'trip_wire_hook'])
blockList.append(['trip_wire_hook', 'tripwire_hook'])
blockList.append(['waterlily', 'lily_pad'])
blockList.append(['prismarine_rough', 'prismarine'])
blockList.append(['prismarine_dark', 'dark_prismarine'])
blockList.append(['ice_packed', 'packed_ice'])
blockList.append(['redstone_lamp_off', 'redstone_lamp'])
blockList.append(['brick', 'bricks'])
blockList.append(['nether_brick', 'nether_bricks'])
blockList.append(['red_nether_brick', 'red_nether_bricks'])
blockList.append(['trip_wire', 'tripwire'])
blockList.append(['portal', 'nether_portal'])
blockList.append(['quartz_ore', 'nether_quartz_ore'])
blockList.append(['itemframe_background', 'item_frame'])
blockList.append(['mob_spawner', 'spawner'])

#blockList.append(['anvil_undamaged', 'anvil'])
#blockList.append(['anvil_slightly_damaged', 'chipped_anvil'])
#blockList.append(['anvil_very_damaged', 'damaged_anvil'])

#blockList.append(['normal_torch', 'torch'])
#blockList.append(['normal_torch_wall', 'wall_torch'])
blockList.append(['unlit_redstone_torch', 'redstone_torch_off'])
blockList.append(['unlit_redstone_torch_wall', 'redstone_wall_torch_off'])
blockList.append(['lit_redstone_torch', 'redstone_torch'])
blockList.append(['lit_redstone_torch_wall', 'redstone_wall_torch'])

#blockList.append(['cobblestone_wall_mossy_inventory', 'mossy_cobblestone_wall_inventory'])

blockList.append(['wooden_button', 'oak_button'])
blockList.append(['wooden_button_inventory', 'oak_button_inventory'])
blockList.append(['wooden_button_pressed', 'oak_button_pressed'])
#ITEMLIST： Tools and Armor
toolList = [
    'wood',
    'gold'
    ]

for _str in toolList:
    itemList.append([_str + '_pickaxe' , _str + 'en_pickaxe'])
    itemList.append([_str + '_sword' , _str + 'en_sword'])
    itemList.append([_str + '_shovel' , _str + 'en_shovel'])
    itemList.append([_str + '_hoe' , _str + 'en_hoe'])
    itemList.append([_str + '_axe' , _str + 'en_axe'])

itemList.append(['gold_horse_armor', 'golden_horse_armor'])
itemList.append(['gold_helmet', 'golden_helmet'])
itemList.append(['gold_chestplate', 'golden_chestplate'])
itemList.append(['gold_leggings', 'golden_leggings'])
itemList.append(['gold_boots', 'golden_boots'])
itemList.append(['bow_standby', 'bow'])
itemList.append(['fishing_rod_uncast', 'fishing_rod'])
#ITEMLIST： Doors
doorList = [
    'iron',
    'birch',
    'jungle',
    'spruce',
    'dark_oak',
    'acacia'
    ]

for _str in doorList:
    itemList.append(['door_' + _str, _str + '_door'])

itemList.append(['door_wood', 'oak_door'])
#ITEMLIST： Food
rawList = [
    'porkchop',
    'rabbit',
    'beef',
    'chicken',
    'mutton',
    'fish_salmon',
    'fish_cod',
    'fish_pufferfish',
    'fish_clownfish'
    ]

for _str in rawList:
    itemList.append([_str + '_raw' , _str])

cookedList = [
    'porkchop',
    'rabbit',
    'beef',
    'chicken',
    'mutton',
    'fish_salmon',
    'fish_cod',
    ]

for _str in cookedList:
    itemList.append([_str + '_cooked' , 'cooked_' + _str])

itemList.append(['potato_baked', 'baked_potato'])
itemList.append(['potato_poisonous', 'poisonous_potato'])
itemList.append(['carrot_golden', 'golden_carrot'])
itemList.append(['reeds', 'sugar_cane'])
itemList.append(['apple_golden', 'golden_apple'])
itemList.append(['melon_speckled', 'glistering_melon_slice'])
itemList.append(['chorus_fruit_popped', 'popped_chorus_fruit'])
itemList.append(['clownfish', 'tropical_fish'])
itemList.append(['melon', 'melon_slice'])
#ITEMLIST： Music Discs
cdList = [
    '11',
    '13',
    'mall',
    'cat',
    'far',
    'chirp',
    'wait',
    '_strad',
    'ward',
    'blocks',
    'mellohi',
    'stal'
    ]

for _str in cdList:
    itemList.append(['record_' + _str, 'music_disc_' + _str])

#ITEMLIST： Dyes
for _str in colorList:
    itemList.append(['dye_powder_' + _str, _str + '_dye'])

#ITEMLIST： Minecarts
cartList = [
    'chest',
    'tnt',
    'command_block',
    'hopper',
    'furnace',
    ]

for _str in cartList:
    itemList.append(['minecart_' + _str, _str + '_minecart'])

itemList.append(['minecart_normal', 'minecart'])

#ITEMLIST： Books
bookList = [
    'enchanted',
    'written',
    'writable'
    ]

for _str in bookList:
    itemList.append(['book_' + _str, _str + '_book'])

itemList.append(['book_normal', 'book'])

#ITEMLIST： Buckets
bucketList = [
    'water',
    'lava',
    'milk'
    ]

for _str in bucketList:
    itemList.append(['bucket_' + _str, _str + '_bucket'])

itemList.append(['bucket_empty', 'bucket'])

#ITEMLIST： Seeds
seedList = [
    'wheat',
    'pumpkin',
    'melon'
    ]

for _str in seedList:
    itemList.append(['seeds_' + _str, _str + '_seeds'])

#ITEMLIST： Misc
itemList.append(['totem', 'totem_of_undying'])
itemList.append(['potion_bottle_lingering', 'lingering_potion'])
itemList.append(['potion_bottle_drinkable', 'potion'])
itemList.append(['potion_bottle_splash', 'splash_potion'])
itemList.append(['potion_bottle_empty', 'glass_bottle'])
itemList.append(['fireball', 'fire_charge'])
itemList.append(['slimeball', 'slime_ball'])
itemList.append(['redstone_dust', 'redstone'])
itemList.append(['fireworks', 'firework_rocket'])
itemList.append(['wooden_armorstand', 'armor_stand'])
itemList.append(['fireworks_charge', 'firework_star'])
itemList.append(['fireworks_charge_overlay', 'firework_star_overlay'])
itemList.append(['spider_eye_fermented', 'fermented_spider_eye'])
itemList.append(['netherbrick', 'nether_brick'])
itemList.append(['map_empty', 'map'])

#ENTITYLIST： Shulker
entityList.append(['shulker/shulker_silver', 'shulker/shulker_light_gray'])
entityList.append(['shulker/shulker_purple', 'shulker/shulker'])

#ENTITYLIST： Bed
entityList.append(['bed/silver', 'bed/light_gray'])

#ENTITYLIST： Illager
entityList.append(['illager/fangs', 'illager/evoker_fangs.png'])

#ENTITYLIST： Wither
entityList.append(['wither/wither_invul.png', 'wither/wither_invulnerable'])

#ENTITYLIST： Llama
llamaList = [
    'brown',
    'creamy',
    'gray',
    'white'
    ]

for _str in llamaList:
    itemList.append(['llama/llama_' + _str, 'llama/' + _str])

#ENTITYLIST： Decor
for _str in colorList:
    itemList.append(['decor/decor_' + _str, 'decor/' + _str])

#ENTITYLIST： Boat
bootList = [
    'acacia',
    'birch',
    'dark_oak',
    'jungle',
    'oak',
    'spruce'
    ]

for _str in llamaList:
    itemList.append(['boat/boat_' + _str, 'boat/' + _str])

#ENTITYLIST： End Crystal
entityList.append(['endercrystal/endercrystal', 'endercrystal/end_crystal'])
entityList.append(['endercrystal/endercrystal_beam', 'endercrystal/end_crystal_beam'])
