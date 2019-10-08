import robloxautomation as roblox
import time

roblox.OpenRoblox()

for x in range(0,5000):
    roblox.Click(roblox.RandomTime(3,10))
    roblox.GoUp(roblox.RandomTime(3,10))
    roblox.Jump(roblox.RandomTime(1,2))
    roblox.Click(roblox.RandomTime(3,10))
    roblox.GoDown(roblox.RandomTime(1,6))
    roblox.Jump(roblox.RandomTime(1,2))
    roblox.Click(roblox.RandomTime(3,10))
    roblox.GoLeft(roblox.RandomTime(1,6))
    roblox.Jump(roblox.RandomTime(1,2))
    roblox.Click(roblox.RandomTime(3,10))
    roblox.GoRight(roblox.RandomTime(1,6))
    time.sleep(roblox.RandomTime(1,2))    
    x += 1