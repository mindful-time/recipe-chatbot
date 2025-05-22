import yaml

def load_yaml_file(file_path):
    """Loads a YAML file and returns its content.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The content of the YAML file.
    """
    with open(file_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None

if __name__ == '__main__':
    # Example usage (optional, for testing)
    # Create a dummy test.yml file for this example to work
    # with open('test.yml', 'w') as f:
    #     f.write('name: Test\ndescription: A test YAML file.')
    
    data = load_yaml_file('test.yml')
    if data:
        print("YAML file loaded successfully:")
        print(data)
    else:
        print("Failed to load YAML file.")
