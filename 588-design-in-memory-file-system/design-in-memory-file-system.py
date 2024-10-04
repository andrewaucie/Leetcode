class FileSystem:

    def __init__(self):
        self.path = {0: defaultdict(str)}

    def getDirectory(self, path):
        directory = self.path
        for item in path.split("/"):
            if item == '':
                continue
            if item not in directory:
                break
            directory = directory[item]
        return directory

    def ls(self, path: str) -> List[str]:
        #print(self.path)
        directory = self.path
        for item in path.split("/"):
            #print(item)
            if item == '':
                continue
            if item not in directory:
                return [item]
            directory = directory[item]
        #print(path, directory)
        items = []
        for d in directory:
            if d != 0:
                items.append(d)
        if 0 in directory:
            for f in directory[0]:
                items.append(f)
        return sorted(items)

    def mkdir(self, path: str) -> None:
        directory = self.path
        for d in path.split("/"):
            if d == '':
                continue
            if d not in directory:
                directory[d] = {0: defaultdict(str)}
            directory = directory[d]
        return

    def addContentToFile(self, filePath: str, content: str) -> None:
        d,f = filePath[:filePath.rindex('/')], filePath[filePath.rindex('/')+1:]
        self.mkdir(d)
        directory = self.getDirectory(d)
        directory[0][f] += content
        
    def readContentFromFile(self, filePath: str) -> str:
        d,f = filePath[:filePath.rindex('/')], filePath[filePath.rindex('/')+1:]
        directory = self.getDirectory(d)
        return directory[0][f]



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)