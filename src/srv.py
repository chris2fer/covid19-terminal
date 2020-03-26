

import falcon

class ThingsResource(object):
    def on_get(self, req, res):

        res.status = falcon.HTTP_200
        res.body = (
            "\033[44m     .-.     \033[0m\n"
			"\033[44;31m    (   ).   \033[0m\n"
			"\033[44m   (___(__)  \033[0m\n"
			"\033[38;5;255m    *  *  *  \033[0m\n"
			"\033[38;5;255m   *  *  *   \033[0m\n"
        )


app = falcon.API()

things = ThingsResource()

app.add_route('/', things)
