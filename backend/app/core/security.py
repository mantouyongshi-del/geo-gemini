import hmac
import hashlib
import base64
import time
from typing import Optional
from app.core.config import settings

def generate_share_token(company_id: int, expire_days: int = 365) -> str:
    """
    生成安全防篡改且带有时效性的公开报表分享码 (Token)
    格式: base64(company_id:expire_timestamp:hmac_signature)
    """
    expire_at = int(time.time()) + (expire_days * 86400)
    payload = f"{company_id}:{expire_at}"
    signature = hmac.new(
        settings.SECRET_KEY.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()[:16]
    
    token_str = f"{payload}:{signature}"
    return base64.urlsafe_b64encode(token_str.encode()).decode().rstrip("=")

def verify_share_token(token: str) -> Optional[int]:
    """
    校验分享码有效性，防止越权（IDOR）与过期访问
    """
    try:
        # 补齐 base64 padding
        padding = 4 - (len(token) % 4)
        if padding != 4:
            token += "=" * padding
            
        decoded = base64.urlsafe_b64decode(token.encode()).decode()
        parts = decoded.split(":")
        if len(parts) != 3:
            return None
            
        company_id_str, expire_at_str, signature = parts
        company_id = int(company_id_str)
        expire_at = int(expire_at_str)
        
        # 检查是否过期
        if time.time() > expire_at:
            return None
            
        payload = f"{company_id}:{expire_at}"
        expected_sig = hmac.new(
            settings.SECRET_KEY.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()[:16]
        
        if hmac.compare_digest(signature, expected_sig):
            return company_id
        return None
    except Exception:
        return None
