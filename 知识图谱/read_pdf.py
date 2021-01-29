import PyPDF2

# 使用open的‘rb’方法打开pdf文件，使用二进制模式
my_pdf = open('./PDF/1.pdf', mode='rb')

# 调用PdfFileReader函数
# pdf_document = PyPDF2.PdfFileReader(my_pdf)

# 使用PdfFileReader对象的变量，获取各个信息，如numPages属性获取PDF文档的页数
# print(pdf_document.numPages)

# 调用PdfFileReader对象的getPage()方法，传入页码，取得Page对象：输出PDF文档的第一页内容
# first_page = pdf_document.getPage(0)

# 调用Page对象的extractText()方法，返回该页文本的字符串
# text = first_page.extractText()
# print(text)
pdf_document = PyPDF2.PdfFileReader(my_pdf, strict=False)
print(pdf_document.getDocumentInfo())
page_info = pdf_document.getPage(2)
print(page_info.extractText())
