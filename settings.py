from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    qdrant_rest_api: int = Field(alias='QDRANT_REST_API')
    qdrant_grpc_api: int = Field(alias='QDRANT_GRPC_API')


settings = Settings()
