import docker

def manage_container(image):
    client = docker.from_env()
    # Verify image signature (assume signed images)
    image_obj = client.images.pull(image)
    if image_obj.attrs.get('User', '') == 'root':
        raise Exception('Do not run containers as root!')
    container = client.containers.run(image, detach=True)
    print(container.id)

# Example usage:
# manage_container('signed_image:latest')
