import falcon
import requests
import re


MEMBERS_LIST_URL = "https://forum.pirati.cz/memberlist.php"


def get_members_list_page():
    response = requests.get(MEMBERS_LIST_URL)
    return response.text


def parse_members_count(page):
    m = re.search(r"[\d]+(?= uživatelů)", page)
    return int(m.group(0))


class MembersResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        page = get_members_list_page()
        count = parse_members_count(page)
        results = {"members": count}
        resp.media = results


def create_api():
    """Creates and returns Facon API instance"""
    api = falcon.API()
    api.add_route("/members", MembersResource())
    return api


api = create_api()
