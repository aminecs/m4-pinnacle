from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings): 
    SQLALCHEMY_URI: str
    GOOGLE_APPLICATION_CREDENTIALS: str
    EMERGENCY_NUMBER: str
    class Config: 
        env_file = '.env'
    
settings = Settings()