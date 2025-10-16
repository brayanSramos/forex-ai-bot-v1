from src.data.download_ohlc import download_data
from src.api.signals_api import generate_signals
from src.utils.db_connection import connect_db
from src.api.signals_api import start_api
import MetaTrader5 as mt5

def main():
    # Conectar a la base de datos
    conn = connect_db()
    
    # Descargar datos OHLC
    data = download_data()
    
    # Generar señales
    signals = generate_signals(data)
    
    # Mostrar señales
    print(signals)
    
if __name__ == "__main__":
    main()
    print("🚀 Iniciando bot Forex...")
    download_data()
    start_api()