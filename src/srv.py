

import falcon

from src.nyt_data import get_state_data

class ThingsResource(object):
    def on_get(self, req, res):

        res.status = falcon.HTTP_200
        res.body = "Hello"
        print(get_state_data('washington').get('2020-03-24'))

class StatesResource(object):
    def on_get(self, req, res, state):
        res.status = falcon.HTTP_200
        res.body = "200 OK"
        print(get_state_data(state).get('2020-03-24'))

app = falcon.API()
things = ThingsResource()
states = StatesResource()

app.add_route('/', things)
app.add_route('/state/{state}', states)


banner = (
    "\033[0;33m -------------------------------- C O V I D - 19  U. S.  S T A T S ---------------------------------------\033[0m\n"
)
MOON_PHASES = (
    u"🌑", u"🌒", u"🌓", u"🌔", u"🌕", u"🌖", u"🌗", u"🌘"
)


# (
#             "\033[44m     .-.     \033[0m\n"
# 			"\033[44;31m    (   ).   \033[0m\n"
# 			"\033[44m   (___(__)  \033[0m\n"
# 			"\033[38;5;255m    *  *  *  \033[0m\n"
# 			"\033[38;5;255m   *  *  *   \033[0m\n"
#         )