# Allay Regeneration Datapack

A Minecraft 1.21.4 datapack that makes allays regenerate 1 heart per 30 seconds.

**Created by SpaceTy**  
**Join my server: [https://apply.spacety.dev](https://apply.spacety.dev)**

## Features

- ✨ Allays automatically regenerate to full health every 30 seconds
- 🚀 **Anti-lag design**: Heals small groups (max 5) every 2 seconds instead of all at once
- 🎯 Only heals allays that are not at full health
- 📦 Simple installation

## Installation

1. Download this datapack folder
2. Place it in your world's `datapacks` folder:
   - Singleplayer: `.minecraft/saves/[world_name]/datapacks/`
   - Server: `[server_folder]/world/datapacks/`
3. In-game, run: `/reload`
4. The datapack will automatically load and show a confirmation message

## How it Works

- **Distributed Healing**: Heals up to 5 allays every 2 seconds instead of all allays at once
- **Lag Prevention**: Spreads computational load evenly to prevent lag spikes
- **Efficient Targeting**: Only processes allays that need healing
- **Timer System**: Uses a 40-tick timer (2 seconds) for consistent healing intervals

## Performance Benefits

- ✅ **No Lag Spikes**: Small groups prevent sudden performance drops
- ✅ **Smooth Gameplay**: Healing is spread across time instead of concentrated
- ✅ **Scalable**: Works well with any number of allays
- ✅ **Efficient**: Only processes damaged allays

## Commands

- `/reload` - Reload the datapack (if you make changes)
- `/function allayregen:load` - Manually trigger the load function

## Technical Details

- **Pack Format**: 26 (Minecraft 1.21.4)
- **Healing Rate**: Up to 5 allays every 2 seconds
- **Total Time**: All allays will be healed within 30 seconds (depending on count)
- **Performance**: Distributed load prevents lag spikes

## Files Structure

```
allayregen/
├── pack.mcmeta
├── data/
│   ├── allayregen/
│   │   └── functions/
│   │       ├── tick.mcfunction
│   │       ├── regenerate_allays.mcfunction
│   │       └── load.mcfunction
│   └── minecraft/
│       └── tags/
│           └── functions/
│               ├── tick.json
│               └── load.json
└── README.md
```

---

**Want to play on a server with this datapack?**  
**Apply to join SpaceTy's server: [https://apply.spacety.dev](https://apply.spacety.dev)** 