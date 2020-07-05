import pygame

map_data = {}

map_data["grid"] = [
    ["plain", "plain", "plain", "plain", "mountain", "mountain", "mountain", "water", "water", "water"],
    ["plain", "fort" , "plain", "plain", "mountain", "mountain", "mountain", "sand" , "sand" , "plain"],
    ["plain", "plain", "plain", "plain", "mountain", "mountain", "mountain", "sand" , "sand" , "plain"],
    ["plain", "plain", "plain", "plain", "forest"  , "forest"  , "forest"  , "sand" , "sand" , "plain"],
    ["plain", "fort" , "plain", "plain", "forest"  , "forest"  , "forest"  , "sand" , "sand" , "plain"],
    ["plain", "plain", "plain", "plain", "forest"  , "forest"  , "forest"  , "water", "water", "water"]
]
map_data["background"] = pygame.image.load("Graphics/battlefield_sample.png")
map_data["init_cursor"] = [5, 9]