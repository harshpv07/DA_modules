def git_push(commit_mess,path,username,password):
    import os
    path = "/home/Desktop/test18"
    path_split = path.split("/")[len(path.split("/"))-1]
    print(i.type())
    from mongo_cred import mongoprint
    for i in mongoprint(username,password):
        if(i['names'] == path_split):
            os.system("cd "+path + " && git init" + " && git add ." + " && git commit -m " + commit_mess + " && git remote add origin " +i["projects"] + " && git push origin master")



#clone the remote repo
def git_clone(path,repo_url):
    import os
    os.system("cd "+ path + " && git clone " + str(repo_url))

#commit the current repo
def git_commit(path,commit_mess):
    import os
    os.system("git add . && git commit -m " + commit_mess)
