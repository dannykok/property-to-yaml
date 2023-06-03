import sys, yaml

# Read the input and output filenames from the command line arguments
input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Open the input file and read its contents
with open(input_filename, 'r') as f:
    env_contents = f.read()

# Split the contents into lines and remove any empty lines or comments
env_lines = [line.strip() for line in env_contents.split('\n') if line.strip() and not line.startswith('#')]

# Convert the lines into a dictionary
env_dict = {}
for line in env_lines:
    key_value_pair = line.split('=')
    key = key_value_pair[0].strip()
    value = '='.join(key_value_pair[1:]).strip().strip('"').strip("'")
    env_dict[key] = value

# Convert the dictionary to YAML and write it to the output file
with open(output_filename, 'w') as f:
    f.write('#\n')
    f.write('# This is a generated file\n')
    f.write('#\n\n')
    yaml.dump(env_dict, f, default_flow_style=False)