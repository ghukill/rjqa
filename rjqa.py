import pandas as pd
import random
from sanic import Sanic
from sanic import response


########################################################################
# Settings
########################################################################
QA_FILE = 'jq_clean.csv'
WS_PORT = 42421


########################################################################
# Sanic app
########################################################################
app = Sanic()


########################################################################
# Helpers
########################################################################
def get_random_question():
	# load questions as dataframe
	df = pd.read_csv(QA_FILE)

	# get random row number
	rq_index = int(random.random() * len(df))

	# get random row
	rq = df.iloc[rq_index]

	# return
	return rq


########################################################################
# Routes
########################################################################
@app.route("/json")
async def random_question(request):

	# get random question
	rq = get_random_question()

	# return as json
	return response.raw(
		rq.to_json().encode('utf-8'),
		headers={
			'Content-Type':'application/json'
		}
	)


@app.route("/")
async def random_question(request):

	# get random question
	rq = get_random_question()

	# return as json
	return response.html('<html><head><script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha256-k2WSCIexGzOj3Euiig+TlR8gA0EmPjuc79OEeY5L45g=" crossorigin="anonymous"></script></head><body><h1>RJQA</h1><p><strong>Category:</strong> %s</p><p><strong>Value:</strong> %s</p><p><strong>Clue:</strong> %s</p><p><a href="#" onclick="$(\'#answer\').show(); return false;">show me the question...</a></p><p style="display:none;" id="answer"><strong>Question:</strong> %s</p></body></html>' % (rq.category, rq.value, rq.question, rq.answer))


########################################################################
# Main loop
########################################################################
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=WS_PORT)