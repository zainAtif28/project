import os

# Create the annotations directory if it doesn't exist
if not os.path.exists("annotations"):
    os.makedirs("annotations")

# Open the pairs file for reading
with open("dataset/pairs.txt", "r") as pairs_file:
    # Create the new annotated file for writing
    with open("annotations/pairs_annotated.txt", "w") as annotated_file:
        # Read each line in the pairs file
        for line in pairs_file:
            print(f"Line: {line}")
            # Split the line into its components
            components = line.split()
            print(f"Components: {components}")
            # If the line contains the number of pairs
            if len(components) == 3:
                # Write the number of pairs to the annotated file
                annotated_file.write(components[0] + "\n")
                print(f"Number of Pairs: {components[0]}")
            # If the line contains a pair of face image names
            elif len(components) == 4:
                # Write the label (0 or 1) to the annotated file
                annotated_file.write(components[2] + "\n")
                print(f"Label: {components[2]}")
            # Otherwise, skip the line
            else:
                continue
