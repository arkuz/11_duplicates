import os


if __name__ == '__main__':
    path = os.getcwd()

    print(path)


    r = os.walk('/home/arkuz/Devman/GitHub/11_duplicates')

    for i in r:
        print(i)
    print('=' * 20)


    def crawlDirectories(directoryToCrawl):
        output = []
        for path, dirnames, filenames in os.walk(directoryToCrawl):
            for fname in filenames:
                output.append(os.path.join(path, fname))
        return output

    t = crawlDirectories('/home/arkuz/Devman/GitHub/11_duplicates')

    for i in t:
        print(i)
