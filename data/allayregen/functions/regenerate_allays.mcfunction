# Regenerate a small group of allays (max 5 at a time)
# This prevents lag spikes by spreading the healing load
# Only heal allays that are not at full health

execute as @e[type=minecraft:allay,limit=5] unless entity @s[nbt={Health:20.0f}] run data modify entity @s Health set value 20.0f 