import math

G0 = 9.80665

def delta_v(m0, m1, isp=300):
    if m1 <= 0 or m0 < m1:
        raise ValueError("Требуется m0 >= m1 > 0")
    return isp * G0 * math.log(m0 / m1)

def flight_time(distance_km, accel):
    distance_m = distance_km * 1000
    t_seconds = 2 * math.sqrt((distance_m / 2) / accel)
    return t_seconds / 3600

def fuel_needed(m_dry, target_dv, isp=300):
    return m_dry * (math.exp(target_dv / (isp * G0)) - 1)
