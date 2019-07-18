import os
import json
from PIL import Image
import numpy as np
import zipfile
import shutil
import math
from onefile import *
from changes import *

def detectRes():
    if(os.path.exists(block_path)):
        searchfold = block_path
    elif(os.path.exists(item_path)):
        searchfold = item_path
    else:
        return False

    selected = list(file for file in os.listdir(searchfold)
             if file.endswith('.png'))[0]

    tex = Image.open(searchfold + selected)
    print(tex.size)
    ro = 0
    while math.pow(2, ro) < (tex.size[0]/16):
        ro += 1
    print('resolution: ' +  str(tex.size[0]) + '  ro: ' + str(ro))
    if (ro<0):ro=0
    return ro

def alter(f, old_str, new_str):
    file_data = ""
    for line in f:
        line = line.replace(old_str,new_str)
        file_data += line
    return file_data

def alterAllModels(f):
    file_data = ""
    for line in f:
        line = line.replace('"blocks/','"block/')
        line = line.replace('"items/','"item/')
        for name in blockList:
            line = line.replace('"block/' + name[0] + '"','"block/' + name[1] + '"')
        for name in itemList:
            line = line.replace('"item/' + name[0] + '"','"item/' + name[1] + '"')

        for name in modelList:
            line = line.replace('"parent": "block/' + name[0] + '"','"parent": "block/' + name[1] + '"')
        file_data += line
    return file_data

def alterAllStates(f):
    file_data = ""
    for line in f:
        line = line.replace('"model": "', '"model": "block/')
        for name in modelList:
            line = line.replace('"model": "block/' + name[0] + '"','"model": "block/' + name[1] + '"')
        file_data += line
    return file_data

def modifyJson(f):
    lines = []
    for line in f:
        if (len(line) > 0):
            lines.append(line)
    return lines
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
'''
                            static textures' name
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
            print ("Error: fail to read " + name[0] + '.png')

    for name in itemList:
        try:
            #change file name
            os.rename(item_path + name[0] + '.png', item_path + name[1] + '.png')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0] + '.png')

    for name in entityList:
        try:
            #change file name
            os.rename(entity_path + name[0] + '.png', entity_path + name[1] + '.png')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0] + '.png')

    #print ("static texs'name conversion is completed!")

    '''
                                dynamic textures' name
    ---------------------------------------------------------------------------
    '''
    for name in blockList:
        try:
            #change file name (animations?)
            os.rename(block_path + name[0] + '.png.mcmeta', block_path + name[1] + '.png.mcmeta')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0] + '.png.mcmeta')

    for name in itemList:
        try:
            #change file name (animations?)
            os.rename(item_path + name[0] + '.png.mcmeta', item_path + name[1] + '.png.mcmeta')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0] + '.png.mcmeta')

    for name in entityList:
        try:
            #change file name (animations?)
            os.rename(entity_path + name[0] + '.png.mcmeta', entity_path + name[1] + '.png.mcmeta')
            print (name[0] + " changed to " + name[1])
        except IOError:
            print ("Error: fail to read " + name[0] + '.png.mcmeta')
    #print ("dynamic texs'name conversion is completed!")

    '''
                                models' name
    ---------------------------------------------------------------------------
    '''
    for name in modelList:
        try:
            os.rename(
                MAIN_PATH + 'models/block/' + name[0] + '.json',
                MAIN_PATH + 'models/block/' + name[1] + '.json'
                )
        except IOError:
            print ("Error: fail to read" + name[0] + '.json')

    for name in stateList:
        try:
            os.rename(
                MAIN_PATH + 'models/item/' + name[0] + '.json',
                MAIN_PATH + 'models/item/' + name[1] + '.json'
                )
        except IOError:
            print ("Error: fail to read" + name[0] + '.json')
    '''
                                bloackstates' name
    ---------------------------------------------------------------------------
    '''
    for name in stateList:
        try:
            os.rename(
                MAIN_PATH + 'blockstates/' + name[0] + '.json',
                MAIN_PATH + 'blockstates/' + name[1] + '.json',
                )
        except IOError:
            print ("Error: fail to read " + name[0] + '.json')

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
    '''
                                models' content
    ---------------------------------------------------------------------------
    '''
    #BLOCK MODEL
    if(os.path.exists(MAIN_PATH + 'models/block/')):
        blockModelList = (file for file in os.listdir(MAIN_PATH + 'models/block/')
                 if file.endswith('.json'))
        for model in blockModelList:
            #change all textures & models' name in model file
            with open(MAIN_PATH + 'models/block/' + model, "r", encoding="utf-8") as f:
                fileData = alterAllModels(f)

            with open(MAIN_PATH + 'models/block/' + model, "w", encoding="utf-8") as f:
                f.write(fileData)
            print(model + ' is OK')

    #ITEM MODEL
    if(os.path.exists(MAIN_PATH + 'models/item/')):
        itemModelList = (file for file in os.listdir(MAIN_PATH + 'models/item/')
                 if file.endswith('.json'))
        for model in itemModelList:
            #change all textures & models' name in model file
            with open(MAIN_PATH + 'models/item/' + model, "r", encoding="utf-8") as f:
                fileData = alterAllModels(f)

            with open(MAIN_PATH + 'models/item/' + model, "w", encoding="utf-8") as f:
                f.write(fileData)
            print(model + ' is OK')

    #merge grasss_block and grass_normal
    if(os.path.exists(MAIN_PATH + 'models/block/grass_block.json')):
        with open(MAIN_PATH + 'models/block/grass_block.json','r') as f:
            grass_block_json = json.loads("\n".join(modifyJson(f)))

        if 'elements' not in grass_block_json:
            grass_block_json['elements'] = [
                {   "from": [ 0, 0, 0 ],
                    "to": [ 16, 16, 16 ],
                    "faces": {
                        "down":  { "uv": [ 0, 0, 16, 16 ], "texture": "#bottom", "cullface": "down" },
                        "up":    { "uv": [ 0, 0, 16, 16 ], "texture": "#top",    "cullface": "up", "tintindex": 0 },
                        "north": { "uv": [ 0, 0, 16, 16 ], "texture": "#side",   "cullface": "north" },
                        "south": { "uv": [ 0, 0, 16, 16 ], "texture": "#side",   "cullface": "south" },
                        "west":  { "uv": [ 0, 0, 16, 16 ], "texture": "#side",   "cullface": "west" },
                        "east":  { "uv": [ 0, 0, 16, 16 ], "texture": "#side",   "cullface": "east" }
                    }
                },
                {   "from": [ 0, 0, 0 ],
                    "to": [ 16, 16, 16 ],
                    "faces": {
                        "north": { "uv": [ 0, 0, 16, 16 ], "texture": "#overlay", "tintindex": 0, "cullface": "north" },
                        "south": { "uv": [ 0, 0, 16, 16 ], "texture": "#overlay", "tintindex": 0, "cullface": "south" },
                        "west":  { "uv": [ 0, 0, 16, 16 ], "texture": "#overlay", "tintindex": 0, "cullface": "west" },
                        "east":  { "uv": [ 0, 0, 16, 16 ], "texture": "#overlay", "tintindex": 0, "cullface": "east" }
                    }
                }
            ]

        if(os.path.exists(MAIN_PATH + 'models/block/grass_normal.json')):
            with open(MAIN_PATH + 'models/block/grass_normal.json','r') as f:
                grass_normal_json = json.loads("\n".join(modifyJson(f)))
            if "textures" in grass_json:
                grass_block_tex = grass_normal_json["textures"]
            else:
                grass_block_tex = grass_block_json["textures"]
        else:
            grass_block_tex = grass_block_json["textures"]
            
        if "particle" not in grass_block_tex:
            grass_block_tex["particle"] = "block/dirt"
        if "bottom" not in grass_block_tex:
            grass_block_tex["bottom"] = "block/dirt"
        if "top" not in grass_block_tex:
            grass_block_tex["top"] = "block/grass_block_top"
        if "side" not in grass_block_tex:
            grass_block_tex["side"] = "block/grass_block_side"
        if "overlay" not in grass_block_tex:
            grass_block_tex["overlay"] = "block/grass_block_side_overlay"
        
        grass_block_json["textures"] = grass_block_tex
        grass_block_json["parent"] = "block/block"

        with open(MAIN_PATH + 'models/block/grass_block.json','w') as dump_f:
            json.dump(grass_block_json,dump_f)

    if(os.path.exists(MAIN_PATH + 'models/block/anvil.json')):
        with open(MAIN_PATH + 'models/block/anvil.json','r') as f:
            anvil_json = json.loads("\n".join(modifyJson(f)))

        if(os.path.exists(MAIN_PATH + 'models/block/anvil_undamaged.json')):
            with open(MAIN_PATH + 'models/block/anvil_undamaged.json','r') as f:
                anvil_tex = json.loads("\n".join(modifyJson(f)))['textures']
        else:
            anvil_tex = {
                "particle": "block/anvil",
                "body": "block/anvil",
                "top": "block/anvil_top"
            }

        anvil_json['textures'] = anvil_tex
        with open(MAIN_PATH + 'models/block/anvil.json','w') as dump_f:
            json.dump(anvil_json,dump_f)

    '''
                               blockstates' content
    ---------------------------------------------------------------------------
    '''
    if(os.path.exists(MAIN_PATH + 'blockstates/')):
        blockstateList = (file for file in os.listdir(MAIN_PATH + 'blockstates/')
                 if file.endswith('.json'))
        for state in blockstateList:
            #change all models' name in blockstate file
            with open(MAIN_PATH + 'blockstates/' + state, "r", encoding="utf-8") as f:
                fileData = alterAllStates(f)

            with open(MAIN_PATH + 'blockstates/' + state, "w", encoding="utf-8") as f:
                f.write(fileData)
            print(state + ' is OK')

    #splite torch bloackstates
    def changeTorchState(_str):
        try:
            with open(MAIN_PATH + 'blockstates/'+ _str+ 'torch.json','r', encoding="utf-8") as f:
                torch_dict = json.loads("\n".join(modifyJson(f)))

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
            print ("Error: fail to splite " + _str + "torch state")

    changeTorchState('')
    changeTorchState('redstone_')
    changeTorchState('unlit_redstone_')

    #splite anvi bloackstates
    try:
        with open(MAIN_PATH + 'blockstates/anvil.json','r') as f:
            anvil_dict = json.loads("\n".join(modifyJson(f)))
        if 'damage=0,facing=south' in anvil_dict['variants']:
            anvil_json = {
                'variants' : {
                    "facing=south": anvil_dict['variants']["damage=0,facing=south"],
                    "facing=west": anvil_dict['variants']["damage=0,facing=west"],
                    "facing=north": anvil_dict['variants']["damage=0,facing=north"],
                    "facing=east": anvil_dict['variants']["damage=0,facing=east"]
                    }
            }

            with open(MAIN_PATH + 'blockstates/anvil.json','w') as dump_f:
                json.dump(anvil_json,dump_f)

        if 'damage=1,facing=south' in anvil_dict['variants']:
            chipped_anvil_json = {
                'variants' : {
                    "facing=south": anvil_dict['variants']["damage=1,facing=south"],
                    "facing=west": anvil_dict['variants']["damage=1,facing=west"],
                    "facing=north": anvil_dict['variants']["damage=1,facing=north"],
                    "facing=east": anvil_dict['variants']["damage=1,facing=east"]
                    }
            }

            with open(MAIN_PATH + 'blockstates/chipped_anvil.json','w') as dump_f:
                json.dump(chipped_anvil_json,dump_f)

        if 'damage=2,facing=south' in anvil_dict['variants']:
            damaged_anvil_json = {
                'variants' : {
                    "facing=south": anvil_dict['variants']["damage=2,facing=south"],
                    "facing=west": anvil_dict['variants']["damage=2,facing=west"],
                    "facing=north": anvil_dict['variants']["damage=2,facing=north"],
                    "facing=east": anvil_dict['variants']["damage=2,facing=east"]
                    }
            }

            with open(MAIN_PATH + 'blockstates/damaged_anvil.json','w') as dump_f:
                json.dump(damaged_anvil_json,dump_f)

    except IOError:
        print ("Error: fail to splite anvil state")

    #change lever bloackstates
    def changeLeverState(variants, lever_dict,  _str):
        if 'facing=east,powered=' + _str in lever_dict['variants']:
            model = lever_dict['variants']["facing=east,powered=" + _str]["model"]
            variants = {
                **variants,
                "face=wall,facing=north,powered=" + _str: { "model": model, "x": 90},
                "face=wall,facing=east,powered=" + _str: { "model": model, "x": 90, "y": 90 },
                "face=wall,facing=south,powered=" + _str: { "model": model, "x": 90, "y": 180 },
                "face=wall,facing=west,powered=" + _str: { "model": model, "x": 90, "y": 270 },
            }

        if 'facing=down_z,powered=' + _str in lever_dict['variants']:
            model = lever_dict['variants']["facing=down_z,powered=" + _str]["model"]
            variants = {
                **variants,
                "face=ceiling,facing=north,powered=" + _str: { "model": model, "x": 180, "y": 180 },
                "face=ceiling,facing=east,powered=" + _str: { "model": model, "x": 180, "y": 270 },
                "face=ceiling,facing=south,powered=" + _str: { "model": model, "x": 180},
                "face=ceiling,facing=west,powered=" + _str: { "model": model, "x": 180, "y": 90 },
            }

        if 'facing=up_z,powered=' + _str in lever_dict['variants']:
            model = lever_dict['variants']["facing=up_z,powered=" + _str]["model"]
            variants = {
                **variants,
                "face=floor,facing=north,powered=" + _str: { "model": model},
                "face=floor,facing=east,powered=" + _str: { "model": model,  "y": 90 },
                "face=floor,facing=south,powered=" + _str: { "model": model, "y": 180},
                "face=floor,facing=west,powered=" + _str: { "model": model, "y": 270 },
            }
        return variants

    try:
        with open(MAIN_PATH + 'blockstates/lever.json','r') as f:
            lever_dict = json.loads("\n".join(modifyJson(f)))

        variants = {}
        variants = changeLeverState(variants, lever_dict, 'false')
        variants = changeLeverState(variants, lever_dict, 'true')

        with open(MAIN_PATH + 'blockstates/lever.json','w') as dump_f:
            json.dump({'variants':variants},dump_f)

    except IOError:
        print ("Error: fail to splite anvil state")
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

    if(os.path.exists(TEX_PATH + 'particle/particles.png')):
        try:
            p_img = Image.open(TEX_PATH + 'particle/particles.png').convert("RGBA")
            p_img = p_img.resize((128 * RES_R, 128 * RES_R), Image.NEAREST)
            p_arr = np.array(p_img)

            p_o_img = Image.open(resource_path('particles.png')).convert("RGBA")
            p_o_img = p_o_img.resize((256 * RES_R, 256 * RES_R), Image.NEAREST)
            p_o_arr = np.array(p_o_img)

            n_p_arr = np.zeros((256 * RES_R, 256 * RES_R, 4), dtype=np.uint8)
            n_p_arr = overlayImg(p_arr, n_p_arr)
            n_p_arr = overlayImg(cutImg(p_o_arr,104,112, 0,8), n_p_arr,0,104)
            n_p_arr = overlayImg(cutImg(p_o_arr,128,152, 0,88), n_p_arr,0,128)
            
            n_p_img = Image.fromarray(n_p_arr)
            #n_p_img.show()
            n_p_img.save(TEX_PATH + 'particle/particles.png','PNG')
            print('particles.png conversion is OK')
        except:
            print('fail to convert particles.png')

    if(os.path.exists(TEX_PATH + 'map/map_icons.png')):
        try:
            m_img =  Image.open(TEX_PATH + 'map/map_icons.png').convert("RGBA")
            m_img = m_img.resize((32 * RES_R, 32 * RES_R), Image.NEAREST)
            m_arr = np.array(m_img)

            m_o_img = Image.open(resource_path('map_icons.png')).convert("RGBA")
            m_o_img = m_o_img.resize((128 * RES_R, 128 * RES_R), Image.NEAREST)
            m_o_arr = np.array(m_o_img)

            n_m_arr = np.zeros((128 * RES_R, 128 * RES_R, 4), dtype=np.uint8)
            n_m_arr = overlayImg(cutImg(m_arr,0,8, 0,32), n_m_arr,0,0)
            n_m_arr = overlayImg(cutImg(m_arr,0,16, 8,32), n_m_arr,32,0)
            n_m_arr = overlayImg(cutImg(m_arr,16,24, 0,16), n_m_arr,64,0)
            n_m_arr = overlayImg(cutImg(m_o_arr,0,8, 80,128), n_m_arr,80,0)
            n_m_arr = overlayImg(cutImg(m_o_arr,8,16, 0,128), n_m_arr,0,8)
            
            n_m_img = Image.fromarray(n_m_arr)
            #n_m_img.show()
            n_m_img.save(TEX_PATH + 'map/map_icons.png', 'PNG')
            print('map_icons.png conversion is OK')
        except:
            print('fail to convert map_icons.png')

    def changeHorseTex(dir, file):
        try:
            path = dir + file
            h_img = Image.open(path).convert("RGBA")
            h_img = h_img.resize((128 * RES_R, 128 * RES_R), Image.NEAREST)
            h_arr = np.array(h_img)

            n_h_arr = np.zeros((64 * RES_R, 64 * RES_R, 4), dtype=np.uint8)

            #head
            n_h_arr = overlayImg(cutImg(h_arr,0,12, 0,24), n_h_arr,0,13)
            n_h_arr = overlayImg(cutImg(h_arr,0,12, 9,24), n_h_arr,10,13)
            n_h_arr = overlayImg(cutImg(h_arr,0,7, 14,17), n_h_arr,16,13)
            n_h_arr = overlayImg(cutImg(h_arr,7,12, 21,24), n_h_arr,23,20)

            #ear
            n_h_arr = overlayImg(cutImg(h_arr,12,20, 0,6), n_h_arr,0,12)
            n_h_arr = overlayImg(cutImg(h_arr,0,4, 0,6), n_h_arr,19,16)

            #morth
            n_h_arr = overlayImg(cutImg(h_arr,19,27, 25,43), n_h_arr,0,25)
            n_h_arr = overlayImg(cutImg(h_arr,32,34, 24,42), n_h_arr,0,33)
            n_h_arr = overlayImg(cutImg(h_arr,27,32, 33,37), n_h_arr,9,25)

            #neck
            n_h_arr = overlayImg(cutImg(h_arr,21,33, 0,7), n_h_arr,0,42)
            n_h_arr = overlayImg(cutImg(h_arr,21,33, 8,12), n_h_arr,7,42)
            n_h_arr = overlayImg(cutImg(h_arr,21,33, 13,20), n_h_arr,11,42)
            n_h_arr = overlayImg(cutImg(h_arr,21,33, 20,24), n_h_arr,18,42)

            n_h_arr = overlayImg(cutImg(h_arr,12,19, 8,16), n_h_arr,7,35)

            #horsehair
            n_h_arr = overlayImg(cutImg(h_arr,4,20, 58,60), n_h_arr,56,38)
            n_h_arr = overlayImg(cutImg(h_arr,4,20, 62,64), n_h_arr,58,38)
            n_h_arr = overlayImg(cutImg(h_arr,4,20, 65,67), n_h_arr,60,38)
            n_h_arr = overlayImg(cutImg(h_arr,4,20, 67,69), n_h_arr,62,38)

            n_h_arr = overlayImg(cutImg(h_arr,2,4, 62,66), n_h_arr,58,36)

            #body
            n_h_arr = overlayImg(cutImg(h_arr,58,68, 0,22), n_h_arr,0,54)
            n_h_arr = overlayImg(cutImg(h_arr,58,68, 13,24), n_h_arr,11,54)

            n_h_arr = overlayImg(cutImg(h_arr,58,68, 24,34), n_h_arr,22,54)

            n_h_arr = overlayImg(cutImg(h_arr,58,68, 34,56), n_h_arr,32,54)
            n_h_arr = overlayImg(cutImg(h_arr,58,68, 47,57), n_h_arr,43,54)

            n_h_arr = overlayImg(cutImg(h_arr,58,68, 58,68), n_h_arr,54,54)
            n_h_arr = overlayImg(cutImg(h_arr,34,56, 24,44), n_h_arr,22,32)
            n_h_arr = overlayImg(cutImg(h_arr,49,58, 24,44), n_h_arr,22,45)

            #chest
            n_h_arr = overlayImg(cutImg(h_arr,34,45, 0,11), n_h_arr,26,21)
            n_h_arr = overlayImg(cutImg(h_arr,47,58, 11,22), n_h_arr,37,21)

            #foot
            n_h_arr = overlayImg(cutImg(h_arr,35,41, 97,113), n_h_arr,48,25)
            n_h_arr = overlayImg(cutImg(h_arr,49,51, 96,104), n_h_arr,48,31)
            n_h_arr = overlayImg(cutImg(h_arr,49,51, 96,104), n_h_arr,56,31)
            n_h_arr = overlayImg(cutImg(h_arr,55,58, 96,112), n_h_arr,48,33)
            n_h_arr = overlayImg(cutImg(h_arr,29,33, 101,105), n_h_arr,52,21)
            n_h_arr = overlayImg(cutImg(h_arr,51,55, 104,108), n_h_arr,56,21)

            #rein
            n_h_arr = overlayImg(cutImg(h_arr,0,4, 74,80), n_h_arr,29,5)
            #n_h_arr = overlayImg(cutImg(h_arr,24,29, 81,83), n_h_arr,1,7)
            #n_h_arr = overlayImg(cutImg(h_arr,24,29, 81,83), n_h_arr,25,2)
            #n_h_arr = overlayImg(cutImg(h_arr,24,29, 86,88), n_h_arr,17,7)
            #n_h_arr = overlayImg(cutImg(h_arr,24,29, 86,88), n_h_arr,19,2)

            #tail?
            n_h_arr = overlayImg(np.rot90(cutImg(h_arr,10,14, 34,41),-1), n_h_arr,42,47)
            n_h_arr = overlayImg(np.rot90(cutImg(h_arr,3,10, 31,37),-2), n_h_arr,46,47)
            n_h_arr = overlayImg(np.rot90(cutImg(h_arr,10,14, 24,31),1), n_h_arr,52,47)

            n_h_arr = overlayImg(np.rot90(cutImg(h_arr,14,18, 48,55),-1), n_h_arr,42,40)
            n_h_arr = overlayImg(np.rot90(cutImg(h_arr,7,14, 45,51),-2), n_h_arr,46,40)
            n_h_arr = overlayImg(np.rot90(cutImg(h_arr,14,18, 38,45),1), n_h_arr,52,40)
            n_h_arr = overlayImg(cutImg(h_arr,14,18, 45,48), n_h_arr,46,36)

            #sella
            n_h_arr = overlayImg(cutImg(h_arr,0,9, 88,98), n_h_arr,35,0)
            n_h_arr = overlayImg(cutImg(h_arr,9,11, 89,98), n_h_arr,26,9)
            n_h_arr = overlayImg(cutImg(h_arr,9,11, 89,98), n_h_arr,45,9)

            n_h_img = Image.fromarray(n_h_arr)
            #n_h_img.show()
            n_h_img.save(path, 'PNG')
            print(file + ' conversion is OK')
        except:
            print('fail to convert ' + file)

    if(os.path.exists(TEX_PATH + 'entity/horse/')):
        horseList = (file for file in os.listdir(TEX_PATH + 'entity/horse/')
                 if file.endswith('.png'))
        for horse in horseList:
            changeHorseTex(TEX_PATH + 'entity/horse/', horse)


        if(os.path.exists(TEX_PATH + 'entity/horse/armor')):
            armorList = (file for file in os.listdir(TEX_PATH + 'entity/horse/armor')
                     if file.endswith('.png'))
            for armor in armorList:
                changeHorseTex(TEX_PATH + 'entity/horse/armor/', armor)

'''
---------------------------------------------------------------------------
                        change pack's info
---------------------------------------------------------------------------
'''
def changeInfo():

    try:
        with open(PACK + '/pack.mcmeta','r') as f:
            pack_info = json.loads("\n".join(modifyJson(f)))

            #print(pack_info)
            pack_info['pack']['pack_format'] = 4
            pack_info['pack']['description'] = pack_info['pack']['description'].replace(" fit for 1.13 by icrdr","")
            pack_info['pack']['description'] += " fit for 1.13 by icrdr"
            #print(pack_info)

        with open(PACK + '/pack.mcmeta','w') as f:
            json.dump(pack_info,f)
    except:
        with open(PACK + '/pack.mcmeta', "r", encoding="utf-8") as f:
            fileData = alter(f,'"pack_format": 3', '"pack_format": 4')

        with open(PACK + '/pack.mcmeta', "w", encoding="utf-8") as f:
            f.write(fileData)
'''
---------------------------------------------------------------------------
                                zip pack
---------------------------------------------------------------------------
'''
def deleteTemp(pack):
    print ("deleting temp...")
    #delete folder
    shutil.rmtree(pack)
    '''try:
        shutil.rmtree(pack)
    except:
        print('fail to delete unziped file. u may delete them by yourself.')'''

def zipPack():
    print ("CONVERTION DONE!")
    print ("zipping pack...")

    azip = zipfile.ZipFile(PACK + '_for_1.13_by_icrdr.zip', 'w')
    for root, dirs, files in os.walk(PACK):
        for name in files:
            azip.write(os.path.join(root, name),os.path.join(root, name)[len(PACK)+1:])
            print(os.path.join(root, name)[len(PACK)+1:])
    azip.close()
    deleteTemp(PACK)

def main(pack):
    global PACK, MAIN_PATH, TEX_PATH, block_path, item_path, entity_path
    PACK = pack
    MAIN_PATH = PACK + '/assets/minecraft/'
    TEX_PATH =  MAIN_PATH+ 'textures/'
    block_path = TEX_PATH+ 'blocks/'
    item_path = TEX_PATH+ 'items/'
    entity_path = TEX_PATH+ 'entity/'
    unzipPack()
    with open(PACK + '/pack.mcmeta', "r", encoding="utf-8") as f:
        is113 = False
        for line in f:
            print (line)
            if '"pack_format": 4' in line:is113 = True
    if(is113):
        deleteTemp(PACK)
        return -1
    res_r = detectRes()
    if(not res_r):
        print("fail to detect the pack's resolution")
        deleteTemp(PACK)
        return 0
    return conversion(res_r)

def conversion(res_r):
    global RES_R
    if(res_r == 0):res_r = 1
    RES_R = int(math.pow(2, res_r))
    changeFileName()
    changeFolderName()
    changeModel()
    resizeTex()
    changeInfo()
    zipPack()
    print ("ALL DONE!")
    return True

if __name__ == '__main__':
    print ("input resource pack dir")
    pack = input()
    main(pack)
