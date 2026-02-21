from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from app.models.schemas import ClientContext

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# This acts as our mock database. In production, this would be a lookup 
# to PostgreSQL, MongoDB, or Redis.
CLIENT_DB = {
    "finance-corp-key-123": ClientContext(
        domain="Financial Services & Online Banking",
        products=["Online Accounts", "Wire Transfers"],
        policies=["Never ask a customer to download remote desktop software."],
        risk_triggers=["AnyDesk", "Crypto", "Gift cards"]
    ),
    "telecom-inc-key-456": ClientContext(
        domain="Telecommunications",
        products=["Mobile Plans", "Internet Packages"],
        policies=["Always verify the account PIN before upgrading."],
        risk_triggers=["Sim swap", "Free upgrade scam"]
    )
}

async def get_client_context(api_key: str = Security(api_key_header)) -> ClientContext:
    """Validates the API key and returns the associated Client Context."""
    if not api_key or api_key not in CLIENT_DB:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
    
    # Return the specific business rules for this client
    return CLIENT_DB[api_key]