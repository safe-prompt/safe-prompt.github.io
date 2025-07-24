def reset_config(config_file, default_content):
    with open(config_file, 'w') as f:
        f.write(default_content)
    print(f"Reset {config_file}")

# Example usage
reset_config('server.conf', 'default settings')
