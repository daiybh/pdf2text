# -*- coding:utf-8 -*-
def pdf_to_image(pdfPath):
    from pdf2image import convert_from_path
    import os
    savePath=pdfPath+'out/'
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    pages=convert_from_path(pdfPath,fmt='jpeg',paths_only=True,output_file='pdf2png',output_folder=savePath,poppler_path=r'.\poppler-0.68.0\bin')
    return pages
    # i=0
    # for page in pages:
    #     page.save(pdfPath+'out'+str(i)+'.jpg', 'JPEG')
    #     i=i+1

if __name__ == '__main__':
    pdf_to_image('49.pdf')