class chains(object):
    def __init__(self,path=''):
        self.path = path

    def __str__(self):
        return self.path

    def __getattr__(self,path):
        return chains('%s/%s' %(self.path,path))

print(chains().status.user.list)
