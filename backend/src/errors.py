from flask import jsonify

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

