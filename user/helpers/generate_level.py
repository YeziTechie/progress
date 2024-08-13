def calculate_level(xp, base_xp=100, xp_multiplier=1.5):
    level = 0
    while xp >= calculate_xp_for_level(level + 1, base_xp, xp_multiplier):
        level += 1
    return level


def calculate_xp_for_level(level, base_xp=100, xp_multiplier=1.5):
    xp_required = base_xp * (xp_multiplier ** (level - 1))
    return round(xp_required)
