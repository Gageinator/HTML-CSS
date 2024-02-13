import tornado.web
import random

D = {
    "alice":
    {
        "f_name" : "Alice",
        "l_name" : "Smith",
        "DOB" : "Jan.1",
        "email" : "alice@example.com",
        "image" : "/static/Alice.png"
    },
    "bob":
    {
        "f_name" : "Bob",
        "l_name" : "Jones",
        "DOB" : "Dec.31",
        "email" : "bob@bob.xyz",
        "image" : "/static/Bob.png"
    },
    "carol":
    {
        "f_name" : "Carol",
        "l_name" : "Ling",
        "DOB" : "Jul.17",
        "email" : "carol@example.com",
        "image" : "/static/Carol.png"
    },
    "dave":
    {
        "f_name" : "Dave",
        "l_name" : "N. Port",
        "DOB" : "Mar.14",
        "email" : "dave@dave.dave",
        "image" : "/static/Dave.png"
    }
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        L = self.request.path.split("/")
        uname = L[2]
        info = D[uname]
        self.render("ProfilePage.html",
                    f_name=info["f_name"], l_name=info["l_name"], dateOfBirth=info["DOB"],
                    email=info["email"], image=info["image"])
    def post(self):
        J=json.loads(self.request.body)
        f_name = J["f_name"]
        l_name = J["l_name"]
        dob = J["DOB"]
        ppic = base64.b64decode(J["image"])
        print("WE GOT:",f_name,l_name,dob,ppic[:20])
        resp={"ok": True}
        self.write( json.dumps(resp) )
        uname = L[2]
        D[uname]["f_name"] = f_name
        D[uname]["l_name"] = l_name
        D[uname]["DOB"] = dob
        D[uname]["image"] = ppic

        