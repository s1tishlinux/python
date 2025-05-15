#!/usr/bin/env python3
"""
Script to create a new Python topic with all required files.
This script copies the template files and replaces placeholders.
"""

import os
import sys
import shutil

def create_new_topic(topic_name):
    """Create a new topic folder with all required files."""
    # Convert topic name to proper format
    topic_name = topic_name.strip().lower().replace(' ', '_')
    
    # Define paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, 'template')
    new_topic_dir = os.path.join(base_dir, topic_name)
    
    # Check if topic already exists
    if os.path.exists(new_topic_dir):
        print(f"Error: Topic '{topic_name}' already exists.")
        return False
    
    # Create new topic directory
    os.makedirs(new_topic_dir)
    
    # Copy and modify template files
    for filename in os.listdir(template_dir):
        src_path = os.path.join(template_dir, filename)
        dst_path = os.path.join(new_topic_dir, filename)
        
        # Skip directories and non-template files
        if os.path.isdir(src_path) or not os.path.isfile(src_path):
            continue
        
        # Read template content
        with open(src_path, 'r') as file:
            content = file.read()
        
        # Replace placeholders with actual topic name
        topic_title = topic_name.replace('_', ' ').title()
        content = content.replace('[Topic]', topic_title)
        
        # Write to new file
        with open(dst_path, 'w') as file:
            file.write(content)
    
    print(f"Successfully created new topic: {topic_name}")
    print(f"Topic directory: {new_topic_dir}")
    print("Files created:")
    for filename in os.listdir(new_topic_dir):
        print(f"  - {filename}")
    
    return True

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: python add_new_topic.py <topic_name>")
        print("Example: python add_new_topic.py decorators")
        return
    
    topic_name = sys.argv[1]
    create_new_topic(topic_name)

if __name__ == "__main__":
    main()