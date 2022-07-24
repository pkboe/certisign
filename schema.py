ISSUER_SCHEMA={
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

CERTIFICATE_SCHEMA={
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
        "certificate_type": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        "certificate_id": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        "certificate_data": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        "certificate_signature": {  
            "type": "string",
            "minLength": 1,
            "maxLength": 3000,
            "required": True
        }
    }
}

CANDIDATE_SCHEMA={
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
        "candidate_id": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        "candidate_type": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        "candidate_data": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        "candidate_signature": {
            "type": "string",
            "minLength": 1,
            "maxLength": 3000,
            "required": True
        },
        "candidate_status": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "required": True
        },
        'certificates': {
            "type": "array",
            "items": {
                "type": "string",
                "minLength": 1,
                "maxLength": 100,
                "required": True
            }
        }
    }
}