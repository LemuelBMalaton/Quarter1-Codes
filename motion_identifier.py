def convert_velocity(value, unit):
    if unit == "m/s":
        return value
    elif unit == "ft/s":
        v = value / 3.281
        return v
    elif unit == "km/s":
        v = value * 1000
        return v
    else:
        v = value * 1609
        return v
    pass

def convert_acceleration(value, unit):
    if unit == "m/s²":
        return value
    elif unit == "ft/s²":
        v = value / 3.281
        return v
    elif unit == "km/s²":
        v = value * 1000
        return v
    else:
        v = value * 1609
        return v
    pass

def motion_type(v, a):
    if v > 0 and a == 0:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    else:
        return "At rest"
    pass

v_value = float(input("Enter velocity value: "))

v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")


a_value = float(input("Enter acceleration value: "))

a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")


v_si = convert_velocity(v_value, v_unit)      

a_si = convert_acceleration(a_value, a_unit)  


motion = motion_type(v_si, a_si)              


print("\n--- Results ---")

print(f"Velocity = {v_si:.3f} m/s")

print(f"Acceleration = {a_si:.3f} m/s²")

print(f"Motion Type = {motion}")