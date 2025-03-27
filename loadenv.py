from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.getcwd(), ".env")
print(f"Intentando cargar: {dotenv_path}")

if load_dotenv(dotenv_path):
    print("✅ .env cargado correctamente")
else:
    print("❌ No se pudo cargar el archivo .env")

print(f"DB_USER: {os.getenv('DB_USER')}")
