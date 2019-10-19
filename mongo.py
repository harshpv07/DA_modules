def mongoprint(ques):
    import pymongo
    import dns
    client = pymongo.MongoClient("mongodb+srv://admin:passw0rd123@cluster0-zixtz.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.stack
    for posts in client.stack.owndb.find({"question":ques}):
        return posts


def ins(ques,sol):
    import pymongo
    import dns
    client = pymongo.MongoClient("mongodb+srv://admin:passw0rd123@cluster0-zixtz.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.stack
    db.owndb.insert_one({"question": ques , "ans":sol})

if __name__ == "__main__":
    #ins("no module h5py","pip install h5py. thats it")
    ques = "bash: pip: command not found"
    ans = "This installs pip using the default python package installer system and saves you the hassle of manual set-up all at the same time."
    if(bool(mongoprint(ques)) == False):
        ins(ques,ans)
    else:
        print(mongoprint(ques))
    