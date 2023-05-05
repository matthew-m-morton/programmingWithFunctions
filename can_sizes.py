import math

def main():
    height = 0
    radius = 0
    
    #Lists for inputs
    names = ["#1 Picnic", "#1 tall", '#2', '#2.5', "#3 Cylander", "#5", '#6z', "8z short", "#10", "#211", "#300", "#303"]
    radii = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27, 11.11]

    #for loop
    for i in range(len(names)):
        can_vol = compute_vol(radii[i], heights[i])
        can_surface_area = compute_surface_area(radii[i], heights[i])
        storage_efficiency = compute_storage_efficiency(can_vol, can_surface_area)

        print(f"{names[i]} {storage_efficiency:.01f}")

def compute_vol(radius, height):
    vol = math.pi * (radius**2) * height
    return vol

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return(surface_area)

def compute_storage_efficiency(vol, surface_area):
    storage_efficiency = vol / surface_area
    return storage_efficiency

main()