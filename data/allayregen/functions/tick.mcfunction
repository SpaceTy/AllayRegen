# Allay Regeneration System - Distributed Healing
# Runs every tick to check and heal allays in small groups

# Heal a small group of allays every 2 seconds (40 ticks)
# This spreads the load and prevents lag spikes
execute if score #timer allayregen matches 40.. run function allayregen:regenerate_allays
execute if score #timer allayregen matches 40.. run scoreboard players set #timer allayregen 0

# Increment timer
scoreboard players add #timer allayregen 1 