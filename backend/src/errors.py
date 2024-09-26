from flask import jsonify
from .auth.auth import AuthError


def errors(app):

    # Error Handling

    @app.errorhandler(400)
    def badrequest(error):
        return (
            jsonify({
                "success": False,
                "error": 400,
                "message": "Bad request"
            }), 400)

    @app.errorhandler(401)
    def authentication_fail(error):
        return (
            jsonify({
                "success": False,
                "error": 401,
                "message": "authentication failed"
            }), 401)

    @app.errorhandler(403)
    def forbidden(error):
        return (
            jsonify({
                "success": False,
                "error": 403,
                "message": "forbidden"
            }), 403)

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({
                "success": False,
                "error": 404,
                "message": "Not found"
            }), 404)

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({
                "success": False,
                "error": 422,
                "message": "unprocessable"
            }), 422)

    @app.errorhandler(500)
    def server_error(error):
        return (
            jsonify({
                "success": False,
                "error": 500,
                "message": "Server error"
            }), 500)

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify({
            "success": False,
            "error": ex.status_code,
            "description": ex.error['description'],
            "code": ex.error['code']
        })
        response.status_code = ex.status_code
        return response
