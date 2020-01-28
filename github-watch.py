g = Github("Github token")


if __name__ =="__main__":
    for repo in g.get_user().get_repos():
        if (repo.full_name.find('jeygith') != -1 or repo.full_name.find('news-archive') !=-1 ):  
            print(repo.full_name.find('jeygith || news-archive'))
            print repo.full_name
            print(g.get_user().add_to_watched(repo))
        else:
            print 'other'
            print repo.full_name
        # if (repo.full_name.find('jeygith')):  
        #     print repo
        #     print 'found jeygith'
        # else:
        #     print 'other'
        #     print repo
        #     #print(g.get_user().add_to_watched(repo))