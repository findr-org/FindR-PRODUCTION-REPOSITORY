#==========================#
#Config.py
#==========================#

"""
This file is solely responsible for handling and validating
Application configuration variables 
"""

from pydantic_settings import SettingsConfigDict
from pydantic import BaseModel


class Settings(BaseModel):
    model_config = SettingsConfigDict(
        use_enum_values = True,
    )