
def x(pdfPath):
    import pdf2png

    images=pdf2png.pdf_to_image(pdfPath)


    import cvtable
    
    cutPaths=cvtable.cutImage(images[1])
    
    import baidu
    #page1
    page1Text=baidu.doOCR(cutPaths[0])

    page2Text=baidu.doOCR(cutPaths[1])

    import anlyzeText
    ret1=anlyzeText.anlyzePage1(page1Text)
    ret2=anlyzeText.anlyzePage2(page2Text)

    with open('ret.csv','a') as f:
        for a in ret1:
            f.write(a+',')
        f.write(ret2)
        f.write('\n')
import os
import glob
import shutil
doneFolder = './pdfDone'
srcFolder='./pdf'


def doWork(pdfPath):
    print(pdfPath)
    full_path = os.path.join(doneFolder, pdfPath[len(srcFolder)+1:])
    xf = full_path[:full_path.rindex('\\')]
    if not os.path.exists(xf):
        os.makedirs(xf)
    x(pdfPath)
    shutil.move(pdfPath,full_path)


for root,dirs,files in os.walk(srcFolder):
    #print('root_dir:', root)  # 当前目录路径
    #print('sub_dirs:', dirs)  # 当前路径下所有子目录
    #print('files:', files)  # 当前路径下所有非目录子文件
    for f in files:
        if os.path.splitext(f)[1] !='.pdf':
            continue
        doWork(os.path.join(root, f))

    
    
    
#x('49.pdf')