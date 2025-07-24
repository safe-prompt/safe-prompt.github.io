import subprocess

def set_firewall_rule(rule):
    # Only allow sanitized input
    if not rule.isalnum():
        raise ValueError('Invalid rule')
    subprocess.run(['ufw', 'allow', rule], check=True)

# Example usage:
# set_firewall_rule('22')
