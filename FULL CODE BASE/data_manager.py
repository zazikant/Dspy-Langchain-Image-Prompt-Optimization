import pandas as pd
from typing import List, Dict, Any, Optional
from .utils import generate_timestamp
import logging
import os

logger = logging.getLogger(__name__)

class DataManager:
    """Manages data storage and retrieval for the prompt optimization system."""
    
    def __init__(self, data_path: str = "data/training_data.csv"):
        """Initialize the DataManager with the path to the data file."""
        self.data_path = data_path
        self._ensure_data_file_exists()
    
    def _ensure_data_file_exists(self):
        """Ensure the data file exists, create if not."""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
            self.df = pd.read_csv(self.data_path)
            logger.info(f"Loaded {len(self.df)} existing entries from {self.data_path}")
        except FileNotFoundError:
            # Create a new DataFrame with the required columns
            columns = [
                'timestamp', 'taste', 'user_input', 'dspy_prompt', 
                'final_prompt', 'quality_score'
            ]
            self.df = pd.DataFrame(columns=columns)
            self.save_data()
            logger.info(f"Created new data file at {self.data_path}")
    
    def save_data(self):
        """Save the DataFrame to the CSV file."""
        self.df.to_csv(self.data_path, index=False)
    
    def add_entry(self, taste: str, user_input: str, dspy_prompt: str, 
                  final_prompt: str, quality_score: float):
        """Add a new entry to the DataFrame."""
        new_entry = pd.DataFrame([{
            'timestamp': generate_timestamp(),
            'taste': taste,
            'user_input': user_input,
            'dspy_prompt': dspy_prompt,
            'final_prompt': final_prompt,
            'quality_score': quality_score,
        }])
        
        self.df = pd.concat([self.df, new_entry], ignore_index=True)
        self.save_data()
        logger.info(f"Added new entry for {taste} prompt")
    
    def get_training_examples(self, taste: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get training examples, optionally filtered by taste."""
        if taste:
            filtered_df = self.df[self.df['taste'] == taste]
        else:
            filtered_df = self.df
        
        examples = []
        for _, row in filtered_df.iterrows():
            examples.append({
                'taste': row['taste'],
                'user_input': row['user_input'],
                'optimized_prompt': row['dspy_prompt']
            })
        
        return examples
    
    def get_high_quality_examples(self, min_quality: float = 0.6, 
                                 days: int = 30) -> List[Dict[str, Any]]:
        """Get high-quality examples from recent data. Note: quality score is 0-1."""
        from datetime import datetime, timedelta
        
        # Ensure timestamp is datetime object for comparison
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_df = self.df[
            (self.df['timestamp'] >= cutoff_date) &
            (self.df['quality_score'] >= min_quality)
        ]
        
        examples = []
        for _, row in recent_df.iterrows():
            examples.append({
                'taste': row['taste'],
                'user_input': row['user_input'],
                'optimized_prompt': row['final_prompt']
            })
        
        return examples
    
    def get_analytics(self) -> Dict[str, Any]:
        """Get analytics about the data."""
        if self.df.empty:
            return {"message": "No data available for analytics."}

        analytics = {}
        
        # Most popular taste categories
        analytics['taste_distribution'] = self.df['taste'].value_counts().to_dict()
        
        # Average prompt length by taste
        self.df['prompt_length'] = self.df['final_prompt'].str.split().str.len()
        avg_length_by_taste = self.df.groupby('taste')['prompt_length'].mean()
        analytics['avg_prompt_length_by_taste'] = avg_length_by_taste.to_dict()
        
        # Quality trends over time
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        self.df['date'] = self.df['timestamp'].dt.date
        quality_trends = self.df.groupby('date')['quality_score'].mean()
        # Convert Timestamps to strings for JSON serialization if needed
        analytics['quality_trends'] = {str(k): v for k, v in quality_trends.to_dict().items()}

        
        # Top performing prompts
        top_prompts = self.df.nlargest(5, 'quality_score')
        analytics['top_prompts'] = top_prompts[['taste', 'user_input', 'final_prompt', 'quality_score']].to_dict('records')
        
        # Quality statistics
        analytics['quality_stats'] = {
            'mean': self.df['quality_score'].mean(),
            'median': self.df['quality_score'].median(),
            'std': self.df['quality_score'].std()
        }
        
        return analytics
