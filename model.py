# issuer={
#     "name": "",
#     "description": "",
#     "issuer_id": "",
#     "issuer_type": "",    
# }

# certificate={
#     "name": "",
#     "description": "",
#     "issuer_id": "",
#     "issuer_type": "",
#     "certificate_type": "",
#     "certificate_key": "",
#     "certificate_value": "",
# }

# Define mongodb schema for issuer
issuerSchema={
    "type": "schemaObject",
    "properties": {
        "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        "description": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        "issuer_id": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        "issuer_type": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
    }
}
