from django.db import connection

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        tenant_schema = "tenant1"  # Get the schema based on your logic
        connection.set_schema(tenant_schema)
        response = self.get_response(request)
        connection.set_schema_to_public()  # Reset schema to public
        return response



class TenantRouter:
    def db_for_read(self, model, **hints):
        # Return the schema for read queries
        return connection.schema_name

    def db_for_write(self, model, **hints):
        # Return the schema for write queries
        return connection.schema_name



