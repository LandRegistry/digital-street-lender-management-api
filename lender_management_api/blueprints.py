# Import every blueprint file
from lender_management_api.views import general, restriction_v1, user_v1


def register_blueprints(app):
    """Adds all blueprint objects into the app."""
    app.register_blueprint(general.general)
    app.register_blueprint(restriction_v1.restriction_v1, url_prefix="/v1")
    app.register_blueprint(user_v1.user_v1, url_prefix="/v1")

    # All done!
    app.logger.info("Blueprints registered")
