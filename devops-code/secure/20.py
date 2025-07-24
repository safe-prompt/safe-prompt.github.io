import logging

logging.basicConfig(filename='deploy.log', level=logging.INFO)


def safe_log_event(event):
    # Avoid logging sensitive data
    if 'password' in event or 'secret' in event:
        event = '[REDACTED] Sensitive data removed.'
    logging.info(event)

# Example usage:
# safe_log_event('Deployment started')
