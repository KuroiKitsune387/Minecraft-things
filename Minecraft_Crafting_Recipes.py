#Minecraft:crafting recipes

wood_types_to_planks_amount = {
    "oak_log": 4,
    "birch_log": 4,
    "spruce_log": 4,
    "jungle_log": 4,
    "acacia_log": 4,
    "dark_oak_log": 4,
    "mangrove_log": 4,
    "crimson_stem": 4,
    "warped_stem": 4,
    "cherry_log": 4,
    "bamboo_block": 2,
    "pale_oak_log": 4
}

item_aliases = {
    "oak": "oak",
    "oak_log": "oak",
    "oak_wood": "oak",
    "stripped_oak": "oak",
    "stripped_oak_log": "oak",
    "stripped_oak_wood": "oak",
    
    "birch": "birch",
    "birch_log": "birch",
    "birch_wood": "birch",
    "stripped_birch": "birch",
    "stripped_birch_log": "birch",
    "stripped_birch_wood": "birch",
    
    "spruce": "spruce",
    "spruce_log": "spruce",
    "spruce_wood": "spruce",
    "stripped_spruce": "spruce",
    "stripped_spruce_log": "spruce",
    "stripped_spruce_wood": "spruce",
    
    "jungle": "jungle",
    "jungle_log": "jungle",
    "jungle_wood": "jungle",
    "stripped_jungle": "jungle",
    "stripped_jungle_log": "jungle",
    "stripped_jungle_wood": "jungle",
    
    "acacia": "acacia",
    "acacia_log": "acacia",
    "acacia_wood": "acacia",
    "stripped_acacia": "acacia",
    "stripped_acacia_log": "acacia",
    "stripped_acacia_wood": "acacia",
    
    "dark": "dark_oak",
    "dark_oak": "dark_oak",
    "dark_oak_log": "dark_oak",
    "dark_oak_wood": "dark_oak",
    "stripped_dark": "dark_oak",
    "stripped_dark_oak": "dark_oak",
    "stripped_dark_oak_log": "dark_oak",
   "stripped_dark_wood": "dark_oak",
    "stripped_dark_oak_wood": "dark_oak",
    
    "mangrove": "mangrove",
    "mangrove_log": "mangrove",
    "mangrove_wood": "mangrove",
    "stripped_mangrove": "mangrove",
    "stripped_mangrove_log": "mangrove",
    "stripped_mangrove_wood": "mangrove",
    
    "crimson": "crimson",
    "crimson_stem": "crimson",
    "crimson_hyphae": "crimson",
    "stripped_crimson": "crimson",
    "stripped_crimson_stem": "crimson",
    "stripped_crimson_hyphae": "crimson",
    
    "warped": "warped",
    "warped_stem": "warped",
    "warped_hyphae": "warped",
    "stripped_warped": "warped",
    "stripped_warped_stem": "warped",
    "stripped_warped_hyphae": "warped",
    
    "cherry": "cherry",
    "cherry_log": "cherry",
    "cherry_wood": "cherry",
    "stripped_cherry": "cherry",
    "stripped_cherry_log": "cherry",
    "stripped_cherry_wood": "cherry",
    
    "bamboo": "bamboo_block",
    "bamboo_block": "bamboo_block",
    "stripped_bamboo": "bamboo_block",
    "stripped_bamboo_block": "bamboo_block",
    
    "pale": "pale_oak",
    "pale_oak": "pale_oak",
    "pale_oak_log": "pale_oak",
    "pale_oak_wood": "pale_oak",
   "stripped_pale": "pale_oak",
    "stripped_pale_oak_log": "pale_oak",
    "stripped_pale_oak_wood": "pale_oak"
}

log_aliases = {
    "oak": "oak_log",
    "birch": "birch_log",
    "spruce": "spruce_log",
    "jungle": "jungle_log",
    "acacia": "acacia_log",
    "dark_oak": "dark_oak_log",
    "dark": "dark_oak_log",
    "mangrove": "mangrove_log",
    "crimson": "crimson_stem",
    "warped": "warped_stem",
    "cherry": "cherry_log",
    "bamboo_block": "bamboo_block",
    "pale_oak": "pale_oak_log",
}

exotic_suffixes = ["wood", "hyphae"]

wood = input("Enter the type of wood your using: ").strip().lower()
if wood.endswith(tuple(exotic_suffixes)) or wood.startswith("bamboo"):
    print("This is any exotic wood type.")

# if wood in item_aliases:
#     wood_type = item_aliases[wood]
#     if wood_type in log_aliases:
#         log_type = log_aliases[wood_type]
#         planks_amount = wood_types_to_planks_amount.get(log_type, 0)
#         print(f"You can craft {planks_amount} {wood_type} planks from one {log_type}.")
    