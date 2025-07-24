import os
import subprocess

def schedule_task(command, schedule):
    cron_job = f"{schedule} {command}\n"
    with open('mycron', 'w') as f:
        f.write(cron_job)
    subprocess.run(['crontab', 'mycron'])
    print("Scheduled task:", cron_job)

# Example usage
schedule_task('echo Hello', '* * * * *')
