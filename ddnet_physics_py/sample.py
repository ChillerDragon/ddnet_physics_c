#!/usr/bin/env python3

import ddnet_physics

physics = ddnet_physics.DDNetPhysics("/home/chiller/.teeworlds/maps/tinycave.map")
physics.add_character()
physics.tick()

for character in physics.characters():
    print(f"character with id={character.m_Id}")

