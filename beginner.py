import mcpi.minecraft as minecraft
import mcpi.block as block
import math

#To send your code to another game, uncomment the "ip" line below and 
#enter their remote ip address. Then type ip in the parentheses
#at the end of the "mc" line.

#Example:
#ip="127.0.0.1"
#mc=minecraft.Minecraft.create(ip)

mc=minecraft.Minecraft.create()

#The code below makes your world flat
mc.setBlocks(-128,-3,-128,128,64,128,0)


#this gets the x,y, and z coordinate and a second coordiante.
#It then fills in with whaterver block you want
#The coordinates are the three numbers in the top left corner
mc.setBlocks(5,5,5, 10,10,10, 246)


'''
#API Blocks
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
