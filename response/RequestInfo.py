class RequestInfo(object):

    action = None

    def __init__(self, req):
        if isinstance(req, dict):
            self.action = req.get("action", "")
