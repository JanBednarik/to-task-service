import falcon


class MembersResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        results = {"members": 1234}
        resp.media = results


def create_api():
    """Creates and returns Facon API instance"""
    api = falcon.API()
    api.add_route("/members", MembersResource())
    return api


api = create_api()
