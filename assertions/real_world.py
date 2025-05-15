"""
Python Assertions - Real-World Examples
======================================

This script demonstrates practical real-world uses of assertions
in different programming scenarios.
"""

# ===============================
# 1. DATA SCIENCE EXAMPLE
# ===============================
print("1. DATA SCIENCE EXAMPLE")
print("----------------------")

import numpy as np

def preprocess_dataset(data):
    """Preprocess a dataset for machine learning."""
    # Verify data shape and type
    assert isinstance(data, np.ndarray), "Data must be a numpy array"
    assert data.ndim == 2, "Data must be 2-dimensional"
    
    # Check for missing values
    assert not np.isnan(data).any(), "Dataset contains missing values"
    
    # Normalize data (assuming values should be between 0 and 1000)
    assert np.all(data >= 0) and np.all(data <= 1000), "Data values out of expected range"
    
    # Perform preprocessing
    normalized_data = data / 1000.0
    
    return normalized_data

# Example usage
try:
    # Create a valid dataset
    valid_data = np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])
    processed = preprocess_dataset(valid_data)
    print("✓ Valid data processed successfully")
    print(f"Original data:\n{valid_data}")
    print(f"Processed data:\n{processed}")
    
    # Uncomment to see assertion errors:
    # Invalid data type
    # preprocess_dataset([1, 2, 3])
    
    # Invalid dimensions
    # preprocess_dataset(np.array([1, 2, 3]))
    
    # Out of range values
    # preprocess_dataset(np.array([[100, 2000, 300]]))
    
    # Missing values
    # data_with_nan = np.array([[100, 200, np.nan], [400, 500, 600]])
    # preprocess_dataset(data_with_nan)
    
except AssertionError as e:
    print(f"Assertion failed: {e}")

print("\n")

# ===============================
# 2. WEB DEVELOPMENT EXAMPLE
# ===============================
print("2. WEB DEVELOPMENT EXAMPLE")
print("-------------------------")

def validate_user_input(user_data):
    """Validate user input from a web form."""
    # Check required fields
    assert "username" in user_data, "Username is required"
    assert "email" in user_data, "Email is required"
    assert "password" in user_data, "Password is required"
    
    # Validate username
    username = user_data["username"]
    assert isinstance(username, str), "Username must be a string"
    assert 3 <= len(username) <= 20, "Username must be between 3 and 20 characters"
    assert username.isalnum(), "Username must contain only letters and numbers"
    
    # Validate email (simple check)
    email = user_data["email"]
    assert isinstance(email, str), "Email must be a string"
    assert "@" in email and "." in email, "Invalid email format"
    
    # Validate password
    password = user_data["password"]
    assert isinstance(password, str), "Password must be a string"
    assert len(password) >= 8, "Password must be at least 8 characters"
    assert any(c.isupper() for c in password), "Password must contain at least one uppercase letter"
    assert any(c.islower() for c in password), "Password must contain at least one lowercase letter"
    assert any(c.isdigit() for c in password), "Password must contain at least one number"
    
    return True

# Example usage
try:
    # Valid user data
    valid_user = {
        "username": "JohnDoe123",
        "email": "john.doe@example.com",
        "password": "SecurePass123"
    }
    
    if validate_user_input(valid_user):
        print("✓ User data is valid")
    
    # Uncomment to see assertion errors:
    # Missing field
    # invalid_user1 = {"username": "JohnDoe123", "email": "john.doe@example.com"}
    # validate_user_input(invalid_user1)
    
    # Invalid username
    # invalid_user2 = {"username": "John Doe!", "email": "john.doe@example.com", "password": "SecurePass123"}
    # validate_user_input(invalid_user2)
    
    # Invalid email
    # invalid_user3 = {"username": "JohnDoe123", "email": "not-an-email", "password": "SecurePass123"}
    # validate_user_input(invalid_user3)
    
    # Weak password
    # invalid_user4 = {"username": "JohnDoe123", "email": "john.doe@example.com", "password": "password"}
    # validate_user_input(invalid_user4)
    
except AssertionError as e:
    print(f"Validation failed: {e}")

print("\n")

# ===============================
# 3. API DEVELOPMENT EXAMPLE
# ===============================
print("3. API DEVELOPMENT EXAMPLE")
print("------------------------")

def process_api_request(request, required_permissions):
    """Process an API request with permission checking."""
    # Verify request format
    assert isinstance(request, dict), "Request must be a dictionary"
    assert "user_id" in request, "Request must include user_id"
    assert "action" in request, "Request must include action"
    
    # Verify user has required permissions
    user_permissions = get_user_permissions(request["user_id"])
    assert set(required_permissions).issubset(set(user_permissions)), \
           f"User lacks required permissions: {set(required_permissions) - set(user_permissions)}"
    
    # Process the request based on the action
    action = request["action"]
    if action == "get_data":
        return {"status": "success", "data": "Requested data"}
    elif action == "update_record":
        assert "record_id" in request, "update_record action requires record_id"
        return {"status": "success", "message": f"Record {request['record_id']} updated"}
    else:
        assert False, f"Unknown action: {action}"

def get_user_permissions(user_id):
    """Simulate fetching user permissions from a database."""
    # In a real application, this would query a database
    permissions_db = {
        "user123": ["read", "write"],
        "admin456": ["read", "write", "delete", "admin"],
        "guest789": ["read"]
    }
    
    assert user_id in permissions_db, f"Unknown user: {user_id}"
    return permissions_db[user_id]

# Example usage
try:
    # Valid request with sufficient permissions
    admin_request = {
        "user_id": "admin456",
        "action": "update_record",
        "record_id": 42
    }
    
    result = process_api_request(admin_request, ["read", "write"])
    print(f"✓ API request processed: {result}")
    
    # Valid request with different action
    read_request = {
        "user_id": "guest789",
        "action": "get_data"
    }
    
    result = process_api_request(read_request, ["read"])
    print(f"✓ API request processed: {result}")
    
    # Uncomment to see assertion errors:
    # Unknown user
    # bad_request1 = {"user_id": "unknown", "action": "get_data"}
    # process_api_request(bad_request1, ["read"])
    
    # Insufficient permissions
    # bad_request2 = {"user_id": "guest789", "action": "update_record", "record_id": 42}
    # process_api_request(bad_request2, ["read", "write"])
    
    # Missing required field for action
    # bad_request3 = {"user_id": "admin456", "action": "update_record"}
    # process_api_request(bad_request3, ["read", "write"])
    
    # Unknown action
    # bad_request4 = {"user_id": "admin456", "action": "delete_everything"}
    # process_api_request(bad_request4, ["admin"])
    
except AssertionError as e:
    print(f"API error: {e}")

print("\n")

# ===============================
# 4. GAME DEVELOPMENT EXAMPLE
# ===============================
print("4. GAME DEVELOPMENT EXAMPLE")
print("--------------------------")

class GameObject:
    def __init__(self, position, size):
        # Validate position and size
        assert isinstance(position, tuple) and len(position) == 2, "Position must be a tuple of (x, y)"
        assert isinstance(size, tuple) and len(size) == 2, "Size must be a tuple of (width, height)"
        assert all(isinstance(n, (int, float)) for n in position), "Position values must be numbers"
        assert all(isinstance(n, (int, float)) and n > 0 for n in size), "Size values must be positive numbers"
        
        self.position = position
        self.size = size
        self.active = True
    
    def move(self, dx, dy):
        """Move the object by the specified delta."""
        assert isinstance(dx, (int, float)) and isinstance(dy, (int, float)), "Movement delta must be numbers"
        
        x, y = self.position
        self.position = (x + dx, y + dy)
    
    def collides_with(self, other):
        """Check if this object collides with another object."""
        assert isinstance(other, GameObject), "Can only check collision with another GameObject"
        assert self.active and other.active, "Cannot check collision with inactive objects"
        
        # Simple collision detection (bounding box)
        x1, y1 = self.position
        w1, h1 = self.size
        x2, y2 = other.position
        w2, h2 = other.size
        
        return (x1 < x2 + w2 and x1 + w1 > x2 and
                y1 < y2 + h2 and y1 + h1 > y2)

# Example usage
try:
    # Create game objects
    player = GameObject((100, 100), (50, 50))
    enemy = GameObject((200, 200), (40, 40))
    
    print(f"Player position: {player.position}, size: {player.size}")
    print(f"Enemy position: {enemy.position}, size: {enemy.size}")
    
    # Move player
    player.move(50, -20)
    print(f"Player moved to: {player.position}")
    
    # Check collision
    if player.collides_with(enemy):
        print("Player collides with enemy!")
    else:
        print("No collision detected")
    
    # Move player to cause collision
    player.move(40, 70)
    print(f"Player moved to: {player.position}")
    
    if player.collides_with(enemy):
        print("Player collides with enemy!")
    else:
        print("No collision detected")
    
    # Uncomment to see assertion errors:
    # Invalid position
    # bad_object1 = GameObject("invalid", (50, 50))
    
    # Invalid size
    # bad_object2 = GameObject((100, 100), (-10, 50))
    
    # Invalid movement
    # player.move("right", 10)
    
    # Invalid collision check
    # player.collides_with("not an object")
    
    # Deactivate object and try collision
    # enemy.active = False
    # player.collides_with(enemy)
    
except AssertionError as e:
    print(f"Game error: {e}")

print("\n")
print("End of Real-World Examples")