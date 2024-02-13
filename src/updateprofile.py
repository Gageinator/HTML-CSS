import tornado.web
import json
import base64
import ProfilePage

class Handler(tornado.web.RequestHandler):
    def get(self):
        L = self.request.path.split("/")
        uname = L[2]
        info = ProfilePage.D[uname]
        self.render("ProfilePage.html",
                    f_name=info["f_name"], l_name=info["l_name"], dateOfBirth=info["DOB"],
                    email=info["email"], image=info["image"])
    def post(self):
        print(self.request.path)
        J=json.loads(self.request.body)
        firstName = J["firstName"]
        lastName = J["lastName"]
        dob = J["birthDate"]
        ppic = "data:image/png;base64," + (J["pic"])
        print("WE GOT:",firstName,lastName,dob,ppic[:20])
        resp={"ok": True}
        self.write( json.dumps(resp) )
        
        L = self.request.path.split("/")
        uname = L[2]
        ProfilePage.D[uname]["f_name"] = firstName
        ProfilePage.D[uname]["l_name"] = lastName
        ProfilePage.D[uname]["DOB"] = dob
        ProfilePage.D[uname]["image"] = ppic