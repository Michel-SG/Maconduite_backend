"""
This module provides security for the Flask application.

Specifically, it provides a session mechanism and Role-Based Access Control (or RBAC) with
JSON Web Tokens (or JWT). These tokens are encoded in the function generate_token(), and
are decoded in the decorator @auth_required.
"""