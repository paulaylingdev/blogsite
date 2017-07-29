from itsdangerous import URLSafeTimedSerializer

def getTimedSerializer(app):
    return URLSafeTimedSerializer(app.config['SECRET_KEY'])
    
