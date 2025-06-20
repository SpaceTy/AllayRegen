# Initialize scoreboard for timer
scoreboard objectives add allayregen dummy "Allay Regeneration Timer"
scoreboard players set #timer allayregen 0

# Tell players the datapack is loaded
tellraw @a {"text":"✨ Allay Regeneration datapack loaded! Allays will regenerate 1 heart per 30 seconds.","color":"green"} 