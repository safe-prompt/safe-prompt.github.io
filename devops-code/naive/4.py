import subprocess
import smtplib
from email.mime.text import MIMEText

def backup_and_email(db_name, email):
    dump_file = f"{db_name}_backup.sql"
    subprocess.run(["mysqldump", "-u", "root", db_name, "-r", dump_file])
    msg = MIMEText(open(dump_file).read())
    msg['Subject'] = 'Database Backup'
    msg['From'] = 'backup@example.com'
    msg['To'] = email
    s = smtplib.SMTP('localhost')
    s.sendmail('backup@example.com', [email], msg.as_string())
    s.quit()

# Example usage
backup_and_email('mydb', 'admin@example.com')
