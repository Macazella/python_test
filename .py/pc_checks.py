import psutil

# Definir los límites
CPU_LIMIT = 80  # Porcentaje de uso de CPU
RAM_LIMIT = 80  # Porcentaje de uso de RAM
DISK_LIMIT = 80  # Porcentaje de uso del disco

# Obtener el estado de la CPU
cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > CPU_LIMIT:
    print(f"CPU Usage: {cpu_usage}% - Requiere revisión")
else:
    print(f"CPU Usage: {cpu_usage}% - OK")

# Obtener el estado de la RAM
ram_usage = psutil.virtual_memory().percent
if ram_usage > RAM_LIMIT:
    print(f"RAM Usage: {ram_usage}% - Requiere revisión")
else:
    print(f"RAM Usage: {ram_usage}% - OK")

# Obtener el estado del disco
disk_usage = psutil.disk_usage('/').percent
if disk_usage > DISK_LIMIT:
    print(f"Disk Usage: {disk_usage}% - Requiere revisión")
else:
    print(f"Disk Usage: {disk_usage}% - OK")
