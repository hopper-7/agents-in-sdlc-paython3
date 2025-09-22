"""
Category model for the Tailspin Toys Crowd Funding platform.
Represents game categories used to classify games for easier discovery.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
    """Model representing a game category in the crowdfunding platform."""
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one category has many games
    games = relationship("Game", back_populates="category")
    
    @validates('name')
    def validate_name(self, key, name):
        """
        Validate category name meets minimum length requirements.
        
        Args:
            key (str): The column name being validated
            name (str): The category name to validate
            
        Returns:
            str: The validated name
            
        Raises:
            ValueError: If name is too short or invalid
        """
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key, description):
        """
        Validate category description meets minimum length requirements.
        
        Args:
            key (str): The column name being validated
            description (str): The description to validate
            
        Returns:
            str: The validated description
            
        Raises:
            ValueError: If description is too short or invalid
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)
    
    def __repr__(self):
        """
        Return string representation of the category.
        
        Returns:
            str: Human-readable representation of the category
        """
        return f'<Category {self.name}>'
        
    def to_dict(self):
        """
        Convert category instance to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary containing category data including game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }