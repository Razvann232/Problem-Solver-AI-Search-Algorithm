import pygame

pygame.init()

# Title
titleImage = pygame.image.load("Title.png")

# Animation elements
background = pygame.image.load("Background.png")
missionary_right = pygame.image.load("Missionary_Right.png")
cannibal_right = pygame.image.load("Cannibal_Right.png")
missionary_left = pygame.image.load("Missionary_Left.png")
cannibal_left = pygame.image.load("Cannibal_Left.png")
empty_boat = pygame.image.load("Empty_Boat.png")

arrow_right = pygame.image.load("arrow_right.png")
arrow_left = pygame.image.load("arrow_left.png")
arrow_right = pygame.transform.scale(arrow_right, (75, 75))
arrow_left = pygame.transform.scale(arrow_left, (75, 75))

boat_two_missionaries = pygame.image.load("boat_two_missionaries.png")
boat_two_missionaries = pygame.transform.scale(boat_two_missionaries, (200, 200))

boat_two_cannibals = pygame.image.load("boat_two_cannibals.png")
boat_two_cannibals = pygame.transform.scale(boat_two_cannibals, (200, 200))

boat_both = pygame.image.load("boat_both.png")
boat_both = pygame.transform.scale(boat_both, (200, 200))

boat_one_missionary = pygame.image.load("boat_one_missionary.png")
boat_one_missionary = pygame.transform.scale(boat_one_missionary, (200, 200))

boat_one_cannibal = pygame.image.load("boat_one_cannibal.png")
boat_one_cannibal = pygame.transform.scale(boat_one_cannibal, (200, 200))