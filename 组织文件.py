import shutil,os

#shutil.copy(source,destination)复制文件
#shutil.copytree(source,destination)复制整个文件夹
#shutil.move(source,destination)移动文件，如果没有目标文件夹，该函数会把文件改名
#os.unlink(path)删除path处的文件
#os.rmdir(path)删除文件夹
#os.rmtree(path)删除path处的文件夹，包含所有的文件
#send2trash模块安全删除pip install send2trash
#os.walk()遍历文件，返回文件夹名，子文件夹名，当前文件名
for folderName,subfolders,filenames in os.walk('e:\\python'):
    print('The current folder is '+folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF '+folderName+':'+subfolder)
    for filename in filenames:
        print('FILE INSIDE '+folderName+':'+filename)
    print('')

#zipfile.ZipFile()压缩一个文件
#zipfile.namelist()返回文件夹中的文件和文件夹
#zipfile.getinfo()返回file_size和compress_size
#zipfile.extractall()解压文件夹到当前目录第一个参数是文件名，第二个参数是路径
