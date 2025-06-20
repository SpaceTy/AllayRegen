# Allay Regeneration Datapack

A Minecraft 1.21.4 datapack that makes allays regenerate 1 heart per 2 seconds.

**Created by SpaceTy**  
**Join my server: [https://apply.spacety.dev](https://apply.spacety.dev)**  
**📦 [Download Latest Release](https://github.com/SpaceTy/AllayRegen/releases/tag/MAIN)**

## Features

- ✨ Allays automatically regenerate to full health every 30 seconds
- 🚀 **Anti-lag design**: Heals small groups (max 5) every 2 seconds instead of all at once
- 🎯 Only heals allays that are not at full health

## Installation

1. **Download the zip file** from [GitHub Releases](https://github.com/SpaceTy/AllayRegen/releases/tag/MAIN)
2. Extract the zip file to your world's `datapacks` folder:
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
**Apply to join my server "TYSMP": [https://apply.spacety.dev](https://apply.spacety.dev)** 