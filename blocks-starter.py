# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
import mcpi.minecraft as minecraft
import mcpi.block as block
import math
mc=minecraft.Minecraft.create()

mc.player.setPos(0,0,0)
mc.setBlocks(-128,-3,-128,128,64,128,0)
mc.player.setPos(0,100  ,0)

mc.setBlocks(5,-3,5, 5,1,5, 5)
mc.setBlocks(10,-3,5, 10,1,5, 5)
mc.setBlocks(9,-3,5, 6,1,5, 4)

mc.setBlocks(4,-3,4, 4,1,4, 5)
mc.setBlocks(4,-3,3, 4,1,-1, 4)
mc.setBlocks(4,-3,-1, 4,1,-1, 5)

mc.setBlocks(5,-3,-2, 5,1,-2, 5)
mc.setBlocks(6,-3,-2, 9,1,-2, 4)
mc.setBlocks(10,-3,-2, 10,1,-2, 5)

mc.setBlocks(11,-3,-1, 11,1,4, 5)
mc.setBlocks(11,-3,0, 11,1,3, 4)

mc.setBlocks(10,2,-1,5,9,4, 17)

mc.setBlocks(9,2,-1, 6,9,-1, 45)
mc.setBlocks(5,2,0, 5,9,3, 45)
mc.setBlocks(9,2,4, 6,9,4, 45)
mc.setBlocks(10,2,0, 10,9,3, 45)

mc.setBlocks(9,10,0, 9,17,3, 98)
mc.setBlocks(9,10,3, 6,17,3, 98)
mc.setBlocks(6,10,0, 6,17,3, 98)
mc.setBlocks(9,9,0, 6,17,0, 98)

mc.setBlocks(9,18,1, 11,18,2, 42)

mc.setBlocks(12,18,1, 12,17,2, 5)

mc.setBlocks(12,25,1, 12,19,1, 17)
mc.setBlocks(12,17,-6, 12,17,0, 17)
mc.setBlocks(12,18,3, 12,18,10, 17)
mc.setBlocks(12,16,2, 12,10,2, 17)
#windmill fans
mc.setBlocks(12,19,2, 12,19,7, 35)
mc.setBlocks(12,20,2, 12,20,5, 35)
mc.setBlocks(12,21,2, 12,21,4, 35)
mc.setBlocks(12,22,2, 12,22,3, 35)
mc.setBlocks(12,22,2, 12,24,2, 35)

mc.setBlocks(12,18,0, 12,18,-5, 35)
mc.setBlocks(12,19,0, 12,19,-3, 35)
mc.setBlocks(12,20,0, 12,20,-2, 35)
mc.setBlocks(12,21,0, 12,21,-1, 35)
mc.setBlocks(12,22,0, 12,23,0, 35)

mc.setBlocks(12,17,3, 12,17,8, 35)
mc.setBlocks(12,16,3, 12,16,6, 35)
mc.setBlocks(12,15,3, 12,15,5, 35)
mc.setBlocks(12,14,3, 12,14,4, 35)
mc.setBlocks(12,13,3, 12,12,3, 35)

mc.setBlocks(12,16,1, 12,16,-4, 35)
mc.setBlocks(12,15,1, 12,15,-2, 35)
mc.setBlocks(12,14,1, 12,14,-1, 35)
mc.setBlocks(12,13,1, 12,13,0, 35)
mc.setBlocks(12,12,1, 12,11,1, 35)
#roof
mc.setBlocks(9,18,3, 6,18,3, 53,3)
mc.setBlocks(9,18,0, 6,18,0, 53,2)
mc.setBlocks(6,18,2, 6,18,1, 53,0)  
mc.setBlocks(9,19,2, 9,19,1, 53,1)

mc.setBlocks(8,19,2, 7,19,1, 5)





#45 brick
#98 stone brick
#42 is iron block
#35 is for wool
#wood for windmill is 7 each

mc.setBlock(1,0,0, 1,0,0, 103)# is x
mc.setBlock(0,0,1, 0,0,1, 246)#this is z


'''
#API Bloscks
#====================
#   AIR                   0
#   STONE                 1
#   GRASS                 2
#   DIRT                  3
#   COBBLESTONE           4
#   WOOD_PLANKS           5
#   SAPLING               6
#   BEDROCK               7
#   WATER_FLOWING         8
#   WATER                 8
#   WATER_STATIONARY      9
#   LAVA_FLOWING         10
#   LAVA                 10
#   LAVA_STATIONARY      11
#   SAND                 12
#   GRAVEL               13
#   GOLD_ORE             14
#   IRON_ORE             15
#   COAL_ORE             16
#   WOOD                 17
#   LEAVES               18
#   GLASS                20
#   LAPIS_LAZULI_ORE     21
#   LAPIS_LAZULI_BLOCK   22
#   SANDSTONE            24
#   BED                  26
#   COBWEB               30
#   GRASS_TALL           31
#   WOOL                 35
#   FLOWER_YELLOW        37
#   FLOWER_CYAN          38
#   MUSHROOM_BROWN       39
#   MUSHROOM_RED         40
#   GOLD_BLOCK           41
#   IRON_BLOCK           42
#   STONE_SLAB_DOUBLE    43
#   STONE_SLAB           44
#   BRICK_BLOCK          45
#   TNT                  46
#   BOOKSHELF            47
#   MOSS_STONE           48
#   OBSIDIAN             49
#   TORCH                50
#   FIRE                 51
#   STAIRS_WOOD          53
#   CHEST                54
#   DIAMOND_ORE          56
#   DIAMOND_BLOCK        57
#   CRAFTING_TABLE       58
#   FARMLAND             60
#   FURNACE_INACTIVE     61
#   FURNACE_ACTIVE       62
#   DOOR_WOOD            64
#   LADDER               65
#   STAIRS_COBBLESTONE   67
#   DOOR_IRON            71
#   REDSTONE_ORE         73
#   SNOW                 78
#   ICE                  79
#   SNOW_BLOCK           80
#   CACTUS               81
#   CLAY                 82
#   SUGAR_CANE           83
#   FENCE                85
#   GLOWSTONE_BLOCK      89
#   BEDROCK_INVISIBLE    95
#   STONE_BRICK          98
#   GLASS_PANE          102
#   MELON               103
#   FENCE_GATE          107
#   GLOWING_OBSIDIAN    246
#   NETHER_REACTOR_CORE 247
'''



