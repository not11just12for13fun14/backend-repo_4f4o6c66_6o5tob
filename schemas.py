"""
Database Schemas for Real Estate App

Each Pydantic model represents a collection in MongoDB.
Collection name is the lowercase of the class name.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class Property(BaseModel):
    """
    Real estate properties for sale or rent
    Collection: "property"
    """
    title: str = Field(..., description="Listing title")
    description: Optional[str] = Field(None, description="Short description")
    price: float = Field(..., ge=0, description="Price in USD")
    address: str = Field(..., description="Street address")
    city: str = Field(..., description="City")
    state: str = Field(..., description="State/Region")
    beds: int = Field(..., ge=0, description="Number of bedrooms")
    baths: float = Field(..., ge=0, description="Number of bathrooms")
    area_sqft: int = Field(..., ge=0, description="Area in square feet")
    image_url: Optional[str] = Field(None, description="Cover image URL")
    gallery: Optional[List[str]] = Field(default=None, description="Additional image URLs")
    listed_type: str = Field("sale", description="sale | rent")
    featured: bool = Field(False, description="Whether featured on homepage")

class Inquiry(BaseModel):
    """
    Buyer/renter inquiries for a specific property
    Collection: "inquiry"
    """
    property_id: Optional[str] = Field(None, description="Related property document _id as string (optional)")
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    message: str = Field(..., description="Message from the lead")

# Example additional models (kept for reference if needed)
class User(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True

class Product(BaseModel):
    title: str
    price: float
    in_stock: bool = True
