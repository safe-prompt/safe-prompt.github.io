def save_config(settings, filename):
    with open(filename, 'w') as f:
        for key, value in settings.items():
            f.write(f"{key}={value}\n")
    print(f"Configuration saved to {filename}")

# Example usage
save_config({'host': 'localhost', 'port': 8080}, 'config.txt')
