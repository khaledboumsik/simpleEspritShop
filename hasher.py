import bcrypt

def hash_password(password):
    # Hash a password using bcrypt
    salt = bcrypt.gensalt()  # Generate a salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt) 
    return hashed_password.decode('utf-8')

def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))
print(verify_password(hash_password("khaled"),"khaled"))