import gc
import psutil

def liberar_ram():
    # Ejecutar el recolector de basura para liberar memoria no utilizada
    gc.collect()
    
    # Obtener información sobre el uso de memoria
    memoria = psutil.virtual_memory()
    print(f"Uso de RAM antes de liberar: {memoria.percent}%")
    
    # Realizar algunas operaciones que podrían liberar memoria
    # Por ejemplo, eliminar objetos grandes que ya no se necesitan
    global data
    data = None
    
    # Forzar la recolección de basura nuevamente
    gc.collect()
    
    # Verificar el uso de memoria después de la limpieza
    memoria = psutil.virtual_memory()
    print(f"Uso de RAM después de liberar: {memoria.percent}%")

# Ejemplo de uso de la función
data = [x for x in range(10**7)]  # Crear un gran objeto para ocupar memoria
print(f"Uso de RAM inicial: {psutil.virtual_memory().percent}%")
liberar_ram()
