# HUSTOM-1 NIGHTFALCON Fuel Calculator
# Thomas Hustom | Zanzibar
# TBCC: 0.15 kg/s turbofan + 440 kg/s FFSC dash

CH4_DENSITY = 420
CH4_BURN = 0.15

def calc(hours):
    t = hours*3600
    mass = CH4_BURN*t
    vol = mass/CH4_DENSITY
    rng = 850*hours
    tanks = max(0, (vol-2.4-3.5)/2.0)
    return mass, vol, rng, tanks

for h in [12,18,24]:
    m,v,r,tk = calc(h)
    print(f"{h}HR: {m}kg, {v:.1f}m3, {r}km, {tk:.0f} drop tanks")

print("Rocket 12hr = 19,008 TONS impossible")
print("Turbofan 12hr = 6.4 TONS possible")
