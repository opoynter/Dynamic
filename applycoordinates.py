import bpy
import csv

# Path to your CSV file
csv_path = '/home/owpo6214/Desktop/DynamicVis/coordinates.csv'
multiplier = 1
offset = 0

# Read the CSV file
coordinates = []
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        # Parse Timestamp and Coordinates
        timestamp = row[0]
        x, y, z = map(float, row[1:])
        x, y, z = multiplier*x, multiplier*y, multiplier*z
        coordinates.append((timestamp, (x, y, z)))

# Select the active object
obj = bpy.context.object

if obj is None:
    raise Exception("No object selected! Please select an object.")

# Animate the object using the parsed data
for frame, (_, coords) in enumerate(coordinates):
    x, y, z = coords
    
    #apply frame offset
    adjusted_frame = frame + offset

    # Set object location
    obj.location = (x, y, z)

    # Insert keyframe at the corresponding frame
    obj.keyframe_insert(data_path="location", frame=adjusted_frame)
