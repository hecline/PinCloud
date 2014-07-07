from pinterest.client import raw_client
import unirest
import webbrowser
#	Key
APP_SECRET = "<INSERT SECRET KEY HERE>"
APP_ID = "<INSERT APP ID HERE>"

my_client = raw_client(APP_ID, APP_SECRET)

#	User input
check = 'z'

while check != "Y" and check != "y":
	usn = raw_input("Enter your Pinterest account name\n>")
	board = raw_input("Enter the board title" + "\n>" + "(please pick boards without special characters in the title)" + "\n")
	print "Username: " + usn + "\n" + "Board Title: " + board + "\n"
	check = raw_input("Is this information correct? [y/n]" + "\n>")

board = board.replace(" ", "-")

#	Pull pin descriptions from user's board
response, bookmark = getattr(my_client.boards, usn)(board).pins.get()

#	Print response
for each_pin in response:
	x=1
print "Generating word cloud...."
cloud_text = each_pin["description"]

#	Cloud
response = unirest.post("https://gatheringpoint-word-cloud-maker.p.mashape.com/index.php", 
	headers={ 
	"X-Mashape-Authorization": "g7tB4AOaI3DnfTco5sF7rTPkrtBtg8qB"
	},
	params={
	 "height": 600,
	 "textblock": cloud_text,
	 "width": 700,
	 "config": "n\/a"
	}
);
new = 0
webbrowser.open(response.body["url"], new=new)
