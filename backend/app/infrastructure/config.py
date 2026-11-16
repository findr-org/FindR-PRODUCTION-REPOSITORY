# ==========================#
# Config.py
# ==========================#

"""
This file is solely responsible for handling and validating
Application configuration variables
"""

from pydantic import Field
from enum import Enum as PyEnum
from typing import Literal
from functools import lru_cache

from pydantic_settings import SettingsConfigDict, BaseSettings


class Environment(PyEnum, str):
    """Environment Type Enum"""

    DEVELOPMENT = "dev"
    STAGING = "stg"
    PRODUCTION = "prod"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=True
    )

    # ==========================#
    # BASIC APP CONFIGURATION
    # ==========================#
    APP_NAME: str
    ENV: Environment = Environment.DEVELOPMENT
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR"] | None = None

    # ==========================#
    # DATABASE CONFIGURATION
    # ==========================#
    PRIMARY_DATABASE_URL: str
    READ_DATABASE_URL: str

    DB_POOL_SIZE: int = Field(default=5, ge=1, le=50)
    DB_MAX_OVERFLOW: int = Field(default=5, ge=0, le=100)
    DB_POOL_TIMEOUT_SECONDS: int = Field(default=10, ge=1, le=120)
    DB_POOL_RECYCLE_SECONDS: int = Field(default=1800, ge=60)



    #==========================#
    #REDIS CONFIGURATION
    #==========================#
    REDIS_URL : str | None = None
    CACHE_ENABLED : bool = True




    #==========================#
    #SECURITY TOKEN CONFIGUATION
    #==========================#
    SECRET_KEY : str = Field(...,min_length = 32)
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 5
    DEFAULT_SESSION_DAYS : int = Field(default = 7 , gt = 0)
    REMEMBER_ME_SESSION_DAYS : int = Field(default = 30 , gt = 0)




    #==========================#
    #CORS CONFIGURATION
    #==========================#

    ALLOWED_ORIGINS: list[str] = Field(default_factory=list)    



@lru_cache
def get_settings():
    return Settings
