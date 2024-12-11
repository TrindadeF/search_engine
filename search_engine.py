from iqoptionapi.stable_api import IQ_Option
from dotenv import load_dotenv
import os
import time

load_dotenv()

def get_open_assets():
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    iq = IQ_Option(email, password)
    connected, reason = iq.connect()
    
    if not connected:
        print(f"Falha na conexão: {reason}")
        return []

    iq.change_balance("REAL") 
    time.sleep(1)
    
    open_assets = []
    all_assets = iq.get_all_open_time()

    for asset_type, asset_info in all_assets.items():
        for asset, data in asset_info.items():
            if data['open'] and not asset.startswith("OTC"):  
                open_assets.append({
                    "type": asset_type,
                    "asset": asset
                })

    return open_assets

open_assets = get_open_assets()
if open_assets:
    print("Ativos abertos encontrados:")
    for asset in open_assets:
        print(f"Tipo: {asset['type']}, Ativo: {asset['asset']}")
else:
    print("Nenhum ativo aberto encontrado.")
