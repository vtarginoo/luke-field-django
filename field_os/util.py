from datetime import datetime
import random

def generate_id_os():
    random_number = random.randint(0, 9999)
    formatted_number = f"{random_number:04d}"
    ano_mes = datetime.now().strftime('%y%m')
    return f"OS-{ano_mes}-{formatted_number}"


