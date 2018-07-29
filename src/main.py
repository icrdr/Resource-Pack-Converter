import os
import json
import cv2
import numpy as np
import zipfile
import shutil
import math
from onefile import *

blockList = []
itemList = []
entityList = []
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

#BLOCKLIST： Quartz
blockList.append(['quartz_block_chiseled', 'chiseled_quartz_block'])
blockList.append(['quartz_block_chiseled_top', 'chiseled_quartz_block_top'])
blockList.append(['quartz_block_lines', 'quartz_pillar'])
blockList.append(['quartz_block_lines_top', 'quartz_pillar_top'])
blockList.append(['quartz_outer_stairs', 'quartz_stairs_outer'])
blockList.append(['quartz_inner_stairs', 'quartz_stairs_inner'])

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
blockList.append(['rail_normal', 'rail'])
blockList.append(['rail_normal_turned', 'rail_corner'])
blockList.append(['rail_activator', 'activator_rail'])
blockList.append(['rail_activator_powered', 'activator_rail_on'])
blockList.append(['rail_detector', 'detector_rail'])
blockList.append(['rail_detector_powered', 'detector_rail_on'])
blockList.append(['rail_golden', 'powered_rail'])
blockList.append(['rail_golden_powered', 'powered_rail_on'])

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
    'wood',
    'iron',
    'birch',
    'jungle',
    'spruce',
    'dark_oak',
    'acacia'
    ]

for _str in doorList:
    itemList.append(['door_' + _str, _str + '_door'])

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

def init(pack,res_r):
    global RES_R, PACK, MAIN_PATH, TEX_PATH, block_path, item_path, entity_path
    if(res_r<1):res_r=1
    RES_R = int(math.pow(2, res_r-1))
    PACK = pack
    MAIN_PATH = PACK + '/assets/minecraft/'
    TEX_PATH =  MAIN_PATH+ 'textures/'
    block_path = TEX_PATH+ 'blocks/'
    item_path = TEX_PATH+ 'items/'
    entity_path = TEX_PATH+ 'entity/'

'''
---------------------------------------------------------------------------
                               unzip pack
---------------------------------------------------------------------------
'''
def unzipPack():
    print ("unzipping pack...")
    azip = zipfile.ZipFile(PACK + '.zip')
    azip.extractall(PACK)

'''
---------------------------------------------------------------------------
                            change files'name
---------------------------------------------------------------------------
'''
def changeFileName():
    print ("changing texs'name...")
    for name in blockList:
        try:
            #change file name
            os.rename(block_path + name[0] + '.png', block_path + name[1] + '.png')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0])

    for name in itemList:
        try:
            #change file name
            os.rename(item_path + name[0] + '.png', item_path + name[1] + '.png')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0])

    for name in entityList:
        try:
            #change file name
            os.rename(entity_path + name[0] + '.png', entity_path + name[1] + '.png')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0])

    #print ("static texs'name conversion is completed!")

    for name in blockList:
        try:
            #change file name (animations?)
            os.rename(block_path + name[0] + '.png.mcmeta', block_path + name[1] + '.png.mcmeta')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0])

    for name in itemList:
        try:
            #change file name (animations?)
            os.rename(item_path + name[0] + '.png.mcmeta', item_path + name[1] + '.png.mcmeta')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0])

    for name in entityList:
        try:
            #change file name (animations?)
            os.rename(entity_path + name[0] + '.png.mcmeta', entity_path + name[1] + '.png.mcmeta')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0])

    #print ("dynamic texs'name conversion is completed!")
    try:
        os.rename(MAIN_PATH + 'models/block/cobblestone_wall_mossy_inventory.json',MAIN_PATH + 'models/block/mossy_cobblestone_wall_inventory.json')
    except IOError:
        print ("Error: fail to read cobblestone_wall_mossy_inventory")
'''
---------------------------------------------------------------------------
                            change folders'name
---------------------------------------------------------------------------
'''
def changeFolderName():
    print ("changing folders'name...")
    try:
        os.rename(entity_path + 'endercrystal', entity_path + 'end_crystal')
        #os.rename(entity_path + 'horse', entity_path + '.horse')

        os.rename(TEX_PATH + 'blocks', TEX_PATH + 'block')
        os.rename(TEX_PATH + 'items', TEX_PATH + 'item')
        #os.rename(TEX_PATH + 'particle', TEX_PATH + '.particle')

    except IOError:
        pass
'''
---------------------------------------------------------------------------
                     change state/model files'content
---------------------------------------------------------------------------
'''
def changeModel():
    print ("converting models...")
    def alter(file,old_str,new_str):
        file_data = ""
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    if old_str in line:
                        line = line.replace(old_str,new_str)
                    file_data += line

            with open(file,"w", encoding="utf-8") as f:
                f.write(file_data)
        except:
            print(file + "fail to replace name in content")
    def alterAll(file):
        for name in blockList:
            alter(file, '/' + name[0] + '"', '/' + name[1] + '"')
        for name in itemList:
            alter(file, '/' + name[0] + '"', '/' + name[1] + '"')
        alter(file, 'blocks/', 'block/')
        alter(file, 'items/', 'item/')
        print (file + " is OK")

    if(os.path.exists(MAIN_PATH + 'models/block/')):
        blockModelList = (file for file in os.listdir(MAIN_PATH + 'models/block/')
                 if file.endswith('.json'))
        for model in blockModelList:
            alterAll(MAIN_PATH + 'models/block/' + model)

    if(os.path.exists(MAIN_PATH + 'models/item/')):
        itemModelList = (file for file in os.listdir(MAIN_PATH + 'models/item/')
                 if file.endswith('.json'))
        for model in itemModelList:
            alterAll(MAIN_PATH + 'models/item/' + model)

    if(os.path.exists(MAIN_PATH + 'blockstates/')):
        blockstateList = (file for file in os.listdir(MAIN_PATH + 'blockstates/')
                 if file.endswith('.json'))
        for state in blockstateList:
            #for 1.13

            alter(MAIN_PATH + 'blockstates/' + state, '"model": "block/', '"model": "')
            alter(MAIN_PATH + 'blockstates/' + state, '"model": "', '"model": "block/')
            alterAll(MAIN_PATH + 'blockstates/' + state)

    def changeTorchState(_str):
        try:
            with open(MAIN_PATH + 'blockstates/'+ _str+ 'torch.json','r') as load_f:
                torch_dict = json.load(load_f)
            if 'facing=up' in torch_dict['variants']:
                torch_json = {
                    'variants' : {
                        "": torch_dict['variants']["facing=up"]
                        }
                }
                #print(torch_json)
                with open(MAIN_PATH + 'blockstates/'+ _str+ 'torch.json','w') as dump_f:
                    json.dump(torch_json,dump_f)

            if 'facing=east' in torch_dict['variants']:
                if 'facing=up' in torch_dict['variants']:
                    del torch_dict['variants']["facing=up"]
                wall_torch_json = torch_dict
                #print(wall_torch_json)

                with open(MAIN_PATH + 'blockstates/'+ _str+ 'wall_torch.json','w') as dump_f:
                    json.dump(wall_torch_json,dump_f)
        except IOError:
            print ("Error: fail to read " + _str + "torch state")

    changeTorchState('')
    changeTorchState('redstone_')

    def changeRailModel(_str):
        if (os.path.exists(MAIN_PATH + 'models/block/template_rail_raised_' + _str + '.json')):
            return false
        try:
            os.rename(
                MAIN_PATH + 'models/block/rail_raised_' + _str + '.json',
                MAIN_PATH + 'models/block/template_rail_raised_' + _str + '.json'
                )

            railList = [
                'detector_',
                'powered_',
                'activator_'
                '',
                ]

            for _type in railList:
                rail_json = {
                    "parent": "block/template_rail_raised_" + _str,
                    "textures": {
                        "rail": "block/" + _type + "rail"
                    }
                }
                    #print(torch_json)
                with open(MAIN_PATH + 'models/block/' + _type + 'rail_raised_'+ _str+ '.json','w') as dump_f:
                    json.dump(rail_json,dump_f)

        except IOError:
            print ("Error: fail to read " + _str + " rail model")

    changeRailModel('sw')
    changeRailModel('ne')

'''
---------------------------------------------------------------------------
                           resize change tex
---------------------------------------------------------------------------
'''
def resizeTex():
    print ("converting texs...")
    def overlayImg(over_img, base_img, x_offset=0, y_offset=0):
        x1, x2 = x_offset * RES_R, x_offset * RES_R + over_img.shape[1]
        y1, y2 = y_offset * RES_R, y_offset * RES_R + over_img.shape[0]
        alpha_s = over_img[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s

        for c in range(0, 3):
            base_img[y1:y2, x1:x2, c] = (alpha_s * over_img[:, :, c] + alpha_l * base_img[y1:y2, x1:x2, c])
        base_img[y1:y2, x1:x2, 3] = over_img[:, :, 3]
        return base_img

    def cutImg(img,y1,y2,x1,x2):
        return img[y1*RES_R:y2*RES_R, x1*RES_R:x2*RES_R, :]

    if(os.path.exists(TEX_PATH + 'particle/particles.png') and not(os.path.exists(TEX_PATH + 'particle/1.13'))):
        p_img = cv2.imread(TEX_PATH + 'particle/particles.png',-1)
        p_img = cv2.resize(p_img,(128 * RES_R, 128 * RES_R),interpolation=cv2.INTER_NEAREST)

        p_o_img = cv2.imread(resource_path('particles.png'),-1)
        p_o_img = cv2.resize(p_o_img,(256 * RES_R, 256 * RES_R),interpolation=cv2.INTER_NEAREST)

        n_p_img = np.zeros((256 * RES_R, 256 * RES_R, 4), dtype=np.uint8)
        n_p_img = overlayImg(p_img, n_p_img)
        n_p_img = overlayImg(cutImg(p_o_img,104,112, 0,8), n_p_img,0,104)
        n_p_img = overlayImg(cutImg(p_o_img,128,152, 0,88), n_p_img,0,128)
        #print(n_p_img[:, : ,3])
        cv2.imwrite(TEX_PATH + 'particle/particles.png', n_p_img)
        print(TEX_PATH + 'particle/particles.png' + ' conversion is OK')
        open(TEX_PATH + 'particle/1.13','w')
        #cv2.imshow("image", n_p_img)
        #cv2.waitKey(0)

    if(os.path.exists(TEX_PATH + 'map/map_icons.png') and not(os.path.exists(TEX_PATH + 'map/1.13'))):
        m_img = cv2.imread(TEX_PATH + 'map/map_icons.png',-1)
        m_img = cv2.resize(m_img,(32 * RES_R, 32 * RES_R),interpolation=cv2.INTER_NEAREST)

        m_o_img = cv2.imread(resource_path('map_icons.png'),-1)
        m_o_img = cv2.resize(m_o_img,(128 * RES_R, 128 * RES_R),interpolation=cv2.INTER_NEAREST)

        n_m_img = np.zeros((128 * RES_R, 128 * RES_R, 4), dtype=np.uint8)
        n_m_img = overlayImg(cutImg(m_img,0,8, 0,32), n_m_img,0,0)
        n_m_img = overlayImg(cutImg(m_img,0,16, 8,32), n_m_img,32,0)
        n_m_img = overlayImg(cutImg(m_img,16,24, 0,16), n_m_img,64,0)
        n_m_img = overlayImg(cutImg(m_o_img,0,8, 80,128), n_m_img,80,0)
        n_m_img = overlayImg(cutImg(m_o_img,8,16, 0,128), n_m_img,0,8)
        #print(n_p_img[:, : ,3])
        cv2.imwrite(TEX_PATH + 'map/map_icons.png', n_m_img)
        print(TEX_PATH + 'map/map_icons.png' + ' conversion is OK')
        open(TEX_PATH + 'map/1.13','w')
        #cv2.imshow("image", n_p_img)
        #cv2.waitKey(0)

    def changeHorseTex(file):
        h_img = cv2.imread(file,-1)
        h_img = cv2.resize(h_img,(128 * RES_R, 128 * RES_R),interpolation=cv2.INTER_NEAREST)

        n_h_img = np.zeros((64 * RES_R, 64 * RES_R, 4), dtype=np.uint8)

        #head
        n_h_img = overlayImg(cutImg(h_img,0,12, 0,24), n_h_img,0,13)
        n_h_img = overlayImg(cutImg(h_img,0,12, 9,24), n_h_img,10,13)
        n_h_img = overlayImg(cutImg(h_img,0,7, 14,17), n_h_img,16,13)
        n_h_img = overlayImg(cutImg(h_img,7,12, 21,24), n_h_img,23,20)

        #ear
        n_h_img = overlayImg(cutImg(h_img,12,20, 0,6), n_h_img,0,12)
        n_h_img = overlayImg(cutImg(h_img,0,4, 0,6), n_h_img,19,16)

        #morth
        n_h_img = overlayImg(cutImg(h_img,19,27, 25,43), n_h_img,0,25)
        n_h_img = overlayImg(cutImg(h_img,32,34, 24,42), n_h_img,0,33)
        n_h_img = overlayImg(cutImg(h_img,27,32, 33,37), n_h_img,9,25)

        #neck
        n_h_img = overlayImg(cutImg(h_img,21,33, 0,7), n_h_img,0,42)
        n_h_img = overlayImg(cutImg(h_img,21,33, 8,12), n_h_img,7,42)
        n_h_img = overlayImg(cutImg(h_img,21,33, 13,20), n_h_img,11,42)
        n_h_img = overlayImg(cutImg(h_img,21,33, 20,24), n_h_img,18,42)

        n_h_img = overlayImg(cutImg(h_img,12,19, 8,16), n_h_img,7,35)

        #horsehair
        n_h_img = overlayImg(cutImg(h_img,4,20, 58,60), n_h_img,56,38)
        n_h_img = overlayImg(cutImg(h_img,4,20, 62,64), n_h_img,58,38)
        n_h_img = overlayImg(cutImg(h_img,4,20, 65,67), n_h_img,60,38)
        n_h_img = overlayImg(cutImg(h_img,4,20, 67,69), n_h_img,62,38)

        n_h_img = overlayImg(cutImg(h_img,2,4, 62,66), n_h_img,58,36)

        #body
        n_h_img = overlayImg(cutImg(h_img,58,68, 0,22), n_h_img,0,54)
        n_h_img = overlayImg(cutImg(h_img,58,68, 13,24), n_h_img,11,54)

        n_h_img = overlayImg(cutImg(h_img,58,68, 24,34), n_h_img,22,54)

        n_h_img = overlayImg(cutImg(h_img,58,68, 34,56), n_h_img,32,54)
        n_h_img = overlayImg(cutImg(h_img,58,68, 47,57), n_h_img,43,54)

        n_h_img = overlayImg(cutImg(h_img,58,68, 58,68), n_h_img,54,54)
        n_h_img = overlayImg(cutImg(h_img,34,56, 24,44), n_h_img,22,32)
        n_h_img = overlayImg(cutImg(h_img,49,58, 24,44), n_h_img,22,45)

        #chest
        n_h_img = overlayImg(cutImg(h_img,34,45, 0,11), n_h_img,26,21)
        n_h_img = overlayImg(cutImg(h_img,47,58, 11,22), n_h_img,37,21)

        #foot
        n_h_img = overlayImg(cutImg(h_img,35,41, 97,113), n_h_img,48,25)
        n_h_img = overlayImg(cutImg(h_img,49,51, 96,104), n_h_img,48,31)
        n_h_img = overlayImg(cutImg(h_img,49,51, 96,104), n_h_img,56,31)
        n_h_img = overlayImg(cutImg(h_img,55,58, 96,112), n_h_img,48,33)
        n_h_img = overlayImg(cutImg(h_img,29,33, 101,105), n_h_img,52,21)
        n_h_img = overlayImg(cutImg(h_img,51,55, 104,108), n_h_img,56,21)

        #rein
        n_h_img = overlayImg(cutImg(h_img,0,4, 74,80), n_h_img,29,5)
        #n_h_img = overlayImg(cutImg(h_img,24,29, 81,83), n_h_img,1,7)
        #n_h_img = overlayImg(cutImg(h_img,24,29, 81,83), n_h_img,25,2)
        #n_h_img = overlayImg(cutImg(h_img,24,29, 86,88), n_h_img,17,7)
        #n_h_img = overlayImg(cutImg(h_img,24,29, 86,88), n_h_img,19,2)

        #tail?
        n_h_img = overlayImg(np.rot90(cutImg(h_img,10,14, 34,41),-1), n_h_img,42,47)
        n_h_img = overlayImg(np.rot90(cutImg(h_img,3,10, 31,37),-2), n_h_img,46,47)
        n_h_img = overlayImg(np.rot90(cutImg(h_img,10,14, 24,31),1), n_h_img,52,47)

        n_h_img = overlayImg(np.rot90(cutImg(h_img,14,18, 48,55),-1), n_h_img,42,40)
        n_h_img = overlayImg(np.rot90(cutImg(h_img,7,14, 45,51),-2), n_h_img,46,40)
        n_h_img = overlayImg(np.rot90(cutImg(h_img,14,18, 38,45),1), n_h_img,52,40)
        n_h_img = overlayImg(cutImg(h_img,14,18, 45,48), n_h_img,46,36)

        #sella
        n_h_img = overlayImg(cutImg(h_img,0,9, 88,98), n_h_img,35,0)
        n_h_img = overlayImg(cutImg(h_img,9,11, 89,98), n_h_img,26,9)
        n_h_img = overlayImg(cutImg(h_img,9,11, 89,98), n_h_img,45,9)

        cv2.imwrite(file, n_h_img)
        print(file + ' conversion is OK')
        #cv2.imshow("image", n_h_img)
        #cv2.waitKey(0)

    if(os.path.exists(TEX_PATH + 'entity/horse/') and not(os.path.exists(TEX_PATH + 'entity/horse/1.13'))):
        horseList = (file for file in os.listdir(TEX_PATH + 'entity/horse/')
                 if file.endswith('.png'))
        for horse in horseList:
            changeHorseTex(TEX_PATH + 'entity/horse/' + horse)
        open(TEX_PATH + 'entity/horse/1.13','w')

        if(os.path.exists(TEX_PATH + 'entity/horse/armor') and not(os.path.exists(TEX_PATH + 'entity/horse/armor/1.13'))):
            armorList = (file for file in os.listdir(TEX_PATH + 'entity/horse/armor')
                     if file.endswith('.png'))
            for armor in armorList:
                changeHorseTex(TEX_PATH + 'entity/horse/armor/' + armor)
            open(TEX_PATH + 'entity/horse/armor/1.13','w')

'''
---------------------------------------------------------------------------
                        change pack's info
---------------------------------------------------------------------------
'''
def changeInfo():
    with open(PACK + '/pack.mcmeta','r') as load_f:
        pack_info = json.load(load_f)

    #print(pack_info)
    pack_info['pack']['pack_format'] = 4
    pack_info['pack']['description'] = pack_info['pack']['description'].replace(" fit for 1.13 by icrdr","")
    pack_info['pack']['description'] += " fit for 1.13 by icrdr"
    #print(pack_info)
    with open(PACK + '/pack.mcmeta','w') as dump_f:
        json.dump(pack_info,dump_f)

'''
---------------------------------------------------------------------------
                                zip pack
---------------------------------------------------------------------------
'''
def zipPack():
    print ("CONVERTION DONE!")
    print ("zipping pack...")

    azip = zipfile.ZipFile(PACK + '_for_1.13_by_icrdr.zip', 'w')
    for root, dirs, files in os.walk(PACK):
        for name in files:
            azip.write(os.path.join(root, name),os.path.join(root, name)[len(PACK)+1:])
            print(os.path.join(root, name)[len(PACK)+1:])
    azip.close()

    print ("deleting temp...")
    #delete folder
    try:
        shutil.rmtree(PACK)
    except:
        print('fail to delete unziped file. u may delete them by yourself.')

def main(pack,res_r = 1):
  init(pack, res_r)
  unzipPack()
  changeFileName()
  changeFolderName()
  changeModel()
  resizeTex()
  changeInfo()
  zipPack()
  print ("ALL DONE!")

if __name__ == '__main__':
  main('pack',1)
