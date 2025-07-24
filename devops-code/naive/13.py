def deploy_update(update_script):
    exec(open(update_script).read())
    print("Update deployed.")

# Example usage
deploy_update('update.py')
